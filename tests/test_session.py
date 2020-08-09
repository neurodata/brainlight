import pytest
from brainlit.utils.session import NeuroglancerSession
from brainlit.utils.upload import get_volume_info, create_cloud_volume
import SimpleITK as sitk
import scipy.ndimage
import numpy as np
import warnings
from pathlib import Path
import networkx as nx
from cloudvolume import CloudVolume
from cloudvolume.lib import Bbox
from cloudvolume.exceptions import InfoUnavailableError


@pytest.fixture
def vars():
    url = "s3://mouse-light-viz/precomputed_volumes/brain1_2"  # remove _2 when upload done.
    url_segments = url + "_segments"
    url_annotations = url + "_annotations"
    mip = 0
    seg_id = 2
    v_id = 300
    return url, url_segments, url_annotations, mip, seg_id, v_id


@pytest.fixture
def vars_local():
    top_level = Path(__file__).parents[1] / "data"
    input = (top_level / "data_octree").as_posix()
    url = (top_level / "test_upload").as_uri()
    url_segments = url + "_segments"
    url_annotations = url + "_annotations"
    mip = 0
    seg_id = 2
    v_id = 300
    return top_level, input, url, url_segments, url_annotations, mip, seg_id, v_id


@pytest.fixture
def session(vars):
    url, url_seg, url_ann, mip, seg_id, v_id = vars
    sess = NeuroglancerSession(
        url=url, mip=mip, url_segments=url_seg, url_annotations=url_ann
    )
    return sess, seg_id, v_id


@pytest.fixture
def session_local(vars_local):
    top_level, input, url, url_seg, url_ann, mip, seg_id, v_id = vars_local
    sess = NeuroglancerSession(
        url=url, mip=mip, url_segments=url_seg, url_annotations=url_ann
    )
    return sess, seg_id, v_id


def test_ensure_local_data(vars_local):
    """Reruns uploads from test_upload to ensure data is available.
    """
    top_level, input, url, url_seg, url_ann, mip, seg_id, v_id = vars_local
    dir = top_level / "test_upload" / "serial"
    if not (dir / "info").is_file():
        upload.upload_volumes(input.as_posix(), dir.as_uri(), NUM_RES)
    assert   # contains info file



####################
### input checks ###
####################


def test_session_no_urls(vars):
    """Tests that initializing a NeuroglancerSession object without passing urls is valid.
    """
    url, url_segments, url_annotations, mip, seg_id, v_id = vars
    NeuroglancerSession(url)
    NeuroglancerSession(url, url_segments=url_segments)
    NeuroglancerSession(url, url_annotations=url_annotations)
    NeuroglancerSession(url, 0, url_segments, url_annotations)


def test_session_incomplete_urls(vars):
    """Tests that initializing a NeuroglancerSession on data without segmentation or annotation channels is valid and raises a warning.
    """
    top_level = Path(__file__).parents[1] / "data"
    input = (top_level / "data_octree").as_posix()
    path = (top_level / "test_img_only").as_uri()
    # create img volume info file
    (_, _, vox_size, img_size, _) = get_volume_info(input, 1,)
    vols = create_cloud_volume(path, img_size, vox_size, 1, layer_type="image",)
    with pytest.warns(UserWarning):
        sess = NeuroglancerSession(path)
    with pytest.warns(UserWarning):
        sess = NeuroglancerSession(
            path,
            url_segments="s3://mouse-light-viz/precomputed_volumes/brain1_segments",
        )


def test_session_bad_urls(vars):
    """Tests that initializing a NeuroglancerSession object by passing bad urls isn't valid.
    """
    url, url_segments, url_annotations, mip, seg_id, v_id = vars
    url_bad = url + "0"  # bad url
    url_segments_bad = url_segments + "0"  # bad url
    url_annotations_bad = url_annotations + "0"
    with pytest.raises(InfoUnavailableError):
        sess = NeuroglancerSession(url_bad)
    with pytest.raises(InfoUnavailableError):
        sess = NeuroglancerSession(url, url_segments=url_segments_bad)
    with pytest.raises(InfoUnavailableError):
        sess = NeuroglancerSession(url, url_annotations=url_annotations_bad)


