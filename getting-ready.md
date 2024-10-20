# Getting Ready for the Workshop

## Step-1: Basic dev tools

Please have the following tools
- git
- a good editor (VSCode ..etc)

## Step-2: Install Anaconda Python or Equivalent

Either install [Anaconda](https://www.anaconda.com/download/)   or [mini forge](https://github.com/conda-forge/miniforge)

## Step-3:  Setup a Local Python Development Env

Follow [setup-python-dev-env.md](setup-python-dev-env.md) to setup your local python dev environment.

## Step-4: Sign up for Replicate

Get a **free** account at [replicate](https://replicate.com/home)

💰 Use this [invite](https://replicate.com/invites/a8717bfe-2f3d-4a52-88ed-1356231cdf03) to add some credit to your Replicate account!

(Just to give you an idea of pricing, Replicate charges 5c / 1M input tokens, 25c / 1M output token for model meta/meta-llama-3-8b-instruct)

The free account will give you a few API calls for free.  That is enough for this workshop.

Once you sign up, **create a token**


## Step-5: Create an .env file

Create an  `.env` file (note the dot in the front of the filename) in project root directory

Populate your API keys in `.env` file.  Here is an example.

```
REPLICATE_API_TOKEN=your_replicate_token_goes_here
```