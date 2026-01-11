from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

query = "rise of AI in India"

docs = retriever.invoke(query)

print(docs)