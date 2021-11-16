from brainlit.algorithms.generate_fragments import state_generation

sg = state_generation("/data/tathey1/mouselight/250.zarr", "/home/tathey1/ilastik-1.3.3post3-Linux/run_ilastik.sh", "/data/tathey1/mouselight/octopus_exp.ilp", chunk_size=[500,500,250], parallel=12)#, prob_path="/data/tathey1/mouselight/1_probs.zarr")
sg.predict("/data/tathey1/mouselight/data_bin/")
sg.compute_frags()