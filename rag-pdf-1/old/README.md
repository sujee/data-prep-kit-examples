# RAG with Data Prep Kit

This folder has examples of RAG applications with data prep kit (DPK).

These examples are designed to run on a local python dev environment.  See [setup-python-dev.md](../setup-python-dev-env.md) for instructions.

**Jump to:**

- [Featured RAG Example - Processing and querying Walmart PDFs](#featured-example-walmart-financial-documents-search)
- [RAG process explained](./RAG-explained.md)
- [RAG examples](#more-rag-examples)
- [Handy Utils](#handy-utilities)


## RAG Workflow

Here is the overall work flow.  For details see [RAG-explained](./RAG-explained.md)

![](../media/rag-overview-2.png)


## Featured Example: Walmart financial documents search

### Option-1: Using Data Prep Kit

**Workflow** : 
`PDFs --> Process with Data Prep Kit --> Store in Milvus --> query with Llama LLM`

**Stack**

- Processing framework: **data prep kit (DPK)**
- Vector store: **Milvus**
- LLM: **llama**
- Query framework: **Replicate**

**Input Data** 

Walmart's annual reports in PDF format: [data/walmart-reports-1/input/](data/walmart-reports-1/input/)

**Data Ingest Pipeline**

- Step-1: Cleanup and Preprocess. Text is extracted from PDF. And we perform dedupe and other cleanups (**DPK**)
- Step-2: split document into chunks (**DPK**)
- Step-3: vectorize chunks using embedding models(**DPK**)
- Step-4: Saving the final output into vector database

**Output data**: 

The output from DPK is processed parquet files.  [data/walmart-reports-1/output_final/](data/walmart-reports-1/output_final/)

These files will be imported in vector database

**De-Duping in action!**

In the [input folder](data/walmart-reports-1/input/) we have 3 PDFs with one being a duplicate file.  During the ingest process, DPK has performed de-dupe! The  [output](data/walmart-reports-1/output_final/) only has 2 files 👍


**Code:**

- Steps 1, 2 & 3: [Cleanup and process documents, break them into chunks and calculate embeddings](rag_4_walmart_A_dataprepkit_process.md)
    - This step is optional.  We have saved the output from this step.  So you can continue to next steps
- Step 4: [Save the generated output to vector database](./rag_4_walmart_B_load_data_into_milvus.ipynb)
- Steps 5, 6, 7: [Perform vector search on the data](./rag_4_walmart_C_vector_search.ipynb)
- Steps 5, 6, 7, 8 & 9: [Query the documents using LLM](./rag_4_walmart_D_dataprepkit_query_llama_replicate.ipynb)

### Option-2: Using llama-index

And for comparison, here is the [code](rag_4_walmart_E_llamaindex_milvus_llama_replicate.ipynb) that uses llama-index to process PDFs and query

## More RAG Examples

### Ex-1: Granite PDFs

* Input data:  [Granite model document (PDF)](./data/granite-docs/input/)
* Processing framework: **DPK**  [Processing code](./rag_1_granitedocs_A_dataprepkit_process_data.ipynb)
    - Optional: we have saved the output from this step, so you can continue to next step
* Vector store: **Milvus**  [Save to DB code](./rag_1_granitedocs_B_load_data_into_milvus.ipynb)
* Query framework: **Replicate** [query code](./rag_1_granitedocs_C_query_llama_replicate.ipynb)
* LLM: **llama**

### Ex-2: Granite PDFs

We can compare the results of using llama-index and data-prep-kit

* Input data:  [Granite model document (PDF)](./data/granite-docs/input/)
* Processing framework: **llama-index**
* Vector store: **milvus**
* Query framework: **llama-index and replicate**
* LLM: **llama**
* [code](./rag_2_granitedocs_llamaindex_llama_replicate.ipynb)

### Ex-3: Querying Markdown files

* Input data:  [Milvus FAQ documents (md)](./data/milvus_docs/en/faq/)
* Processing framework: **None, using  vanilla python**
* Vector store: **milvus**
* Query framework: **replicate**
* LLM: **llama**
* [code](./rag_3_mdfiles_query_llama_replicate.ipynb)

### Ex-4: Walmart PDF documents 

see [featured example](#featured-example-walmart-financial-documents-search)

## Handy Utilities

[Inspect parquet files](./utils_inspect_parquet.ipynb) - Handy for seeing the contents of parquet files

[Vector search](./vector_search.ipynb) - do a quick vector search of any collection in Milvus DB

