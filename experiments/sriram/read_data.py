import aicspylibczi
from skimage import io
from skimage.transform import resize
import numpy as np
import zarr
from tqdm import tqdm
from cloudvolume import CloudVolume
import igneous.task_creation as tc
from taskqueue import LocalTaskQueue
import h5py
from brainlit.algorithms.generate_fragments.state_generation import state_generation
from brainlit.utils.write import czi_to_zarr, zarr_to_omezarr
import dask.array as da
from ome_zarr.writer import write_image
from ome_zarr.io import parse_url

task = "convert"

if task == "convert":
    czi_path = "/cis/project/sriram/for Tomi/exp227-mouse3-stitched.czi"
    out_dir = "/cis/project/sriram/ng_data/exp227/"

    zarr_paths = czi_to_zarr(czi_path=czi_path, out_dir=out_dir)

    out_path = "/cis/project/sriram/ng_data/exp227/fg_ome.zarr"
    zarr_to_omezarr(zarr_path=zarr_paths[0], out_path=out_path)

elif task == "writeng":
    outpath_prefix = "precomputed://file:///cis/home/tathey/projects/mouselight/sriram/neuroglancer_data/somez/"

    sz = [6814, 8448, 316]

    path = "/cis/project/sriram/Sriram/SS IUE 175 SNOVA RFP single channel AdipoClear Brain 3 ipsilateral small z two colour Image1.czi"
    czi = aicspylibczi.CziFile(path)

    for c, suffix in zip([0, 1], ["fg", "bg"]):
        outpath = outpath_prefix + suffix
        info = CloudVolume.create_new_info(
            num_channels=1,
            layer_type="image",
            data_type="uint16",  # Channel images might be 'uint8'
            # raw, png, jpeg, compressed_segmentation, fpzip, kempressed, zfpc, compresso
            encoding="raw",
            resolution=[500, 500, 3000],  # Voxel scaling, units are in nanometers
            voxel_offset=[0, 0, 0],  # x,y,z offset in voxels from the origin
            # Pick a convenient size for your underlying chunk representation
            # Powers of two are recommended, doesn't need to cover image exactly
            chunk_size=[128, 128, 1],  # units are voxels
            volume_size=sz,  # e.g. a cubic millimeter dataset
        )

        print(f"Posting info: {info} to {outpath}")
        vol = CloudVolume(outpath, info=info, compress=False)
        vol.commit_info()

        num_slices = sz[2]
        for z in tqdm(np.arange(num_slices), desc="Saving slices..."):
            im_slice = np.squeeze(czi.read_mosaic(C=c, Z=z, scale_factor=1))
            im_slice = np.expand_dims(im_slice, axis=2)
            vol[:, :, z] = im_slice

    layer_path_prefix = "precomputed://file:///cis/home/tathey/projects/mouselight/sriram/neuroglancer_data/somez/"
    for suffix in ["fg", "bg"]:
        layer_path = layer_path_prefix + suffix
        print(f"Downsampling {layer_path}")

        tq = LocalTaskQueue(parallel=8)

        tasks = tc.create_downsampling_tasks(
            layer_path,  # e.g. 'gs://bucket/dataset/layer'
            mip=0,  # Start downsampling from this mip level (writes to next level up)
            fill_missing=True,  # Ignore missing chunks and fill them with black
            axis="z",
            num_mips=3,  # number of downsamples to produce. Downloaded shape is chunk_size * 2^num_mip
            chunk_size=None,  # manually set chunk size of next scales, overrides preserve_chunk_size
            preserve_chunk_size=True,  # use existing chunk size, don't halve to get more downsamples
            sparse=False,  # for sparse segmentation, allow inflation of pixels against background
            bounds=None,  # mip 0 bounding box to downsample
            encoding=None,  # e.g. 'raw', 'compressed_segmentation', etc
            delete_black_uploads=False,  # issue a delete instead of uploading files containing all background
            background_color=0,  # Designates the background color
            compress="gzip",  # None, 'gzip', and 'br' (brotli) are options
            factor=(2, 2, 2),  # common options are (2,2,1) and (2,2,2)
        )

        tq.insert(tasks)
        tq.execute()
elif task == "readng":
    ng_path = "precomputed://file:///cis/home/tathey/projects/mouselight/sriram/neuroglancer_data/somez/fg"
    vol = CloudVolume(ng_path, compress=False)

    print(vol.shape)
    print(vol[500:600, 500:600, 150])
