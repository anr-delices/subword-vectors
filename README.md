# subword embeddings trained on arXiv

This repository contains the code to build subword embeddings from the [arXiv dataset of 1.7M+ scholarly papers](https://www.kaggle.com/Cornell-University/arxiv).

## Prerequisites

[Download the arXiv dataset], decompress `archive.zip` and place the file `arxiv-metadata-oai-snapshot.json` into the `data/` directory.

Install required Python modules:
```bash
pip3 install -r requirements.txt
```

Follow the [instructions](https://github.com/google/sentencepiece#build-and-install-sentencepiece-command-line-tools-from-c-source) to build and install SentencePiece command line tools from C++ source.

Follow the [instructions](https://github.com/stanfordnlp/GloVe) to build and install GloVe.

## Train subword embeddings from the arXiv dataset

We follow the idea of pre-trained subword embbeddings from [(Heinzerling and Strube, 2018)](https://www.aclweb.org/anthology/L18-1473.pdf).

```bash
# Extract the textual content from the arXiv dataset
# this creates a one-sentence-per-line raw corpus file
# 12,807,583 lines
python3 src/extract.py data/arxiv-metadata-oai-snapshot.json \
        data/arxiv-metadata-oai-snapshot.txt

# Train a sentencePiece model from the corpus file
spm_train --input=data/arxiv-metadata-oai-snapshot.txt \
          --model_prefix=data/arxiv-metadata-oai-snapshot \
          --vocab_size=10000

# Encode the corpus file using the sentencePiece model
spm_encode --model=data/arxiv-metadata-oai-snapshot \
           --output_format=piece \
           < data/arxiv-metadata-oai-snapshot.txt \
           > data/arxiv-metadata-oai-snapshot.piece

# Train the subword GloVe vectors

```
