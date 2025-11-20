# Getting Ready for the Workshop

Please complete these steps ==**BEFORE ATTENDING**== the workshop  

⚠️ Downloading and installing packages and libraries using a shared workshop/conference wifi connection will be unreliable and slow.  So its highly recommended you complete this setup before the workshop.

## Prerequisites

1. **Laptop** with modern operating system (macOS, Linux, or Windows)
2. **Installed software**:
    - Git
    - Python 3.11+
    - [uv](https://docs.astral.sh/uv/getting-started/installation/)  - Fast Python package installer and resolver
3. **API Keys** for any services needed.

## Step-1: Get the code

```bash
git  clone    https://github.com/sujee/data-prep-kit-examples/
cd   data-prep-kit-examples
```

## Step-2: Install Python

**Python**

Either install [Anaconda](https://www.anaconda.com/download/)   or [mini forge](https://github.com/conda-forge/miniforge)

**Setup UV (highly recommended)**

We use [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager. Follow the setup instructions to install for your laptop.

## Step-3:  Setup Python Development Env

### 3.1 - Setup a python env for the workshop.

**Option 1: using `uv` - highly recommended**

```bash
uv sync
```

**Option 2: Using conda**

```bash
conda create -n dpk-workshop -y python=3.12
conda activate dpk-workshop
pip  install -r   requirements.txt
```

**Option 3: using python**

```bash
python  -m venv   .venv
source   .venv/bin/activate
pip   install -r   requirements.txt
```

### 3.2 - Setup Jupyter Kernel

This is handy to run the code within vscode

```bash
# create a ipykernel to run notebooks with vscode / jupyter / etc
source  .venv/bin/activate
python -m ipykernel install --user --name=dpk-example-1 --display-name "dpk-example-1"

jupyter kernelspec list
```

Choose this kernel 'dpk-example-1' within jupyter / vscode

## Step-4: Sign up for API Services


### Option 1: Nebius - Recommended

1. Sign up for free at [tokenfactory.nebius.com](https://tokenfactory.nebius.com/)
2. Create an API key  (copy it and save it locally)

The free account will give you a few API calls for free.  That is enough for this workshop.  

**Additional API credits will be distributed in the workshop.**



### Option 2: Replicate

Get a **free** account at [replicate](https://replicate.com/home)

Use this [invite](https://replicate.com/invites/a8717bfe-2f3d-4a52-88ed-1356231cdf03) to add some credit to your Replicate account!

The free account will give you a few API calls for free.  That is enough for this workshop.

Once you sign up, **create a token**


## Step-5: Create an .env file

Create an  `.env` file (note the dot in the front of the filename) in project root directory

Populate your API keys in `.env` file.  

**Option 1: If using Nebius**

```ini
NEBIUS_API_KEY="your api key goes here"
```

**Option 2: if using Replicate**

```ini
REPLICATE_API_TOKEN="your_replicate_token_goes_here"
```