def test_NeuroglancerSession_bad_inputs(vars):
    """Tests that errors are raised when bad inputs are given to initializing session.NeuroglancerSession.
    """
    url, url_seg, url_ann, mip, seg_id, v_id = vars
    with pytest.raises(TypeError):
        NeuroglancerSession(url=0, mip=mip, url_segments=url_seg)
    with pytest.raises(NotImplementedError):
        NeuroglancerSession(url="asdf", mip=mip, url_segments=url_seg)
    with pytest.raises(TypeError):
        NeuroglancerSession(url=url, mip=mip, url_segments=0)
    with pytest.raises(NotImplementedError):
        NeuroglancerSession(url=url, mip=mip, url_segments="asdf")
    with pytest.raises(TypeError):
        NeuroglancerSession(url=url, mip=1.5, url_segments=url_seg)
    with pytest.raises(ValueError):
        NeuroglancerSession(url=url, mip=-1, url_segments=url_seg)
    with pytest.raises(ValueError):
        NeuroglancerSession(url=url, mip=100, url_segments=url_seg)


def test_set_url_segments_bad_inputs(session):
    """Tests that errors are raised when bad inputs are given to session.set_url_segments.
    """
    sess, seg_id, v_id = session
    with pytest.raises(TypeError):
        sess.set_url_segments(0)
    with pytest.raises(NotImplementedError):
        sess.set_url_segments("asdf")


def test_get_segments_bad_inputs(session):
    """Tests that errors are raised when bad inputs are given to session.get_segments.
    """
    sess, seg_id, v_id = session
    bbox = (0, 0, 0, 10, 10, 10)
    bad_bbox = (-1, 0, 0, 10, 10, 10)
    with pytest.raises(TypeError):
        sess.get_segments(1.5, bbox)
    with pytest.raises(TypeError):
        sess.get_segments(seg_id, 0)
    with pytest.raises(ValueError):
        sess.get_segments(seg_id, bad_bbox)


def test_pull_voxel_bad_inputs(session):
    """Tests that errors are raised when bad inputs are given to session.pull_voxel.
    """
    sess, seg_id, v_id = session
    with pytest.raises(TypeError):
        sess.pull_voxel(1.5, v_id)
    with pytest.raises(TypeError):
        sess.pull_voxel(seg_id, 1.5)
    with pytest.raises(ValueError):
        sess.pull_voxel(seg_id, -1)
    with pytest.raises(ValueError):
        sess.pull_voxel(seg_id, 10000000)
    with pytest.raises(TypeError):
        sess.pull_voxel(seg_id, v_id, radus=1.5)
    with pytest.raises(ValueError):
        sess.pull_voxel(seg_id, v_id, radius=-1)


def test_pull_vertex_list_bad_inputs(session):
    """Tests that errors are raised when bad inputs are given to session.pull_vertex_list.
    """
    sess, seg_id, v_id = session
    v_id = [
        v_id,
    ]
    with pytest.raises(TypeError):
        sess.pull_vertex_list(1.5, v_id)
    with pytest.raises(TypeError):
        sess.pull_vertex_list(seg_id, 1)
    with pytest.raises(ValueError):
        sess.pull_vertex_list(seg_id, [-1,])
    with pytest.raises(ValueError):
        sess.pull_vertex_list(seg_id, [10000000,])
    with pytest.raises(TypeError):
        sess.pull_vertex_list(seg_id, v_id, buffer=1.5)
    with pytest.raises(ValueError):
        sess.pull_vertex_list(seg_id, v_id, buffer=-1)
    with pytest.raises(TypeError):
        sess.pull_vertex_list(seg_id, v_id, expand="asdf")


