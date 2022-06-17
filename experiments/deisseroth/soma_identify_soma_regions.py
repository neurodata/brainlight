import numpy as np
from cloudvolume import CloudVolume
from tqdm import tqdm
import pickle
from os import listdir
from os.path import isfile, join
from cloudreg.scripts.transform_points import NGLink
from cloudreg.scripts.visualization import create_viz_link_from_json

viz_link = "https://viz.neurodata.io/?json_url=https://json.neurodata.io/v1?NGStateID=my8twEEDBrE0DQ"
viz_link = NGLink(viz_link.split("json_url=")[-1])
ngl_json = viz_link._json

atlas_layer = None
for layer in ngl_json['layers']:
    if layer['name'] == 'atlas_to_target':
        atlas_layer = layer['source']
if atlas_layer is None:
    raise ValueError(f"No atlas_to_target layer at viz link: {viz_link}")

brain = atlas_layer.split("/")[-2]
div_factor = [8, 8, 1]

atlas_vol = CloudVolume(
    atlas_layer,
    parallel=1,
    mip=0,
    fill_missing=True,
)
print(f"size: {atlas_vol.shape} ")

somas = "/data/tathey1/matt_wright/brainr_results/"
outpath = (
    "/data/tathey1/matt_wright/brainr_results/quantification_dict_" + brain + ".pickle"
)

coords = []
coords_target_space = []
if somas[:-4] == ".txt":
    file1 = open(somas, "r")
    lines = file1.readlines()

    for line in tqdm(lines, desc="parsing coordinates"):
        if line != "\n":
            line = " ".join(line.split())
            elements = line.split(",")
            coord = [elements[0][1:], elements[1], elements[2][:-1]]
            coords_target_space.append(coord)
            coord = [
                int(round(float(e.strip()) / f)) for e, f in zip(coord, div_factor)
            ]
            coords.append(coord)
else:  # directory of text files
    onlyfiles = [join(somas, f) for f in listdir(somas) if isfile(join(somas, f))]
    for file in tqdm(onlyfiles, desc="reading files"):
        file1 = open(file, "r")
        lines = file1.readlines()

        for line in tqdm(lines, desc="parsing coordinates", leave=False):
            if line != "\n":
                line = " ".join(line.split())
                elements = line.split(",")
                coord = [elements[0][1:], elements[1], elements[2][:-1]]

                coords_target_space.append([float(e.strip()) for e in coord])
                coord = [
                    int(round(float(e.strip()) / f)) for e, f in zip(coord, div_factor)
                ]
                coords.append(coord)

ngl_json['layers'].append(
    {
        "type": "annotation",
        "points": coords_target_space,
        "name": "transformed_points"
    }   
)
viz_link = create_viz_link_from_json(ngl_json, neuroglancer_link="https://viz.neurodata.io/?json_url=")
print(f"Viz link with detections: {viz_link}")

print(f"{len(coords)} somas detected, first is: {coords[0]}")

dict = {}
for coord in tqdm(coords, desc="identifynig rois"):
    roi = int(np.squeeze(atlas_vol[coord[0], coord[1], coord[2]]))
    if roi not in dict.keys():
        dict[roi] = 1
    else:
        dict[roi] = dict[roi] + 1

print(dict)
with open(outpath, "wb") as handle:
    pickle.dump(dict, handle)
