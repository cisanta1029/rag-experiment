# RAG Experimentation Knowledge Base

A retrieval-augmented generation (RAG) system, built with LangChain and LangGraph, that answers questions about experimentation and causal inference methodology (A/B testing, RCTs, difference-in-differences, and related concepts) grounded in a real document corpus rather than the model's own memory.

Unlike a straight-line RAG chain, this pipeline grades its own retrieval before answering: if the retrieved context doesn't look sufficient, it rewrites the question and tries again. That control flow is what makes LangGraph the right tool here rather than LangChain alone.

## Why this project

I created this project to build hands-on fluency with the modern LLM application stack (chunking, embeddings, vector search, and agentic control flow).

The corpus is built around experimentation and causal inference concepts rather than an arbitrary dataset. That was deliberate: my day-to-day work involves designing nested RCTs with BAU holdout groups and using difference-in-differences to isolate incremental causal lift, so the subject matter of the knowledge base and the instincts behind evaluating whether a retrieval system is actually working come from the same place. Choosing a topic I can independently verify the answers to also makes it much easier to tell whether the pipeline is retrieving well or just producing plausible-sounding text.

### Phase 1: Indexing (`src/ingest.py`)

```
corpus/*.md  ->  chunk  ->  embed  ->  store in Chroma
```

Markdown documents are read from `corpus/`, split into overlapping chunks, embedded with a local sentence-transformers model, and stored in a Chroma vector database. This is only to be run once to build the chunks' vector database, and agaih whenever the corpus changes.

### Phase 2: Query (`src/graph.py`)

```
        +-------------+
        |  retrieve   |<------------+
        +------+------+             |
               |                    |
        +------v-------+            |
        | grade_context|            |
        +------+-------+            |
               |                    |
     sufficient |  insufficient     |
        +------v------+      +------+-------+
        |  generate   |      | reformulate  |
        +------+------+      +--------------+
               |
              END
```

A LangGraph state machine with four nodes:

- **retrieve** — embeds the current question and runs approximate nearest neighbor ("ANN") search against Chroma, returning the top-k chunks (code currently set to k=3)
- **grade_context** — asks the LLM whether the retrieved chunks are sufficient to answer the question, and logs the attempt
- **reformulate** — rewrites the question when grading fails, then routes back to retrieve
- **generate** — builds the final "using only this context, answer the question" prompt and returns the answer

Routing between `grade_context` and the two downstream nodes is handled by a conditional edge (`route_after_grade`), capped at three attempts so the loop can't run indefinitely (preserving token usage in the process). This pattern is often called corrective or self-correcting RAG.

## Design decisions

**Embeddings run locally.** `sentence-transformers/all-MiniLM-L6-v2` runs on the local machine rather than through a paid embeddings API. Only the three LLM-calling nodes hit an external API, which keeps iteration on the ingestion side fast and free.

**Chroma as the vector store.** Chosen for zero-infrastructure local development — no server to stand up, and appropriate for a corpus of this size. A production system operating on millions of vectors would want a managed vector database instead. Chroma stores document text and metadata in SQLite alongside a persisted HNSW index for the ANN search itself.

**Corpus sourced from Wikipedia.** A curated list of articles were pulled directly from the MediaWiki API using a script. Articles were saved as an .md file; each with a source URL and CC BY-SA attribution header, keeping the corpus legally clean for this repo.

**State design: overwrite vs. accumulate.** `current_question`, `chunks`, and `grade` are overwritten on each pass, since only the latest attempt matters for generation. `attempt_log` accumulates one entry per attempt, giving a record of every retrieve/grade cycle without needing a separate tracing tool. `original_question` is deliberately held fixed and separate from `current_question`, so reformulation never loses sight of what was actually asked.

**Migrated off `langchain-community`.** That package was sunset in 2026 and its repository archived. Embeddings and the vector store moved to their dedicated packages (`langchain-huggingface`, `langchain-chroma`). Document loading was replaced with plain Python — a `glob` over the corpus directory constructing `Document` objects directly — following the maintainers' own stated position that simple functionality is better written as application code than pulled in as a shared dependency.

**Using `.text` rather than `.content`.** Provider response shapes are not identical: Anthropic returns a plain string on `.content`, while Gemini can return a list of content blocks, which breaks string methods. This initially got a custom normalization helper before I found LangChain's built-in `.text` property on `BaseMessage`, which handles both shapes. This served as a lesson that a standardized interface doesn't always mean identical behavior underneath.

**Provider is swappable.** `LLM_PROVIDER` selects between Anthropic and Google. The three LLM-calling nodes are unaware of which one is active; they call `_get_llm()` and invoke whatever comes back. This is a key benefit of LangChain's standardized model interface.

