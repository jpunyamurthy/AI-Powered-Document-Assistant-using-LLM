def build_prompt(query, context_docs, chat_history):
    context = "\n\n".join([doc.page_content for doc in context_docs])

    history = ""
    for msg in chat_history:
        role = msg["role"]
        content = msg["content"]
        history += f"{role}: {content}\n"

    prompt = f"""
You are an AI document assistant.

Use the conversation history and context to answer the question.

Chat History:
{history}

Context:
{context}

Question:
{query}

Give a clear, structured, and helpful answer.
"""

    return prompt