def test_pull_chunk_bad_inputs(session):
    """Tests that errors are raised when bad inputs are given to session.pull_chunks.
    """
    sess, seg_id, v_id = session
    with pytest.raises(TypeError):
        sess.pull_chunk(1.5, v_id)
    with pytest.raises(TypeError):
        sess.pull_chunk(seg_id, 1.5)
    with pytest.raises(ValueError):
        sess.pull_chunk(seg_id, -1)
    with pytest.raises(ValueError):
        sess.pull_chunk(seg_id, 10000000)
    with pytest.raises(TypeError):
        sess.pull_chunk(seg_id, v_id, radus=1.5)
    with pytest.raises(ValueError):
        sess.pull_chunk(seg_id, v_id, radius=-1)


def test_pull_bounds_img_bad_inputs(session):
    """Tests that errors are raised when bad inputs are given to session.pull_bounds_img.
    """
    sess, seg_id, v_id = session
    with pytest.raises(TypeError):
        sess.pull_bounds_img(0)
    with pytest.raises(ValueError):
        sess.pull_bounds_img((-1, -1, -1, -1, -1, -1))


def test_pull_bounds_seg_bad_inputs(session):
    """Tests that errors are raised when bad inputs are given to session.pull_bounds_seg.
    """
    sess, seg_id, v_id = session
    with pytest.raises(TypeError):
        sess.pull_bounds_seg(0)
    with pytest.raises(ValueError):
        sess.pull_bounds_seg((-1, -1, -1, -1, -1, -1))


def test_push_bad_inputs(session):
    """Tests that errors are raised when bad inputs are given to session.push.
    """
    sess, seg_id, v_id = session
    img = np.array([[[1, 1, 1], [2, 2, 2]]])
    bounds = (0, 0, 0, 10, 10, 10)
    with pytest.raises(TypeError):
        sess.push(0, bounds)
    with pytest.raises(ValueError):
        sess.push(np.array([[0, 0, 0], [0, 0, 0]]), bounds)
    with pytest.raises(TypeError):
        sess.push(img, 0)
    with pytest.raises(TypeError):
        sess.push(img, ("a", -1, -1, -1, -1, -1))
    with pytest.raises(ValueError):
        sess.push(img, (-1, -1, -1, -1, -1, -1))


###############
### pulling ###
###############


def test_set_url_segments(vars):
    """Tests setting a segmentation url .
    """
    url, url_segments, url_annotations, mip, seg_id, v_id = vars
    sess = NeuroglancerSession(url=url, mip=mip)
    sess.set_url_segments(url_segments)
    assert sess.url_segments == url_segments
    assert len(sess.cv_segments.scales) > 0


def test_get_segments(session):
    """Tests that getting segments returns a valid graph.
    """
    sess, seg_id, v_id = session
    G = sess.get_segments(seg_id)
    G_sub = sess.get_segments(seg_id, (0, 0, 0, 20, 20, 20))
    assert G != G_sub
    assert isinstance(G, nx.Graph) and isinstance(G_sub, nx.Graph)


def test_pull_voxel(session):
    """Tests that pulling a region at a voxel is valid.
    """
    sess, seg_id, v_id = session
    img, bounds, voxel = sess.pull_voxel(seg_id, v_id)
    print(img)
    assert len(img.shape) == 3
    assert img.shape == tuple(bounds.size())
    assert (
        voxel[0] <= img.shape[0]
        and voxel[1] <= img.shape[1]
        and voxel[2] <= img.shape[2]
    )


def test_pull_vertex_list(session):
    """Tests that pulling a vertex list returns valid regions.
    """
    sess, seg_id, v_id = session
    img, bounds, voxel = sess.pull_vertex_list(seg_id, [100, 101, 102, 103])
    assert len(img.shape) == 3
    assert img.shape == tuple(bounds.size())
    for vox in voxel:
        assert (
            vox[0] <= img.shape[0] and vox[1] <= img.shape[1] and vox[2] <= img.shape[2]
        )


