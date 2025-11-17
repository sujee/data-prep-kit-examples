# RAG with Data Prep Kit

This folder has examples of RAG applications with data prep kit (DPK).

## Step-1: Setup Python Environment

[setup-python-dev-env.md](../setup-python-dev-env.md)

Make sure Jupyter is running after this step.  We will use this Jupyter instance to run the notebooks in next steps.

## RAG Workflow

Here is the overall work flow.  For details see [RAG-explained](./RAG-explained.md)

![](media/rag-overview-2.png)

## Step-2: Configuration

Inspect common configuration in [my_config.py](my_config.py)

Here you can set 

- input data
- embedding models 
- ..etc

Also here is an overview of [datasets](datasets.md) we have.

## Step-3: Process Input Documents (RAG stage 1, 2 & 3)

This code uses DPK to 

- Extract text from PDFs (RAG stage-1)
- Performs cleanups (de-dupes & other cleanups) (RAG stage-1)

Here is the code: 

- Python version: [1_dpk_process_python.ipynb](1_dpk_process_python.ipynb)
- Ray version: [1_dpk_process_ray.ipynb](1_dpk_process_ray.ipynb)


## Step-4: Load data into vector database  (RAG stage 4)

Our vector database is [Milvus](https://milvus.io/)

Run the code: [2_save_to_vector_db.ipynb](2_save_to_vector_db.ipynb)

Be sure to [shutdown the notebook](#tips-close-the-notebook-kernels-to-release-the-dblock) before proceeding to the next step



## Step-5: Query the documents using LLM (RAG steps 5, 6, 7, 8 & 9)

We will use **Llama** as our LLM running on services like [Nebius Token Factory](https://tokenfactory.nebius.com/)  or   [Replicate](https://replicate.com/).


### 5.1 - Create an `.env` file

Create an `.env` file (notice the dot in the file name in this directory with content like this

**If using Nebius**

Get an API key from [Nebius Token Factory](https://tokenfactory.nebius.com/)

```ini
LLM_MODEL = 'nebius/openai/gpt-oss-120b'
NEBIUS_API_KEY = 'your api key'
```


**If using replicate**

You can get API key from [Replicate](https://replicate.com/)



```ini
LLM_MODEL = 'ibm-granite/granite-3.3-8b-instruct'
REPLICATE_API_TOKEN=xyz
```

### 5.2 - Run the query code

Code: [3_query_LLM.ipynb](3_query_LLM.ipynb)



## Step 6: Illama Index

For comparision, we can use [Llama-index](https://docs.llamaindex.ai/) framework to process PDFs and query

### Step 6.1 - Process documents and save the index into vector DB

Code: [llamaindex_1_process.ipynb](llamaindex_1_process.ipynb)

Be sure to [shutdown the notebook](#tips-close-the-notebook-kernels-to-release-the-dblock) before proceeding to the next step


### Step 6.2 - Query documents with LLM

code: [llamaindex_2_query.ipynb](llamaindex_2_query.ipynb)


## Tips: Close the notebook kernels, to release the db.lock

When using embedded database, the program maintains a lock on the database file.  If the lock is active, other notebooks may not be able to access the same database.

Here is how to close kernels:

- In **vscode**:  **Restart the kernel**. This will end the current kernel session and release the db.lock
- In **Jupyter** : Go to  `File --> Close and shutdown notebook`.  This will end the current kernel session and release the db.lock