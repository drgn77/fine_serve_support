import streamlit as st
import os

from src.rag import get_answer, load_embeddings, load_vector_store

st.set_page_config(
    page_title="FineServe Support Assistant",
    page_icon="💼",
    layout="centered"
)

st.title("💼 FineServe Support Assistant")
st.markdown("Ask questions about FineServe policies, procedures, and client services. The assistant will search the internal knowledge base and respond using verified sources.")


def init_resources():
    if "embeddings" not in st.session_state:
        st.session_state.embeddings = load_embeddings()
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = load_vector_store(st.session_state.embeddings)


init_resources()

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Example Questions")
    for q in [
        "What is the client onboarding process?",
        "How are late payments handled?",
        "What are the data privacy rights under GDPR?",
        "What products and services does FineServe offer?",
        "How can a client file a complaint?"
    ]:
        if st.button(q):
            st.session_state.example_question = q
    st.divider()
    if st.button("🧹 Clear chat"):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and message.get("sources"):
            with st.expander("Sources"):
                for src in message["sources"]:
                    st.markdown(f"- {os.path.basename(src)}")

question = st.chat_input("Ask a question about FineServe policies or procedures...")

if "example_question" in st.session_state:
    question = st.session_state.example_question
    del st.session_state.example_question

if question:
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching FineServe knowledge base..."):
            result = get_answer(
                query=question,
                vector_store=st.session_state.vector_store
            )

        answer = result.get("answer", "No answer generated.")
        sources = result.get("sources", [])

        st.markdown(answer)

        if sources:
            with st.expander("Sources"):
                for src in sources:
                    st.markdown(f"- {os.path.basename(src)}")

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources
        })