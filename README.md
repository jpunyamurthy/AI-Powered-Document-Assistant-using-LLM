# 🚀 AI-Powered Document Assistant

## 📌 Overview
This project is an AI-powered document assistant that can understand and answer questions from uploaded documents using Large Language Models (LLMs).

It uses a Retrieval-Augmented Generation (RAG) approach to provide context-aware and accurate responses.

---

## 💡 Features
- Upload and process documents (PDF/Text)
- Semantic search using embeddings
- Context-aware answers using LLMs
- Interactive chatbot interface
- Real-time responses using Streamlit

---

## 🛠 Tech Stack
- Python  
- LangChain  
- LLM APIs (OpenAI / Groq)  
- Streamlit  
- Vector Embeddings (FAISS / Chroma)

---

## ⚙️ How It Works
1. Documents are uploaded and split into smaller chunks  
2. Chunks are converted into embeddings  
3. Stored in a vector database  
4. User query is matched with relevant chunks  
5. LLM generates final answer based on context  

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-document-assistant.git
cd ai-document-assistant

Install dependencies
pip install -r requirements.txt

Create a .env file and add:
OPENAI_API_KEY=your_key_here

Run the app:
streamlit run app.py



<img width="1906" height="913" alt="AI Impact summit" src="https://github.com/user-attachments/assets/f7f163d0-920c-432d-bf12-8b64ef757861" />

