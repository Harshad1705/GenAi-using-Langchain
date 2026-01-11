from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat
from dotenv import load_dotenv

load_dotenv()

print("*"*120)

### Indexing - document loader 

document_loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=YtHdaXuOAks", 
    add_video_info=False,
    language=["en", "hi"]
    # created chunks of 30 seconds 
    # transcript_format=TranscriptFormat.CHUNKS,
    # chunk_size_seconds=30,
)

transcript = document_loader.load()
# print(transcript[0].page_content)
print("Transcript length : " , len(transcript[0].page_content))  # 115145
print("*"*120)

### Indexing - text splitting

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)
chunks = text_splitter.split_text(transcript[0].page_content)

# print(chunks)
print("Chunks length : ",len(chunks))
print("*"*120)

### Indexing - embedding generation and storage

embedding = OpenAIEmbeddings(
    base_url="https://openrouter.ai/api/v1",
    model="openai/text-embedding-3-large"
)

vector_store = FAISS.from_texts(chunks, embedding)

# print(vector_store.index_to_docstore_id)
print("Vector store length : ",len(vector_store.index_to_docstore_id))
print("*"*120)


### Retreiver

retriever = vector_store.as_retriever(
    search_type="similarity", search_kwargs={"k": 4}
)
print("Retreiver",retriever)


result = retriever.invoke("What is this video about ?")
print("Test retriever with question, length of results vector fetches by retriever : ",len(result))
print("*"*120)


### Augmentation

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini" ,
    temperature=0.5
)

prompt_template = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)


user_query  = "What is this video about ?"
retrieved_docs  = retriever.invoke(user_query)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

prompt = prompt_template.invoke({
    'context' : context_text, 'question' : user_query
})

print("Prompt : ",prompt)
print("*"*120)

### Generation

answer = llm.invoke(prompt)
print("Final answer \n " , answer.content)