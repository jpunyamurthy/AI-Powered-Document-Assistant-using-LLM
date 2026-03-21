from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY")
    )
    return llm


def generate_response(llm, prompt):
    response = llm.invoke(prompt)
    return response.content