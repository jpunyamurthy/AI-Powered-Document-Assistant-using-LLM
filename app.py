import streamlit as st
import os
from pdf_loader import load_pdf
from vector_store import create_vector_store
from retriever import get_relevant_docs
from prompt import build_prompt
from llm import get_llm, generate_response

st.set_page_config(page_title="AI Document Assistant", layout="wide")

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("📄 AI Assistant")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs", type=["pdf"], accept_multiple_files=True
)

st.sidebar.markdown("---")
st.sidebar.write("Chat with your documents using AI")

# ---------------- SESSION STATE ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# ---------------- TITLE ---------------- #
st.title("🤖 AI Document Assistant")

# ---------------- FILE PROCESSING ---------------- #
if uploaded_files:
    all_docs = []

    for file in uploaded_files:
        with open(file.name, "wb") as f:
            f.write(file.read())

        docs = load_pdf(file.name)
        all_docs.extend(docs)

        os.remove(file.name)

    st.session_state.vectorstore = create_vector_store(all_docs)
    st.success("✅ Documents processed successfully!")

# ---------------- DISPLAY CHAT ---------------- #
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ---------------- #
query = st.chat_input("Ask something about your documents...")

if query:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    if st.session_state.vectorstore is None:
        st.warning("⚠️ Please upload documents first.")
    else:
        with st.spinner("Thinking..."):
            docs = get_relevant_docs(st.session_state.vectorstore, query)

            # 🔥 Use last 5 messages (memory optimization)
            chat_history = st.session_state.messages[-5:]

            prompt = build_prompt(query, docs, chat_history)

            llm = get_llm()
            response = generate_response(llm, prompt)

        # Add assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        with st.chat_message("assistant"):
            st.markdown(response)

        # 🔥 Show sources
        with st.expander("📚 Source Context"):
            for doc in docs:
                st.write(doc.page_content[:300])