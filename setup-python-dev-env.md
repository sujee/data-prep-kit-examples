# Setup a Local Python Dev Environment

## Step-1: Anaconda Python environment

You can install Anaconda by following the [guide here](https://www.anaconda.com/download/).

## Step-2: Create a custom environment

We will create an environment for this workshop with all the required libraries installed.

**Make sure python version is 3.11**

```bash
conda create -n data-prep-kit-1 -y python=3.11
```

Activate the new conda environment

```bash
conda activate data-prep-kit-1
```

Make sure env is swithced to data-prep-kit-1

Be sure in the project directory

```bash
git   clone  https://github.com/sujee/data-prep-kit-examples
```

```bash
cd  data-prep-kit-examples
```

install all needed packages

```bash
pip install -r requirements.txt
```


## Start-3: Start Jupyter

```bash
jupyter lab
```

## Troubleshooting

## If libraries are not loading:  Setup a Jupyter / Ipython Kernel

To use Jupyter notebooks, we will define a kernel specific to this environment

Create a new jupyter kernel (same name as the conda env name)

```bash
ipython kernel install --user --name=data-prep-kit-1
```

SWee installed kernels

```bash
jupyter kernelspec list
```

When running Jupyter notebooks, be sure to select this kernel