## Setup

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env              # then add your API key(s)

python src/fetch_corpus.py        # pull the Wikipedia corpus
python src/ingest.py              # chunk, embed, and store
python src/query.py "Why would you use difference-in-differences instead of a simple before/after comparison?"
```

`query.py` prints the attempt log (showing each retrieve/grade cycle and the question used), a preview of the chunks retrieved on the final attempt, and the generated answer.

## Example

```
$ python src/query.py "what is selection bias?"

Question: what is selection bias?

Running question through RAG pipeline...

==============================
ATTEMPT LOG
==============================
  Attempt 1: grade=sufficient
    Question used: what is selection bias?
==============================
RETRIEVED CHUNKS (final attempt)
==============================
  [1] # Selection bias  > Source: [https://en.wikipedia.org/wiki/Selection_bias]...
  [2] == Related issues == Selection bias is closely related to:...
  [3] == Mitigation == In the general case, selection biases cannot be overcome
      with statistical analysis of existing data alone, though Heckman
      correction may be used in special cases...
==============================
ANSWER
==============================
Based on the context, selection bias is the bias introduced by the selection
of individuals, groups, or data for analysis in such a way that the
association between exposure and outcome among those selected differs from
the association among those eligible.

It typically occurs when researchers condition on a factor that is influenced
both by the exposure and the outcome (or their causes), which creates a false
association between them.

Selection bias encompasses several forms, including differential
loss-to-follow-up, incidence-prevalence bias, volunteer bias, healthy-worker
bias, and nonresponse bias.
```

Two things worth noticing in this run.

First, the correction loop did not fire. Grading passed on the first attempt, so `route_after_grade` sent execution straight to `generate` and `reformulate` never ran. The attempt log confirms this. A second or third entry would indicate retrieval failed initially and the question was rewritten.

Second, the answer synthesizes across all three retrieved chunks rather than restating the closest match. The definition comes from the first chunk, the conditioning mechanism from the second, and the enumerated forms of selection bias are drawn from a different section of the article than the definition. Retrieval's job is to surface candidate context; the connecting is done at generation time.

Note: `ingest.py` appends to the existing collection rather than replacing it, so re-running it without clearing `chroma_db/` first will store duplicate copies of every chunk — which surfaces as retrieval returning the same text multiple times. Delete the directory before re-ingesting. Making this idempotent is on the list below.

## Next steps

### Evaluation harness

The main direction for this project. Right now, changing anything (chunk size, top-k, correction loop on or off, etc.) can only be judged by running a few questions and eyeballing the answers. This project needs a more quantifiable approach.

The harness has three pieces:

**A gold set.** Thirty to fifty questions about the corpus, each paired with a known-correct answer and the chunk or chunks that should have been retrieved. A fixed benchmark everything gets measured against.

**Metrics split by layer.** Retrieval metrics (recall@k, MRR) ask whether the right context was fetched. Generation metrics (groundedness, correctness) ask whether the answer was good given what was fetched. Keeping these separate is what makes a failure diagnosable rather than just visible.

**Variant comparison as an experiment.** Each configuration is an arm, run against the same gold set, with results compared as distributions rather than point estimates. Thirty questions is a small sample, and a few points of difference in correctness may well be noise. This is the same discipline behind comparing a treatment against a holdout, applied to pipeline configurations instead of customer segments.

**Retrieval scores** feed directly into this. `similarity_search_with_score` returns distance alongside each chunk, which separates two failure modes that currently look identical: an answer that was poor because retrieval surfaced the wrong context, versus one that was poor despite good context. Having retrieval scores also enables us to have quick thresholds. For example, if the closest chunk is far enough away, decline to answer rather than paying for an LLM grading call to reach the same conclusion.

### Smaller fixes

**Token usage instrumentation.** Capture `usage_metadata` from each LLM call and accumulate input, output, and total counts into the state, tagged by node and attempt. A failed grading pass re-pays the full input cost of the context, so this makes the cost of the correction loop measurable rather than assumed. Token counts can serve as KPIs for pipeline optimization.

**Structured output for grading.** The grading step currently asks for a one-word answer and parses the returned string. Binding a schema via `with_structured_output()` would constrain the response to a fixed enum, removing both the parsing logic and the formatting instruction from the prompt.

**Reformulation history.** `reformulate_node` currently sees only the original question and the most recent attempt, so with a higher attempt cap it could cycle back toward a phrasing already tried. The full history already exists in `attempt_log` and just needs to be passed into the prompt.

**Idempotent ingestion.** Clear the collection or use stable document IDs so re-running `ingest.py` replaces rather than duplicates.
