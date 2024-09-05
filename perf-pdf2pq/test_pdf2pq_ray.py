import ast
import os
import sys
import shutil

# Main repo root
from utils import rootdir

from data_processing_ray.runtime.ray import RayTransformLauncher
from data_processing.runtime.pure_python import PythonTransformLauncher
from data_processing.utils import ParamsUtils


from pdf2parquet_transform import (
    pdf2parquet_contents_type_cli_param,
    pdf2parquet_contents_types,
)
from pdf2parquet_transform_python import Pdf2ParquetPythonTransformConfiguration
from pdf2parquet_transform_ray import Pdf2ParquetRayTransformConfiguration

from data_processing.utils import GB, ParamsUtils


# create parameters
input_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "input_data", "walmart-reports-1"))
output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "output3"))

shutil.rmtree(output_folder, ignore_errors=True)
shutil.os.makedirs(output_folder, exist_ok=True)

### RAY Config
RAY_NUM_CPUs_PER_WORKER = 1
RAY_MEMORY_PER_WORKER = 2 * GB
RAY_RUNTIME_NUM_WORKERS = 1
# RAY_NUM_GPUS = 0.5


# create parameters
local_conf = {
    "input_folder": input_folder,
    "output_folder": output_folder,
}
worker_options = {"num_cpus" : RAY_NUM_CPUs_PER_WORKER, 
                #   "num_gpus" : RAY_NUM_GPUS, 
                  "memory": RAY_MEMORY_PER_WORKER}
code_location = {"github": "github", "commit_hash": "12345", "path": "path"}
ingest_config = {
    pdf2parquet_contents_type_cli_param: pdf2parquet_contents_types.JSON,
}

params = {
    # where to run
    "run_locally": True,
    # Data access. Only required parameters are specified
    "data_local_config": ParamsUtils.convert_to_ast(local_conf),
    "data_files_to_use": ast.literal_eval("['.pdf']"),
    # orchestrator
    "runtime_worker_options": ParamsUtils.convert_to_ast(worker_options),
    "runtime_num_workers": RAY_RUNTIME_NUM_WORKERS,
    "runtime_pipeline_id": "pipeline_id",
    "runtime_job_id": "job_id",
    "runtime_code_location": ParamsUtils.convert_to_ast(code_location),
}


sys.argv = ParamsUtils.dict_to_req(d=(params | ingest_config))
# create launcher
launcher = RayTransformLauncher(Pdf2ParquetRayTransformConfiguration())
# launch
launcher.launch()