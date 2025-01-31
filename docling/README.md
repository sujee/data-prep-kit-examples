# Introducing Docling

Some examples of [Docling](https://github.com/DS4SD/docling) -  A modern, powerful, open-source document processor that handles various formats (PDFs, DOCX, HTML, PPTX).   

## Getting Started

The code can be run locally or Google Colab.

For Google Colab, no setup instructions required.

Local development environment setup instructions are here.

```bash
# setup a new python dev env - we will use anaconda here
conda create -n docling-intro-1 -y python=3.11
conda activate docling-intro-1

# requiremnets.txt is found in this current dir
pip install  -r requirements.txt

# start jupyter and run the notebooks with this jupyter
jupyter lab
```

## Docling Quick Start

Use CLI

```bash

## PDF --> markdown
!docling   --output output --to md  input.pdf

## PDF --> text
# !docling   --output output --to text  input.pdf

## PDF --> json
!docling   --output output --to json  input.pdf

## PDF --> html
!docling   --output output --to html  input.pdf
```

## Intro 

Walks through docling's parsing features

[docling_1_intro.ipynb](docling_1_intro.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sujee/data-prep-kit-examples/blob/main/docling/docling_1_intro.ipynb)

