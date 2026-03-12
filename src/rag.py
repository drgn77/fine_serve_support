import anthropic
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from typing import Any, Dict
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAISS_PATH = os.path.join(BASE_DIR, os.getenv("FAISS_PATH", "vector_data"))
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
MODEL_NAME = os.getenv("MODEL_NAME", "claude-sonnet-4-6")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = """You are a FinServe Client Support Assistant — an internal tool 
used by customer service agents to quickly find accurate answers from FinServe's 
knowledge base. 

Rules:
- Answer ONLY based on the provided context.
- If the context does not contain the answer, say so clearly.
- Be precise — include specific numbers, deadlines, and fees when available.
- Keep answers concise and professional.
- Reference the relevant policy or document when possible."""


def get_answer(query: str, vector_store: FAISS) -> Dict[str, Any]:
    docs = vector_store.similarity_search(query, k=4)

    context = "\n\n---\n\n".join([doc.page_content for doc in docs])

    sources = []
    for doc in docs:
        source = doc.metadata.get("source")
        if source and source not in sources:
            sources.append(source)

    query_with_context = (
        f"CONTEXT:\n{context}\n\n"
        f"QUESTION:\n{query}\n\n"
        "Answer based solely on the context above. "
        "If the context does not contain the answer, respond with: "
        "'I don't have enough information to answer this based on the available documentation.'"
    )

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=800,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": query_with_context
            }
        ]
    )

    return {
        "answer": response.content[0].text,
        "sources": sources
    }


def load_embeddings():
    return OpenAIEmbeddings(model=EMBEDDING_MODEL)


def load_vector_store(embeddings):
    return FAISS.load_local(
        FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )