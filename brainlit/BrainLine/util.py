import urllib
import json
import numpy as np
import os
import networkx as nx
from pathlib import Path
from brainlit.BrainLine.parse_ara import build_tree
from tqdm import tqdm
from brainlit.BrainLine.imports import *
import json
from cloudvolume.exceptions import OutOfBoundsError


def download_subvolumes(
    data_dir: str,
    brain_id: str,
    layer_names: list,
    dataset_to_save: str,
    data_file: str,
):
    """Download subvolumes around a set of manually marked points for validation of machine learning model.

    Args:
        data_dir (str): Path to directory where subvolumes will be saved.
        brain_id (str): Brain ID key in brain2paths dictionary from soma_data or axon_data/
        layer_names (list): List of precomputed layer names associated with the brain_id, ordered by primary signal channel (e.g. antibody), background channel, and secondary signal channel (e.g. endogenous fluorescence).
        dataset_to_save (str): val or train - specifies which set of subvolumes should be downloaded, if applicable.
        data_file (str): path to json file with data information.

    Raises:
        ValueError: If object_type is not soma or axon
    """
    with open(data_file) as f:
        data = json.load(f)
    object_type = data["object_type"]
    brain2paths = data["brain2paths"]

    if object_type == "soma":
        radius = 25
    elif object_type == "axon":
        radius = 50
    else:
        raise ValueError(f"object_type must be soma or axon, not {object_type}")

    if isinstance(data_dir, str):
        data_dir = Path(data_dir)

    base_dir = data_dir / f"brain{brain_id}" / dataset_to_save
    antibody_layer, background_layer, endogenous_layer = layer_names

    vols = []
    if "base_s3" in brain2paths[brain_id].keys():
        base_dir_s3 = brain2paths[brain_id]["base_s3"]
        for layer in [antibody_layer, background_layer, endogenous_layer]:
            if layer == "zero":
                vol = "zero"
            else:
                dir = base_dir_s3 + layer
                vol = CloudVolume(dir, parallel=1, mip=0, fill_missing=True)
                print(f"{layer} shape: {vol.shape} at {vol.resolution}")
                dtype = vol.dtype
            vols.append(vol)
    else:
        raise ValueError(f"base_s3 not an entry in brain2paths for brain {brain_id}")

    dataset_title = dataset_to_save + "_info"
    url = brain2paths[brain_id][dataset_title]["url"]
    l_dict = json_to_points(url)
    if object_type == "soma":
        soma_centers = l_dict[brain2paths[brain_id][dataset_title]["somas_layer"]]
        nonsoma_centers = l_dict[brain2paths[brain_id][dataset_title]["nonsomas_layer"]]
        centers_groups = [soma_centers, nonsoma_centers]
        suffixes = ["_pos", "_neg"]
    elif object_type == "axon":
        axon_centers = l_dict[brain2paths[brain_id][dataset_title]["layer"]]
        centers_groups = [axon_centers]
        suffixes = [""]

    print(f"{[len(c) for c in centers_groups]} centers")

    isExist = os.path.exists(base_dir)
    if not isExist:
        print(f"Creating directory: {base_dir}")
        os.makedirs(base_dir)
    else:
        print(f"Downloaded data will be stored in {base_dir}")

    for suffix, centers in zip(suffixes, centers_groups):
        for i, center in enumerate(tqdm(centers, desc="Saving samples")):
            images = []
            for vol in vols:
                if vol == "zero":
                    image = np.zeros([2 * radius - 1 for k in range(3)], dtype=dtype)
                else:
                    image = vol[
                        center[0] - radius + 1 : center[0] + radius,
                        center[1] - radius + 1 : center[1] + radius,
                        center[2] - radius + 1 : center[2] + radius,
                    ]
                    image = image[:, :, :, 0]
                images.append(image)

            image = np.squeeze(np.stack(images, axis=0))

            fname = (
                base_dir
                / f"{int(center[0])}_{int(center[1])}_{int(center[2])}{suffix}.h5"
            )
            with h5py.File(fname, "w") as f:
                dset = f.create_dataset("image_3channel", data=image)


def _get_corners(
    shape, chunk_size, min_coords: list = [-1, -1, -1], max_coords: list = [-1, -1, -1]
):
    corners = []
    for i in tqdm(range(0, shape[0], chunk_size[0])):
        for j in tqdm(range(0, shape[1], chunk_size[1]), leave=False):
            for k in range(0, shape[2], chunk_size[2]):
                c1 = [i, j, k]
                c2 = [
                    np.amin([shape[idx], c1[idx] + chunk_size[idx]]) for idx in range(3)
                ]
                conditions_max = [
                    (max == -1 or c < max) for c, max in zip(c1, max_coords)
                ]
                conditions_min = [
                    (min == -1 or c > min) for c, min in zip(c2, min_coords)
                ]
                conditions = conditions_max + conditions_min
                if all(conditions):
                    corners.append([c1, c2])

    return corners


def json_to_points(url, round=False) -> dict:
    """Extract points from a neuroglancer url.

    Args:
        url (str): url to neuroglancer state (that was posted to neurodata json server).
        round (bool, optional): whether to round coordinates to integers. Defaults to False.

    Returns:
        dict: Keys are names of point layers and values are lists of points from that layer.
    """
    if url[-5:] == ".json":
        with open(url) as f:
            js = json.load(f)
    else:
        pattern = "json_url="
        idx = url.find(pattern) + len(pattern)

        json_url = url[idx:]

        data = urllib.request.urlopen(json_url)

        string = data.readlines()[0].decode("utf-8")

        js = json.loads(string)

    point_layers = {}

    for layer in js["layers"]:
        if layer["type"] == "annotation":
            points = []
            for point in layer["annotations"]:
                coord = point["point"]
                if round:
                    coord = [int(np.round(c)) for c in coord]
                points.append(coord)
            point_layers[layer["name"]] = points
    return point_layers


def _find_sample_names(dir, dset="", add_dir=False):
    """Find file paths of samples in a given directory according to filters used in the workflow.


    Args:
        dir (str): path to directory.
        dset (str, optional): dataset type identifier. Defaults to "val".
        add_dir (bool, optional): whether output paths should include the directory path. Defaults to False.

    Returns:
        list: list of file path strings.
    """
    dir = Path(dir)
    items = os.listdir(dir)

    items = [item for item in items if ".h5" in item]
    items = [item for item in items if "Probabilities" not in item]
    items = [item for item in items if "Labels" not in item]
    items = [item for item in items if dset in item]

    if add_dir:
        items = [str(dir / item) for item in items]

    return items


def _setup_atlas_graph(ontology_json_path: str):
    """Create networkx graph of regions in allen atlas (from ara_structure_ontology.json). Initially uses vikram's code in build_tree, then converts to networkx.

    Args:
        ontology_json_path (str): path to ontology json.

    Returns:
        nx.DiGraph: graph representing hierarchy of allen parcellation.
    """
    # create vikram object
    f = json.load(
        open(
            ontology_json_path,
            "r",
        )
    )

    tree = build_tree(f)

    # create nx graph
    queue = [tree]
    G = nx.DiGraph()
    max_level = 0

    while len(queue) > 0:
        node = queue.pop(0)
        if node.level > max_level:
            max_level = node.level
        G.add_node(
            node.id,
            level=node.level,
            st_level=node.st_level,
            name=node.name,
            acronym=node.acronym,
            label=str(node.st_level) + ") " + node.name,
        )
        if node.parent_id is not None:
            G.add_edge(node.parent_id, node.id)

        queue += node.children

    return G


def _get_atlas_level_nodes(atlas_level, atlas_graph):
    """Find regions in atlas that are at a specified level in the hierarchy

    Args:
        atlas_level (int): desired level in the atlas.
        atlas_graph (nx.DiGraph): graph of allen atlas, created from setup_atlas_graph.

    Returns:
        list: list of region ids at the desired hierarchy level.
    """
    atlas_level_nodes = []

    for node in atlas_graph.nodes:
        if atlas_graph.nodes[node]["st_level"] == atlas_level:
            atlas_level_nodes.append(node)
    return atlas_level_nodes


