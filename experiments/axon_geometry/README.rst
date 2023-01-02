Publication
-----------

Athey, T. L., Teneggi, J., Vogelstein, J. T., Tward, D. J., Mueller, U., & Miller, M. I. (2021). Fitting splines to axonal arbors quantifies relationship between branch order and geometry. *Frontiers in Neuroinformatics*, 38.

DOI: https://doi.org/10.3389/fninf.2021.704627

Relevant directory
------------------

``brainlit/experiemnts/axon_geometry``

How to reproduce this experiment
--------------------------------

Before reproducing this experiment, make sure that:

- You have installed the ``brainlit`` package [`Documentation <https://brainlit.netlify.app/readme#installation>`_]. Currently, you need to install the package from source to execute these codes.
- You have installed PyTorch [`Documentation <https://pytorch.org/get-started/locally/>`_].

This experiment does *not* require a GPU (CUDA is not needed for PyTorch).

N.B. if you are using `conda <https://docs.conda.io/en/latest/>`_, make sure that both ``brainlit`` and PyTorch are installed within the same environment.

Now, follow these steps to reproduce the results of the experiment:

1. Download segments, which are stored in the publicly available S3 bucket `open-neurodata <https://registry.opendata.aws/open-neurodata/>`_

.. code-block::

    python scripts/download_segments.py


This script will prepare the experiment folder scaffolding

.. code-block::

    axon_geometry
    ├── data
    │   ├── brain1
    │   │   ├── segments_swc
    │   │   └── trace_data
    │   └── brain2        
    │       ├── segments_swc
    │       └── trace_data
    ├── figures
    │
    ... etc.


and download data from S3 (no credentials are required).

2. Compute and save trace analysis data

.. code-block::

    python scripts/generate_trace_data.py


3. Run any of the notebooks in the ``notebooks`` folder, which will save the results in the ``figures`` folder
