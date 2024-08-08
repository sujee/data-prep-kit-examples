# Data Prep Kit Examples

## Introducing Data Prep Kit (DPK)

Whether you're performing RAG (Retrieval-Augmented Generation) or fine-tuning a model, a significant portion of your time will be dedicated to cleaning (de-duping, removing markups, etc.) and shaping the data.

[Data Prep Kit](https://github.com/IBM/data-prep-kit) can help you with wrangling data.  

Noteworthy  features:

- de-duping documents (exact dedupe and [fuzzy dedupe](https://github.com/IBM/data-prep-kit/tree/dev/transforms/universal/fdedup/ray#readme))
- can handle documents and code
- extract text from PDFs
- language detection (spoken languages and programming languages)
- malware detection
- [document quality checking](https://github.com/IBM/data-prep-kit/blob/dev/transforms/language/doc_quality/python/README.md)
- tokenizing and chunking
- generating embeddings


## Setup Python Dev Env

[Instructions for setting up dev environment](setup-python-dev-env.md)

## Milvus - Vector Database

[Milvus](https://milvus.io/) is a popular vector database that is **open source**

- [A quick start of Milvus](milvus/milvus_1_quick_start.ipynb) - Run an embedded milvus database
- [Vector search of movie plots using Milvus](milvus/milvus_2_movie_search.ipynb) - load movie data, index it with embeddings, upload the data into milvus and run semantic queries


## RAG Demos

See [RAG with data prep kit](./rag/README.md)

