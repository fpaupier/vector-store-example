# <center> 📚 ChromaDB book recommender example </center>
<p align="center">
  <a href="https://pypi.org/project/chromadb"><img src="https://img.shields.io/badge/chromadb-vector%20store-blue" alt="ChromaDB Vector Store"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python->=3.9-brightgreen.svg" alt="Python Version"></a>
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
</p>

<br/>

<p align="center">
  <i>Visualizing ChromaDB in action: Managing vector embeddings for book recommendations.</i>
</p>

<br/>

# Vector store example

A minimal repo to explore the internals of Chroma DB through a book recommender system using sentence embeddings to
identify the closest relevant books from a user query.

# Setting up the project

We use Python >= 3.9, the vector store engine is [ChromaDB](https://docs.trychroma.com/docs/overview/getting-started) -
using the simple local on-disk storage option with sqlite backend. For the embeddings, we compute them locally
with [SBERT](https://sbert.net/docs/sentence_transformer/pretrained_models.html) models. Especially, we use `all-MiniLM-L6-v2` with 384 dimensions.

1. Create a python virtual environment

```bash
python3 -m venv .venv
```

2. Source your env

```bash
source .venv/bin/activate 
```

1. Install dependencies

```bash
pip install -r requirements.txt
```

# Source data

We use
the [Goodreads Recommendation Dataset](https://www.kaggle.com/datasets/rohitganeshkar/goodreads-book-recommendation-datasets) (~
50Mb)from Kaggle which is on Apache 2.0 licence. A small version of this dataset is versioned with this project to get
your started. 