import os 

## Configuration
class MyConfig:
    pass 

MY_CONFIG = MyConfig ()

## Crawl settings
MY_CONFIG.CRAWL_URL_BASE = 'https://thealliance.ai/'
MY_CONFIG.CRAWL_MAX_DOWNLOADS = 500
MY_CONFIG.CRAWL_MAX_DEPTH = 5
MY_CONFIG.CRAWL_MIME_TYPE = 'text/html'

## Directories
MY_CONFIG.INPUT_DIR = "input"
MY_CONFIG.OUTPUT_DIR = "output"
### -------------------------------


# MY_CONFIG.EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
# MY_CONFIG.EMBEDDING_LENGTH = 384

# MY_CONFIG.EMBEDDING_MODEL = 'BAAI/bge-small-en-v1.5'
# MY_CONFIG.EMBEDDING_LENGTH = 384

MY_CONFIG.EMBEDDING_MODEL = 'ibm-granite/granite-embedding-30m-english'
MY_CONFIG.EMBEDDING_LENGTH = 384

## Chunking
MY_CONFIG.CHUNK_SIZE = 512
MY_CONFIG.CHUNK_OVERLAP = 20


### Milvus config
MY_CONFIG.DB_URI = './rag_website.db'  # For embedded instance
MY_CONFIG.COLLECTION_NAME = 'pages'


## LLM Model
# MY_CONFIG.LLM_MODEL = "meta/meta-llama-3-8b-instruct"
# MY_CONFIG.LLM_MODEL = "meta/meta-llama-3-70b-instruct"
MY_CONFIG.LLM_MODEL = "ibm-granite/granite-3.1-2b-instruct"
# MY_CONFIG.LLM_MODEL = "ibm-granite/granite-3.1-8b-instruct"
