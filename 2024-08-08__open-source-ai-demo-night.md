# Notes for Open Source AI Demo Night (2024-08-08)

## Event Details

[Event information](https://lu.ma/oss-ai)  
Date: Thursday, August 08, 2024  
Where: Shack15, San Francisco, CA


## Featured Example: RAG (Retrieval-Augmented Generation)

Here is an example of **end to end** RAG application.

### RAG Pipeline

![](media/rag-overview-2.png)

### Input Data



The data is [here](rag/data/walmart-reports-1/input/).  

#### De-Duping

We have introduced a duplicate document in our [input](rag/data/walmart-reports-1/input/).  

Don't worry, DPK will perform de-dupe for us.  You can see in the [output](rag/data/walmart-reports-1/output_final/) 👍

