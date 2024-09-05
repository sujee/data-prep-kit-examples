# Profiling Code

PDF2Parquet step seems very slow.

it is processing at the rate of 1 page / sec.  So for 3 documents with 300 pages total, it is taking 300 seconds = 5 minutes!

Here is how I am profiling it

## Env Setup

```bash
conda create -n dpk-perf-1 -y python=3.11

# activate the new conda environment
conda activate dpk-perf-1

pip install --upgrade  -r requirements.txt

```

## Profiling Pure Python Code

First simple code with pdf2parquet transform : [test_pdf2pq_py.py](test_pdf2pq_py.py)

Run it under profiler

`py-spy record -o test_pdf2pq_py.svg -- python test_pdf2pq_py.py`

Open SVG file in Chrome browser:   [test_pdf2pq_py.svg](test_pdf2pq_py.svg)

To generate **speedscope** format

`py-spy record -o test_pdf2pq_py.speed -f speedscope -- python test_pdf2pq_py.py`

Open the .speed file at : https://www.speedscope.app/

## Profiling RAY code

code: [test_pdf2pq_ray.py](test_pdf2pq_ray.py)

`py-spy record -o test_pdf2pq_ray.speed -f speedscope -- python test_pdf2pq_ray.py`


Experimenting with the collofing configurations

- RAY_NUM_CPUs_PER_WORKER = 1
- RAY_MEMORY_PER_WORKER = 2 * GB
- RAY_RUNTIME_NUM_WORKERS = 1

| NUM_WORKERS | NUM_CPUs | MEMORY | time taken         | Notes          |
|-------------|----------|--------|--------------------|----------------|
| 1           | 1        | 2 GB   | 900 secs / 15 mins | 1 core @ 100%  |
| 2           | 1        | 2 GB   | 600 secs / 11 mins | 2 cores @ 100% |
| 3           | 1        | 2 GB   | 360 secs / 6 mins  | 3 cores @ 100% |
| 3           | 2        | 2 GB   | 240 secs / 4 mins  | 6 cores @ 100% |