def _find_atlas_level_label(label, atlas_level_nodes, atlas_level, G):
    """Map a given region label to a label at a specified level in the hierarchy.

    Args:
        label (int): region label.
        atlas_level_nodes (list): list of region IDs to which label will be mapped.
        atlas_level (int): level at which the atlas_level_nodes come from.
        G (nx.DiGraph): network of region hierarchy.

    Raises:
        ValueError: Found a node that has more than one parent (which is not possible for a tree).
        ValueError: Was not able to find a node at the desired atlas_level to map the label to.

    Returns:
        int: the relevant atlas label at the desired level in the hierarchy.
    """
    if label == 0 or label not in G.nodes or G.nodes[label]["st_level"] <= atlas_level:
        return label
    else:
        counter = 0
        # find which region of atlas_level is parent
        for atlas_level_node in atlas_level_nodes:
            if label in nx.algorithms.dag.descendants(G, source=atlas_level_node):
                counter += 1
                atlas_level_label = atlas_level_node
        if counter == 0:
            preds = list(G.predecessors(label))
            if len(preds) != 1:
                raise ValueError(f"{len(preds)} predecessors of node {label}")
            atlas_level_label = _find_atlas_level_label(
                preds[0], atlas_level_nodes, atlas_level, G
            )
            counter += 1
        if counter != 1:
            raise ValueError(f"{counter} atlas level predecessors of {label}")
        return atlas_level_label


def _fold(image):
    """Take a 2D image and add the left half to a reflected version of the right half.

    Args:
        image (nd.array): Image to be folded

    Returns:
        nd.array: Folded image.
    """
    half_width = np.round(image.shape[1] / 2).astype(int)
    left = image[:, :half_width]
    right = image[:, half_width:]
    left = left + np.flip(right, axis=1)
    return left


def create_transformed_mask_info(brain, data_file):
    atlas_vol = CloudVolume(
        "precomputed://https://open-neurodata.s3.amazonaws.com/ara_2016/sagittal_10um/annotation_10um_2017"
    )

    with open(data_file) as f:
        data = json.load(f)
    brain2paths = data["brain2paths"]
    layer_path = brain2paths[brain]["base_s3"] + "axon_mask_transformed"
    print(f"Writing info file at {layer_path}")

    info = CloudVolume.create_new_info(
        num_channels=1,
        layer_type="image",
        data_type="uint16",  # Channel images might be 'uint8'
        encoding="raw",  # raw, jpeg, compressed_segmentation, fpzip, kempressed
        resolution=atlas_vol.resolution,  # Voxel scaling, units are in nanometers
        voxel_offset=atlas_vol.voxel_offset,
        chunk_size=[32, 32, 32],  # units are voxels
        volume_size=atlas_vol.volume_size,  # e.g. a cubic millimeter dataset
    )
    vol_mask = CloudVolume(layer_path, info=info)
    vol_mask.commit_info()


def dir_to_atlas_pts(dir, outname, atlas_file):
    """Read coordinates from JSON, remove points that don't fall in interior of atlas, and write a text file.

    Args:
        dir (str): Path to folder with JSON files that contain detection coordiantes.
        outname (str): Name of file to be written.
        atlas_file (str): Name of downloaded atlas parcellation image.
    """
    vol = io.imread(atlas_file)
    files = [
        Path(dir) / f for f in os.listdir(dir) if os.path.splitext(f)[1] == ".json"
    ]

    coords = []
    for file in tqdm(files, "Processing point files..."):
        with open(file) as f:
            json_file = json.load(f)

        for pt in tqdm(json_file, "Finding interior points..."):
            coord = pt["point"]
            try:
                if vol[int(coord[0]), int(coord[1]), int(coord[2])] != 0:
                    coords.append(str(coord))
            except IndexError:
                pass

    with open(outname, "a") as f:
        f.write("\n".join(coords))
