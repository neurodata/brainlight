import h5py
import numpy as np
from brainlit.BrainLine.apply_ilastik import (
    plot_results,
    examine_threshold,
    ApplyIlastik,
    ApplyIlastik_LargeImage,
    downsample_mask,
)
import os
import shutil
import pytest
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import date


soma_data_file = (
    Path(os.path.abspath(__file__)).parents[3]
    / "docs"
    / "notebooks"
    / "pipelines"
    / "BrainLine"
    / "soma_data.json"
)


@pytest.fixture(scope="session")
def axon_data_dir(tmp_path_factory):
    data_dir = tmp_path_factory.mktemp("data")
    brain_dir = data_dir / "braintest"
    brain_dir.mkdir()
    val_dir = brain_dir / "val"
    val_dir.mkdir()

    labels = np.ones((2, 10, 10, 10), dtype=np.uint16)
    labels[0, 0, 0, :] = 2
    labels_path = val_dir / "subvol-image_3channel_Labels.h5"
    with h5py.File(str(labels_path), "w") as f:
        dset = f.create_dataset("exported_data", data=labels)

    im_probs = np.zeros((2, 10, 10, 10))
    im_probs[0, 0, 0, :5] = 0.9
    path = val_dir / "subvol_Probabilities.h5"
    with h5py.File(path, "w") as f:
        f.create_dataset("exported_data", data=im_probs)

    im = np.zeros((3, 10, 10, 10))
    im[0, 0, 0, :5] = 0.9
    path = val_dir / "subvol.h5"
    with h5py.File(path, "w") as f:
        f.create_dataset("image_3channel", data=im)

    return data_dir


# ApplyIlastik


def test_processsubvols_none(axon_data_dir):
    val_dir = axon_data_dir / "brainnonexistant"
    val_dir.mkdir()
    val_dir = val_dir / "val"
    val_dir.mkdir()

    apl = ApplyIlastik(
        ilastik_path="test",
        project_path="test",
        brains_path=axon_data_dir,
        brains=["nonexistant"],
    )

    with pytest.raises(ValueError):
        apl.process_subvols()

    # brainr1
    val_dir = axon_data_dir / "brainr1"
    val_dir.mkdir()
    val_dir = val_dir / "val"
    val_dir.mkdir()

    apl = ApplyIlastik(
        ilastik_path="test",
        project_path="test",
        brains_path=axon_data_dir,
        brains=["8557"],
    )

    with pytest.raises(ValueError):
        apl.process_subvols()

    # brainr2
    val_dir = axon_data_dir / "brainr2"
    val_dir.mkdir()
    val_dir = val_dir / "val"
    val_dir.mkdir()

    apl = ApplyIlastik(
        ilastik_path="test",
        project_path="test",
        brains_path=axon_data_dir,
        brains=["8555"],
    )

    with pytest.raises(ValueError):
        apl.process_subvols()


def test_move_results(axon_data_dir):
    apl = ApplyIlastik(
        ilastik_path="test",
        project_path="test",
        brains_path=axon_data_dir,
        brains=["test"],
    )

    apl.move_results()

    # Check that file was moved
    newdir = apl.brains_path / f"braintest/val/results{date.today()}"
    moved_files = os.listdir(newdir)
    assert len(moved_files) == 1

    # Move files back
    for moved_file in moved_files:
        shutil.move(newdir / moved_file, apl.brains_path / "braintest/val" / moved_file)


# Other methods


def test_plot_results_axon(axon_data_dir):
    data_dir_str = str(axon_data_dir)

    test_max_fscore, test_best_threshold = plot_results(
        data_dir=data_dir_str,
        brain_ids=["test"],
        object_type="axon",
        positive_channel=0,
        show_plot=False,
    )

    true_prec = 1
    true_rec = 0.5
    true_max_fscore = 2 * true_prec * true_rec / (true_prec + true_rec)

    assert test_best_threshold < 0.9
    assert true_max_fscore == test_max_fscore


def test_examine_threshold_axon(axon_data_dir):
    data_dir_str = str(axon_data_dir)
    examine_threshold(
        data_dir=data_dir_str,
        brain_id="test",
        threshold=0.5,
        object_type="axon",
        positive_channel=0,
        show_plot=False,
    )


@pytest.fixture(scope="session")
def soma_data_dir(tmp_path_factory):
    data_dir = tmp_path_factory.mktemp("data")
    brain_dir = data_dir / "braintest"
    brain_dir.mkdir()
    val_dir = brain_dir / "val"
    val_dir.mkdir()

    im_probs = np.zeros((2, 10, 10, 10))
    im = np.zeros((3, 10, 10, 10))
    im_probs[1, :, :, :7] = 0.9
    for fname in ["subvol1_pos", "subvol2_pos", "subvol3_neg"]:
        fname_im = fname + ".h5"
        im_path = val_dir / fname_im
        with h5py.File(str(im_path), "w") as f:
            f.create_dataset("image_3channel", data=im)

        fname_prob = fname + "_Probabilities.h5"
        path = val_dir / fname_prob
        with h5py.File(path, "w") as f:
            f.create_dataset("exported_data", data=im_probs)

    return data_dir


def test_plot_results_soma(soma_data_dir):
    data_dir_str = str(soma_data_dir)
    test_max_fscore, test_best_threshold = plot_results(
        data_dir=data_dir_str,
        brain_ids=["test"],
        object_type="soma",
        positive_channel=1,
        show_plot=False,
        doubles=["subvol2_pos.h5"],
    )
    plt.close("all")

    true_prec = 2 / 3
    true_rec = 1
    true_max_fscore = 2 * true_prec * true_rec / (true_prec + true_rec)

    assert test_best_threshold < 0.9
    assert true_max_fscore == test_max_fscore


def test_examine_threshold_soma(soma_data_dir):
    data_dir_str = str(soma_data_dir)
    examine_threshold(
        data_dir=data_dir_str,
        brain_id="test",
        threshold=0.5,
        object_type="soma",
        positive_channel=1,
        doubles=["subvol2_pos.h5"],
        show_plot=False,
    )


def test_downsample_mask_somafile():
    with pytest.raises(ValueError) as e_info:
        downsample_mask(brain="placeholder", data_file=soma_data_file)
    assert e_info.value.args[0] == f"Entered non-axon data file"


# ApplyIlastik_LargeImage


def test_ApplyIlastik_LargeImage(soma_data_dir):
    # Axon data
    data_file = (
        Path(os.path.abspath(__file__)).parents[3]
        / "docs"
        / "notebooks"
        / "pipelines"
        / "BrainLine"
        / "axon_data.json"
    )
    aili = ApplyIlastik_LargeImage(
        ilastik_path="", ilastik_project="", ncpu=1, data_file=data_file
    )
    aili.collect_axon_results(brain_id="pytest", ng_layer_name="average_10um")
    # Sample data is there but file path in data json is specific to thomastathey

    # Soma data
    data_dir = soma_data_dir
    aili = ApplyIlastik_LargeImage(
        ilastik_path="",
        ilastik_project="",
        ncpu=1,
        data_file=soma_data_file,
        results_dir=str(data_dir),
    )

    somas_path = aili.results_dir / "somas.txt"
    print(somas_path)
    with open(somas_path, "w") as f:
        f.write("[-1, 1, 1]\n")
        f.write("[1, 1, 1]\n")
        f.write("[2, 1, 1]\n")

    aili.collect_soma_results(brain_id="pytest_download")
