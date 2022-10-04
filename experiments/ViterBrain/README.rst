Manuscript
----------

Athey, T. L., Tward, D. J., Mueller, U., & Miller, M. I. (2021). Hidden Markov Modeling for Maximum Likelihood Neuron Reconstruction. *arXiv preprint arXiv*:2106.02701.


How to use ViterBrain
---------------------

* First, make sure that you have installed the ``brainlit`` package [`Documentation <https://brainlit.netlify.app/readme#installation>`_]. 

* Second, uncompress the data ``brainlit/experiments/ViterBrain/data/example.zip``. ``brainlit/experiemnts/ViterBrain/data/sample.zip`` can also be used.

* Make sure you are using Python3.9

* Then, you can run some of the tutorial notebooks in the ``notebooks`` folder:
    * ``ViterBrain.ipynb`` - shows a programmatic example of the pipeline, based on zarr inputs.
    * ``fig3-voxels.ipynb`` - generates Figure 3 from the paper.
    * ``fig7-results.ipynb`` - generates Figure 7 from the paper.
    * other notebooks can be useful for referemce, they were used in generating results in the paper.

* The files in the ``scripts`` folder also can be useful:
    * ``napari_gui.py`` - shows the GUI prototype.
        * click on colored fragment to select, red arrow will identify orientation.
        * o-key or `switch states` button to switch orientation of selected fragment.
        * click on another colored fragment (and hit o-key if necessary to switch orientation).
        * click on the labels layer in the left hand pane, then click somewhere on the image (not on a fragment)
        * t-key or `trace` button to trace between fragments.
        * c-key or `clear selected states` button to clear the selected fragments.
        * q-key or `clear all` button to clear all annotations.
        * n-key or `next color` button to change colors (3 total colors).
    * other scripts are for reference for benchmarking the timing of the pipeline.
