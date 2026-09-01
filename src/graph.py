import os
from typing import TypedDict, List
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

# save chroma_db directory and embedding model as constant 
# (consider environment variable between this and ingest.py)
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "..", "chroma_db")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

MAX_ATTEMPTS = 3
TOP_K = 3

# constant defining which LLM provider to use. One of the benefits of 
# LangChain is that it allows us to swap providers in a modular way, 
# without needing to rewrite the pipeline. Outputs are standardized
LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "anthropic")  # "anthropic" or "google"

ANTHROPIC_MODEL = "claude-sonnet-5"
GEMINI_MODEL = "gemini-2.5-flash"

class GraphState(TypedDict):
    """
    The state object that travels between nodes.
    Inheriting from the TypedDict class

    most variables will be overwritten, while attempt_log will accumulate
    """
    original_question: str
    current_question: str       # overwritten on each reformulation
    chunks: List[str]           # overwritten each retrieval
    grade: str                  # overwritten each grading pass
    attempts: int               # attempt counter
    attempt_log: List[dict]     # accumulates (appends)
    response: str

def _get_vectordb():
    """
    returns the Chroma object, connecting to the stored vector db (from ingest),
    as well as knowing which embedding model to use going forward.
    """
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)

def _get_llm():
    """
    returns LLM acccording to value provided by LLM_PROVIDER
    """
    if LLM_PROVIDER == "google":
        return ChatGoogleGenerativeAI(model=GEMINI_MODEL, temperature=0)
    return ChatAnthropic(model=ANTHROPIC_MODEL, temperature=0)

"""
def _extract_text(response) -> str:
    #Normalize an LLM response's .content into a plain string. May deprecate
    content = response.content
    if isinstance(content, list):
        parts = []
        for part in content:
            if isinstance(part, str):
                parts.append(part)
            elif isinstance(part, dict) and "text" in part:
                parts.append(part["text"])
        return "".join(parts)
    return content
"""

def retrieve_node(state: GraphState) -> GraphState:
    """
    Question is embedded and ANN search is executed (similarity_search)

    Returns the state object, updated with the top-k chunks with vectors 
    closest to the query vectors.
    """
    vectordb = _get_vectordb()
    docs = vectordb.similarity_search(state["question"], k=TOP_K)
    chunks = [d.page_content for d in docs]
    return {**state, "chunks": chunks}


""" #use this if we force a structured output from the llm (v2)
from pydantic import BaseModel, Field
from typing import Literal

class ContextGrade(BaseModel):
    #Grade for whether retrieved context is sufficient to answer the question.
    grade: Literal["sufficient", "insufficient"] = Field(
        description="Whether the retrieved context contains enough information to answer the question"
    )

def grade_node(state: GraphState) -> GraphState:
    llm = _get_llm()
    structured_llm = llm.with_structured_output(ContextGrade)
    
    context = "\n\n---\n\n".join(state["chunks"])
    prompt = (
        "Determine whether the retrieved context below is sufficient to "
        "answer the question.\n\n"
        f"Question: {state['original_question']}\n\n"
        f"Retrieved context:\n{context}"
    )
    
    result = structured_llm.invoke(prompt)
    grade = result.grade   # already "sufficient" or "insufficient" -- no parsing
"""


def grade_node(state: GraphState) -> GraphState:
    llm = _get_llm()
    context = "\n\n---\n\n".join(state["chunks"])
    prompt = (
        "You are grading whether retrieved context is sufficient to answer "
        "a question. Respond with exactly one word: 'sufficient' or "
        "'insufficient'.\n\n"
        f"Question: {state['original_question']}\n\n"
        f"Retrieved context:\n{context}\n\n"
        "Grade:"
    )

    #result = _extract_text(llm.invoke(prompt)).strip().lower()
    result = llm.invoke(prompt).text.strip().lower()

    # check to see if the result contains the word sufficient or insufficient. 
    # There may be a way to force the models to give only responses of 'sufficient' or 'insufficient'. 
    # If so, we can deprecate this if/elif/else statement.

    if "insufficient" in result:
        grade = "insufficient"
    elif "sufficient" in result:
        grade = "sufficient"
    else:
        grade = "insufficient"  # unclear response -> fail safe, retry

    attempts = state["attempts"] + 1
    log_entry = {
        "attempt": attempts,
        "question": state["current_question"],
        "grade": grade,
    }
    return {
        **state,
        "grade": grade,
        "attempts": attempts,
        "attempt_log": state["attempt_log"] + [log_entry],
    }