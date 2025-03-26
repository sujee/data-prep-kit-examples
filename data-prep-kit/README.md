# Data Prep Kit Examples

Some examples of [Data Prep Kit](https://github.com/IBM/data-prep-kit) -  A  powerful, open-source tool kit for preparing data for LLM applications.

## Getting Started

The code can be run locally or Google Colab.

For Google Colab, no setup instructions required.

Local development environment setup instructions are here.

```bash
# setup a new python dev env - we will use anaconda here
conda create -n dpk-intro-1 -y python=3.11
conda activate dpk-intro-1

# requiremnets.txt is found in this current dir
pip install  -r requirements.txt

# start jupyter and run the notebooks with this jupyter
jupyter lab
```

## Examples

### 1 - Processing PDF files

Process PDFs using DPK / Docling

**This example has now been officially integrated into the Data Prep Kit repository. [here](https://github.com/data-prep-kit/data-prep-kit/tree/dev/examples/notebooks/pdf-processing-1)**

[dpk_1_intro.ipynb](dpk_1_intro.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sujee/data-prep-kit-examples/blob/main/data-prep-kit/dpk_1_intro.ipynb)

### 2 - Document Quality

Detect and filter out SPAM  and low quality content

[doc_quality_1.ipynb](doc_quality_1.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sujee/data-prep-kit-examples/blob/main/data-prep-kit/doc_quality_1.ipynb)

### 3 - PII (Personally Identifiable Information) Redactor

Detect and redact sensitive information like 

- Credit card numbers
- emails
- address
- social security numbers

[pii_1.ipynb](pii_1.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sujee/data-prep-kit-examples/blob/main/data-prep-kit/pii_1.ipynb)


### 4 - HAP (Hate Abuse Profanity) Detector

Detect HAP speech in documents

[hap_1.ipynb](hap_1.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sujee/data-prep-kit-examples/blob/main/data-prep-kit/hap_1.ipynb)