def test_pull_vertex_list_voxel(session):
    """Tests that pulling a vertex list of a single voxel is the same as pulling that vertex voxel.
    """
    sess, seg_id, v_id = session
    img, bounds, voxel = sess.pull_voxel(seg_id, v_id)
    img2, bounds2, voxel2 = sess.pull_vertex_list(seg_id, [v_id], expand=False)
    assert img.shape == img2.shape
    assert (voxel == voxel2).all()
    assert bounds == bounds2
    assert (img == img2).all()


def test_pull_vertex_list_chunk(session):
    """Tests that pulling a vertex list of a single voxel is the same as pulling that chunk.
    """
    sess, seg_id, v_id = session
    img, bounds, voxel = sess.pull_chunk(seg_id, v_id)
    img2, bounds2, voxel2 = sess.pull_vertex_list(seg_id, [v_id], expand=True)
    assert img.shape == img2.shape
    assert (voxel == voxel2).all()
    assert bounds == bounds2
    assert (img == img2).all()


def test_pull_chunk(session):
    """Tests that pull_chunk returns a valid region.
    """
    sess, seg_id, v_id = session
    img, bounds, voxel = sess.pull_chunk(seg_id, v_id)
    assert len(img.shape) == 3
    assert img.shape == tuple(bounds.size())
    assert img.shape == tuple(sess.chunk_size)
    assert (
        voxel[0] <= img.shape[0]
        and voxel[1] <= img.shape[1]
        and voxel[2] <= img.shape[2]
    )


def test_pull_bounds_voxel(session):
    """Tests that pulling the volume from the region returned by pull_voxel is the same as the original pull_voxel volume.
    """
    sess, seg_id, v_id = session
    img, bounds, voxel = sess.pull_voxel(seg_id, v_id)
    print(bounds)
    img2 = sess.pull_bounds_img(bounds)
    assert (img == img2).all()


def test_pull_bounds_seg():
    """Tests pulling annotation layers.
    Currently we do not have annotation layers to test with.
    """


###############
### pushing ###
###############


def test_push(session):
    """Tests pushing an annotation volume.
    Currently we do not support annotation layers to push to.
    """


def test_pull_chunk_push_label(session):
    """Tests pulling a chunk of a volume, converting it to an annotation, and pushing the annotation.
    Currently we do not support annotation layers to push to.
    """

    def _img_to_labels(img, voxel, low=None, up=255):
        """Test method that converts volume to pixel-wise annotations.
        """
        img_T1 = sitk.GetImageFromArray(np.squeeze(img), isVector=False)
        img_T1_255 = sitk.Cast(sitk.RescaleIntensity(img_T1), sitk.sitkUInt8)
        seed = (int(voxel[2]), int(voxel[1]), int(voxel[0]))
        seg = sitk.Image(img_T1.GetSize(), sitk.sitkUInt8)
        seg.CopyInformation(img_T1)
        seg[seed] = 1
        seg = sitk.BinaryDilate(seg, 1)
        seg_con = sitk.ConnectedThreshold(
            img_T1_255, seedList=[seed], lower=int(np.round(low)), upper=up
        )
        vectorRadius = (1, 1, 1)
        kernel = sitk.sitkBall
        seg_clean = sitk.BinaryMorphologicalClosing(seg_con, vectorRadius, kernel)
        labels = sitk.GetArrayFromImage(seg_clean)
        return labels

    sess, seg_id, v_id = session
    img, bounds, voxel = sess.pull_chunk(2, 300)
    label = _img_to_labels(img, voxel, low=11)
    # sess.push(label, bounds)
    # label2 = sess.pull_bounds_seg(bounds)
    # assert (label == label2).all()