elif task == "saveilastik":
    z = zarr.open("/cis/home/tathey/projects/mouselight/sriram/somez.zarr")
    corners = [
        [4000, 2100, 150],
        [3000, 2500, 150],
        [5500, 1000, 100],
        [2000, 6000, 160],
        [4000, 7000, 200],
    ]
    for i, corner in enumerate(tqdm(corners, desc="saving samples...")):
        im = z[
            :,
            corner[0] : corner[0] + 220,
            corner[1] : corner[1] + 220,
            corner[2] : corner[2] + 20,
        ]

        fname = f"/cis/home/tathey/projects/mouselight/sriram/ilastik_training/somez_training_{corner[0]}_{corner[1]}_{corner[2]}_.h5"
        with h5py.File(fname, "w") as f:
            dset = f.create_dataset("image_2channel", data=im)
elif task == "stategen":
    sg = state_generation(
        image_path="/cis/project/sriram/ng_data/sriram-adipo-brain1-im3/fg_ome.zarr/0/",
        new_layers_dir="/cis/project/sriram/ng_data/sriram-adipo-brain1-im3/",
        ilastik_program_path="/cis/home/tathey/ilastik-1.3.3post3-Linux/run_ilastik.sh",
        ilastik_project_path="/cis/project/sriram/ilastik_data/axon_segmentation.ilp",
        fg_channel=0,
        chunk_size=[300, 300, 160],
        resolution=[0.5, 0.5, 3],
        parallel=4,
    )

    sg.predict(data_bin="/cis/project/sriram/temp/")
    sg.compute_frags()
    sg.compute_image_tiered()
    sg.compute_soma_lbls()
    sg.compute_states()
    sg.compute_edge_weights()

elif task == "segng":

    # im_path = "precomputed://file:///cis/home/tathey/projects/mouselight/sriram/neuroglancer_data/somez/im"
    # vol_im = CloudVolume(im_path, compress=False)
    # resolution = vol_im.resolution
    z = zarr.open("/cis/project/sriram/ng_data/sriram-adipo-brain1-im3/fg.zarr")
    volume_size = z.shape
    chunk_size = z.chunks
    resolution = [1, 1, 1]

    outpath = "precomputed://file:///cis/project/sriram/ng_data/sriram-adipo-brain1-im3/traces"

    info = CloudVolume.create_new_info(
        num_channels=1,
        layer_type="segmentation",
        data_type="uint16",  # Channel images might be 'uint8'
        # raw, png, jpeg, compressed_segmentation, fpzip, kempressed, zfpc, compresso
        encoding="raw",
        resolution=resolution,  # Voxel scaling, units are in nanometers
        voxel_offset=[0, 0, 0],  # x,y,z offset in voxels from the origin
        # Pick a convenient size for your underlying chunk representation
        # Powers of two are recommended, doesn't need to cover image exactly
        chunk_size=chunk_size,  # units are voxels
        volume_size=volume_size,  # e.g. a cubic millimeter dataset
        skeletons="skeletons",
    )
    vol = CloudVolume(outpath, info=info, compress=False)
    vol.commit_info()
    vol.skeleton.meta.commit_info()

    # outpath = "precomputed://file:///cis/home/tathey/projects/mouselight/sriram/neuroglancer_data/somez/fragments"
    # frags_path = "/cis/home/tathey/projects/mouselight/sriram/somez_labels.zarr"
    # frags = zarr.open(frags_path, "r")

    # info = CloudVolume.create_new_info(
    #     num_channels=1,
    #     layer_type="segmentation",
    #     data_type="uint16",  # Channel images might be 'uint8'
    #     # raw, png, jpeg, compressed_segmentation, fpzip, kempressed, zfpc, compresso
    #     encoding="raw",
    #     resolution=[500, 500, 3000],  # Voxel scaling, units are in nanometers
    #     voxel_offset=[0, 0, 0],  # x,y,z offset in voxels from the origin
    #     # Pick a convenient size for your underlying chunk representation
    #     # Powers of two are recommended, doesn't need to cover image exactly
    #     chunk_size=[128, 128, 1],  # units are voxels
    #     volume_size=frags.shape,  # e.g. a cubic millimeter dataset
    # )

    # print(f"Posting info: {info} to {outpath}")
    # vol = CloudVolume(outpath, info=info, compress=False)
    # vol.commit_info()

    # for z in tqdm(np.arange(frags.shape[-1]), desc="Writing fragments..."):
    #     slice = frags[:, :, z]
    #     slice = np.expand_dims(slice, axis=2)
    #     vol[:, :, z] = slice
