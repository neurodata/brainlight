import os
from brainlit.BrainLine.apply_ilastik import ApplyIlastik_LargeImage
from pathlib import Path

""" 
Inputs
"""
# DOUBLE CHECK:
# -dir_base
# data_dir and results_dir ARE CLEAR
# threshold IS CORRECT
brain = "028L"

antibody_layer = "Ch_647"
background_layer = "Ch_561"
endogenous_layer = "Ch_488"

threshold = 0.8  # threshold to use for ilastik
brainline_exp_dir = Path(os.getcwd()) / Path(__file__).parents[1]
data_dir = (
    brainline_exp_dir / "data" / "brainr_temp"
)  # "/data/tathey1/matt_wright/brainr_temp/"  # directory to store temporary subvolumes for segmentation
results_dir = (
    brainline_exp_dir / "data" / "brainr_results"
)  # directory to store coordinates of soma detections
data_file = brainline_exp_dir / "data" / "soma_data.json"

# Ilastik will run in "headless mode", and the following paths are needed to do so:
ilastik_path = "/home/user/Documents/ilastik-1.4.0-Linux/run_ilastik.sh"
ilastik_project = (
    brainline_exp_dir / "data" / "validation-and-models" / "soma" / "matt_soma_rabies_pix_3ch.ilp"
)


min_coords = [
    -1,
    -1,
    -1,
]  # max coords or -1 if you want to process everything along that dimension
max_coords = [
    6100,
    9100,
    4096,
]  # max coords or -1 if you want to process everything along that dimension
ncpu = 2  # 16  # number of cores to use for detection
chunk_size = [1024, 1024, 1024]  # [256, 256, 300]

""" 
Detect Somas
"""

layer_names = [antibody_layer, background_layer, endogenous_layer]
alli = ApplyIlastik_LargeImage(
    ilastik_path=ilastik_path,
    ilastik_project=ilastik_project,
    ncpu=ncpu,
    data_file=data_file,
    results_dir=results_dir,
)
# alli.apply_ilastik_parallel(
#     brain_id=brain,
#     layer_names=layer_names,
#     threshold=threshold,
#     data_dir=data_dir,
#     chunk_size=chunk_size,
#     min_coords=min_coords,
#     max_coords=max_coords,
# )
alli.collect_soma_results(brain_id=brain)
