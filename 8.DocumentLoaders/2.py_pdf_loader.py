from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0.5
)

prompt = PromptTemplate(
    template="Write a summary of following poem \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader(file_path="8.DocumentLoaders/cricket.txt" , encoding="utf-8")

docs = loader.load()

# print(docs)
# print(type(docs))
# print(len(docs))
# print(docs[0])
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)