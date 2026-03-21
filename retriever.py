def get_relevant_docs(vectorstore, query):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)
    return docs