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
import glob
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# save corpus and chroma_db directories as constants
CORPUS_DIR = os.path.join(os.path.dirname(__file__), "..", "corpus")
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "..", "chroma_db")

# this is the local embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def load_documents() -> list:
    """
    Read in the markdown docs from the corpus directory.

    Returns:
        a list of Document objects, each containing the text in each markdown file.
    """
    documents = []
    for filepath in glob.glob(os.path.join(CORPUS_DIR, "*.md")):
        #print(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        documents.append(Document(page_content=content, metadata={"source": filepath}))
    return documents

def chunk_documents(documents) -> list:
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

def main():
    pass

if __name__ == "__main__":
    print(f"Reading in docs from {os.path.abspath(CORPUS_DIR)} ...")
    documents = load_documents()
    print(f"  Loaded {len(documents)} documents")
    print(documents[0])

    print("Chunking ...")
    chunks = chunk_documents(documents)
    print(f"  Produced {len(chunks)} chunks")

    print(f"Embedding with {EMBEDDING_MODEL} and storing in Chroma ...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )

    print(f"\nDone. Vector store persisted to {os.path.abspath(CHROMA_DIR)}")

    main()