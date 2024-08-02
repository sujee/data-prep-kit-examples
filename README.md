# Data Prep Kit Examples

Examples of using IBM data prep kit

## Setup Python Env

[setup guide](./setup/setup-python-dev-env.md)

## Milvus

[Milvus](https://milvus.io/) is a popular vector database.

- [A quick start of Milvus](milvus/milvus_1_quick_start.ipynb) - Run an embedded milvus database
- [Vector search of movie plots using Milvus](milvus/milvus_2_movie_search.ipynb) - load movie data, index it with embeddings, upload the data into milvus and run semantic queries


## RAG

| Documents          | Framework   | Vector DB | Embedding Model             | LLM                 | Code                                                      | Notes                |
|--------------------|-------------|-----------|-----------------------------|---------------------|-----------------------------------------------------------|----------------------|
| Granite Docs (pdf) | llama-index | Milvus    | BAAI/bge-small-en-v1.5 (OS) | Llama 3 @ Replicate | [code](rag/rag_2_llamaindex_milvus_llama_replicate.ipynb) | Need REPLICATE TOKEN |
| Milvus FAQ (md)    | None        | Milvus    | BAAI/bge-small-en-v1.5 (OS) | Llama 3 @ Replicate | [code](rag/rag_3_milvus_llama_replicate.ipynb)            | Need REPLICATE TOKEN |
|                    |             |           |                             |                     |                                                           |                      |