import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="YouTube RAG Chatbot", layout="centered")
st.title("🎥 YouTube Video Chatbot (RAG)")
st.write("Ask questions from a YouTube video using LangChain + FAISS")

youtube_url = st.text_input("🔗 Enter YouTube URL")
user_query = st.text_input("❓ Ask a question")

if st.button("Ask"):
    if not youtube_url or not user_query:
        st.warning("Please provide both YouTube URL and question.")
        st.stop()

    with st.spinner("Processing video..."):
        try:
            # ---------------- Load transcript ----------------
            loader = YoutubeLoader.from_youtube_url(
                youtube_url,
                add_video_info=False,
                language=["en", "hi"]
            )
            transcript_docs = loader.load()
            transcript_text = transcript_docs[0].page_content

            # ---------------- Split text ----------------
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.split_text(transcript_text)

            # ---------------- Embeddings + Vector Store ----------------
            embeddings = OpenAIEmbeddings(
                base_url="https://openrouter.ai/api/v1",
                model="openai/text-embedding-3-large"
            )
            vector_store = FAISS.from_texts(chunks, embeddings)

            # ---------------- Retriever ----------------
            retriever = vector_store.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 4}
            )

            # ---------------- Prompt ----------------
            prompt_template = PromptTemplate(
                template="""
                You are a helpful assistant.
                Answer ONLY from the provided transcript context.
                If the context is insufficient, just say you don't know.

                {context}
                Question: {question}
                """,
                input_variables=["context", "question"]
            )

            # ---------------- LLM ----------------
            llm = ChatOpenAI(
                base_url="https://openrouter.ai/api/v1",
                model="openai/gpt-4o-mini",
                temperature=0.5
            )

            # ---------------- Chain ----------------
            def create_context(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            parser = StrOutputParser()

            chain = (
                RunnableParallel({
                    "context": retriever | RunnableLambda(create_context),
                    "question": RunnablePassthrough()
                })
                | prompt_template
                | llm
                | parser
            )

            answer = chain.invoke(user_query)

            # ---------------- Output ----------------
            st.success("Answer:")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")
