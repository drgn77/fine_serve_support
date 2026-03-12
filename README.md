# FineServe Support Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit)
![Claude](https://img.shields.io/badge/Claude-Sonnet_4.6-8A2BE2?logo=anthropic)
![LangChain](https://img.shields.io/badge/LangChain-FAISS-green)

An internal RAG-powered chatbot that lets customer service agents instantly query FineServe's knowledge base and get accurate, source-backed answers.

---
## Live Demo
🔗 **[Live Demo](https://fineservesupport.streamlit.app/)**

## Problem Statement

Customer service agents waste time digging through scattered policy documents to answer client questions. Manual lookups are slow, inconsistent, and error-prone — especially under high call volume.

---

## Solution

FineServe Support Assistant indexes internal documents into a FAISS vector store and uses Claude to generate precise, context-grounded answers. Agents ask in plain English and get cited responses in seconds.

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM | Anthropic Claude (claude-sonnet-4-6) |
| Embeddings | OpenAI text-embedding-3-small |
| Vector Store | FAISS (via LangChain) |
| Document Loading | LangChain Community |
| Config | python-dotenv |

---

## Architecture

```
User Question
     │
     ▼
[ Streamlit UI ]
     │
     ▼
[ FAISS Vector Store ] ── similarity_search(k=4) ──► [ Relevant Chunks ]
                                                              │
                                                             ▼
                                              [ Build context prompt ]
                                                              │
                                                             ▼
                                              [ Claude Sonnet API ]
                                                              │
                                                             ▼
                                              [ Answer + Sources ]
     │◄────────────────────────────────────────────────────────
     ▼
[ Display in chat UI ]
```

---

## Setup & Installation

### Prerequisites

- Python 3.11+
- OpenAI API key
- Anthropic API key

### 1. Clone & create virtual environment

```bash
git clone <repo-url>
cd FineServe
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
EMBEDDING_MODEL=text-embedding-3-small
MODEL_NAME=claude-sonnet-4-20250514
FAISS_PATH=vector_data
DATA_PATH=data
```

### 4. Ingest documents

Place your `.md` policy files in the `data/` directory, then run:

```bash
python ingest.py
```

This builds the FAISS vector index in `vector_data/`.

### 5. Run the app

```bash
streamlit run app.py
```

---

## Project Structure

```
FineServe/
├── app.py               # Streamlit UI
├── ingest.py            # Document ingestion & vector store builder
├── requirements.txt
├── .env                 # API keys (not committed)
├── data/                # Source documents (.md)
│   ├── client-onboarding.md
│   ├── complaint-procedure.md
│   ├── data-privacy-gdpr.md
│   ├── faq-clients.md
│   ├── internal-faq-agents.md
│   ├── late-payment-policy.md
│   └── product-policy.md
├── src/
│   └── rag.py           # RAG logic: retrieval + Claude inference
└── vector_data/         # FAISS index (generated, not committed)
```

