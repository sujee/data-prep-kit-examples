# Running Ingest Pipeline

**code**

Here is the [pipeline code](rag_4_walmart_A_dataprepkit_process_2.ipynb)

Here is how to run it:

## Step-1: Setup Python Env

First make sure [setup local python dev env](../setup-python-dev-env.md)

## Step-2: Grab data prep kit repo

```bash
git   clone   https://github.com/IBM/data-prep-kit/

cd data-prep-kit

## Checkout the dev branch
git checkout   dev
```

## Step-3: Setup Python venv

This step will setup virtual env and install all required depdendencies.  It is crucial that we use the supported python versions (3.11)

```bash
## activate the python 3.11 you setup in Step-1
conda   activate  data-prep-kit-dev-1

python --version
# make sure it says 3.11

cd data-prep-kit/examples/notebooks/language

## Setup the virtual environment
## we only have to do this once

make clean
make venv
```

This command will take a few minutes to complete.

## Step-4:  Copy source code and input data

Copy notebook and data into the source tree

copy input pdf files 
- Create data directory : `data-prep-kit/examples/notebooks/language/input_data_walmart`
- copy data files from `data-prep-kit-examples/rag/data/walmart-reports-1/input` 
- into `data-prep-kit/examples/notebooks/language/input_data_walmart`

copy the notebook 
- from `data-prep-kit-examplesrag/rag_4_walmart_A_dataprepkit_process_2.ipynb`
- to `data-prep-kit/examples/notebooks/language/`


## Step-5: Run the code

```bash
## make sure you are in project dir
cd data-prep-kit/examples/notebooks/language/

## Start Jupyter
make jupyter
```


This will start Jupyter server.  Open file `rag_4_walmart_A_dataprepkit_process_2.ipynb ` and run it.

This file will look for input data in `input_data_walmart`

After a few minutes we will have output data stored in `output_walmart`

## Step-6: Copy the output back to the repo

copy the generated output files:

- create directory  `data-prep-kit-examplesrag/data/walmart-reports-1/output_final`
- copy the generated parquet files from `data-prep-kit/examples/notebooks/language/output_walmart`
- to `data-prep-kit-examplesrag/data/walmart-reports-1/output_final`

## Step-7: Next Steps

We will import the produced outupt into vector database

[Continue...](./README.md#featured-example-walmart-financial-documents-search)