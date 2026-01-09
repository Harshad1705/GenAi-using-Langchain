from langchain_openai import OpenAIEmbeddings


embedding = OpenAIEmbeddings(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/text-embedding-3-large",
    dimensions=32
)

documents = [
    "Delhi is capital of India",
    "Paris is capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))