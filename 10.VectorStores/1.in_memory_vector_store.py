from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from dotenv import load_dotenv

load_dotenv()

# Create LangChain documents for IPL players
doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )
docs = [doc1, doc2, doc3, doc4, doc5]

embeddings = embedding_function=OpenAIEmbeddings(
        base_url="https://openrouter.ai/api/v1",
        model="openai/text-embedding-3-large",
)

vector_store = InMemoryVectorStore(embedding=embeddings)

# add documents
vector_store.add_documents(docs)


# search documents
results = vector_store.similarity_search("best IPL captain", k=2)
print(results)
print()

# search with similarity score
score = vector_store.similarity_search_with_score(
    query='Who among these are a bowler?',
    k=2
)
print(score[0][0].page_content)
print(score[0][1])
print()


# Remove document
vector_store.delete(
    filter=lambda doc: "MS Dhoni" in doc.page_content
)
