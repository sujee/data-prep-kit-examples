import ast
import os
import sys
import shutil

from data_processing.runtime.pure_python import PythonTransformLauncher
from data_processing.utils import ParamsUtils
from pdf2parquet_transform_python import Pdf2ParquetPythonTransformConfiguration


# create parameters
input_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',  'data', 'walmart-reports-1', 'input'))
output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))

shutil.rmtree(output_folder, ignore_errors=True)
shutil.os.makedirs(output_folder, exist_ok=True)

local_conf = {
    "input_folder": input_folder,
    "output_folder": output_folder,
}
code_location = {"github": "github", "commit_hash": "12345", "path": "path"}
params = {
    # Data access. Only required parameters are specified
    "data_local_config": ParamsUtils.convert_to_ast(local_conf),
    "data_files_to_use": ast.literal_eval("['.pdf',]"),
    # execution info
    "runtime_pipeline_id": "pipeline_id",
    "runtime_job_id": "job_id",
    "runtime_code_location": ParamsUtils.convert_to_ast(code_location),
    # pdf2parquet params
    # "pdf2parquet_do_table_structure": False,
    "pdf2parquet_contents_type": "application/json",
    # "pdf2parquet_contents_type": "text/markdown",
}
if __name__ == "__main__":
    # Set the simulated command line args
    sys.argv = ParamsUtils.dict_to_req(d=params)
    # create launcher
    launcher = PythonTransformLauncher(runtime_config=Pdf2ParquetPythonTransformConfiguration())
    # Launch the ray actor(s) to process the input
    launcher.launch()

    # input("Press Enter to terminate...")  # wait till we can gather metrics