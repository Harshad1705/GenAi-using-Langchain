from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


loader = DirectoryLoader(
    path="8.DocumentLoaders/some_folder",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(docs)
print()
print(len(docs))
print()
print(docs[0].page_content)
print()
print(docs[0].metadata)

