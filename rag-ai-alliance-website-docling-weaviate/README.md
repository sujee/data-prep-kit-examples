# Chat With AI Alliance Website


## 🔗  [bit.ly/4hlaeFZ](https://bit.ly/4hlaeFZ)

<img src="qrcode_rag-docling-weaviate.png" width="400px">

This example will show how to crawl a website, process HTML files and query them using RAG.

We will utilize Docling for this.

Here is the process:

`website ---(crawler) --> HTML files --- (html2pq)--> markdown content ---(llama-index)--> save to vector db (weaviate) ---(query)---> LLM`

## Step-1: Setup Python Env

```bash
conda create -n rag-website-1  python=3.11

conda activate rag-website-1
```

Install modules

```bash
pip install -r requirements.txt 
```


## Step-2: Configuration

Inspect configuration here: [my_config.py](my_config.py)

Here you can set:

- site to crawl
- how many files to download and crawl depth
- embedding model
- LLM to use

## Step-3: Crawl a website

This step will crawl a site and download HTML files in `input` directory

[1_crawl_site.ipynb](1_crawl_site.ipynb)

For large websites, it is recommended to run the python script as follows

```bash
python     1_crawl_site.py
```


## Step-4: Process HTML files

We will process downloaded HTML files and extract the text as markdown.  The output will be saved in the`output/2-markdown` directory in markdown format

[2_process_html.ipynb](2_process_html.ipynb)

## Step-5: Save data into DB

We will save the extracted text (markdown) into a vector database (Milvus)

[3_save_to_vector_db.ipynb](3_save_to_vector_db.ipynb)

## Step-6: Query documents

### 6.1 - Setup `.env` file with API Token

For this step, we will be using Replicate API service.  We need a Replicate API token for this step.

Follow these steps:

- Get a **free** account at [replicate](https://replicate.com/home)
- Use this [invite](https://replicate.com/invites/a8717bfe-2f3d-4a52-88ed-1356231cdf03) to add some credit  💰  to your Replicate account!
- Create an API token on Replicate dashboard

Once you have an API token, add it to the project like this:

- Copy the file `env.sample.txt` into `.env`  (note the dot in the beginning of the filename)
- Add your token to `REPLICATE_API_TOKEN` in the .env file.

### 6.2 - Query

Query documents using LLM

[4_query.ipynb](4_query.ipynb)
