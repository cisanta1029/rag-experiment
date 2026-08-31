"""
First step of the RAG pipeline.
To be ran any time the corpus is changed (edits/new files)

1. Load every markdown document in the corpus directory
2. Iterate over each document, and split paragraphs into chunks (with some overlap)
3. Embed each chunk with a sentence-transformers model.
4. Store the text chunks and their associated vectors into a Chroma vector database.

To use:
    python src/ingest.py
"""

import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# save corpus and chroma_db directories as constants
CORPUS_DIR = os.path.join(os.path.dirname(__file__), "..", "corpus")
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "..", "chroma_db")

# this is the local embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def load_documents():
    """
    Read in the markdown docs from the corpus directory
    """
    loader = DirectoryLoader(
        CORPUS_DIR,
        glob="*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    return loader.load()

def chunk_documents(documents):
    """
    Splits documents into chunks.
    ~ 1 paragraph per chunk, with some overlap before and after for context
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return splitter.split_documents(documents)