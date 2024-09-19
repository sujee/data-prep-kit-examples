import os 


## Configuration
class MyConfig:
    pass 

MY_CONFIG = MyConfig ()

### -------- configure input / output ---------------

# MY_CONFIG.INPUT_DATA_DIR = "../data/solar-system"
# MY_CONFIG.OUTPUT_FOLDER = "output-solar-system"

MY_CONFIG.INPUT_DATA_DIR = "../data/fomc"
MY_CONFIG.OUTPUT_FOLDER = "output-fomc"

# MY_CONFIG.INPUT_DATA_DIR = "../data/papers"
# MY_CONFIG.OUTPUT_FOLDER = "output-papers"

# MY_CONFIG.INPUT_DATA_DIR = "../data/10k"
# MY_CONFIG.OUTPUT_FOLDER = "output-10k"

# MY_CONFIG.INPUT_DATA_DIR = "../data/walmart-reports-1"
# MY_CONFIG.OUTPUT_FOLDER = "output-walmart-reports-1"

# MY_CONFIG.INPUT_DATA_DIR = "../data/resumes"
# MY_CONFIG.OUTPUT_FOLDER = "output-resumes"

MY_CONFIG.OUTPUT_FOLDER_FINAL = os.path.join(MY_CONFIG.OUTPUT_FOLDER , "output_final")
### -------------------------------

### Milvus config
MY_CONFIG.DB_URI = './rag_1_dpk.db'  # For embedded instance
MY_CONFIG.COLLECTION_NAME = 'docs'

## Embedding model
MY_CONFIG.EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
MY_CONFIG.EMBEDDING_LENGTH = 384

## LLM Model
MY_CONFIG.LLM_MODEL = "meta/meta-llama-3-8b-instruct"



## RAY CONFIGURATION
num_cpus_available =  os.cpu_count()
# print (num_cpus_available)
# MY_CONFIG.RAY_NUM_CPUS = num_cpus_available // 2  ## use half the available cores for processing
MY_CONFIG.RAY_NUM_CPUS =  1
# print (MY_CONFIG.RAY_NUM_CPUS)
MY_CONFIG.RAY_MEMORY_GB = 2  # GB
# MY_CONFIG.RAY_RUNTIME_WORKERS = num_cpus_available // 3
MY_CONFIG.RAY_RUNTIME_WORKERS = 2