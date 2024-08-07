# Setup a Local Python Dev Environment

## Step-1: Anaconda Python environment

You can install Anaconda by following the [guide here](https://www.anaconda.com/download/).

## Step-2: Create a custom environment

We will create an environment for this workshop with all the required libraries installed.

```bash
# need python 3.11 for torch libraries
conda create -n data-prep-kit-1 -y python=3.11

# activate the new conda environment
conda activate data-prep-kit-1
# make sure env is swithced to data-prep-kit-1
```

install all needed packages

```bash
pip install -r requirements.txt
```

## Step-3: Setup a Jupyter / Ipython Kernel

To use Jupyter notebooks, we will define a kernel specific to this environment

```bash
## create a new jupyter kernel (same name as the conda env name)
ipython kernel install --user --name=data-prep-kit-1

# see installed kernels
jupyter kernelspec list
```

When running Jupyter notebooks, be sure to select this kernel