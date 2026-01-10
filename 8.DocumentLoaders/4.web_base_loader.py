from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0.5,
     default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "Web Loader Demo"
    }
)

prompt = PromptTemplate(
    template="Answer the following {question} from following text \n {text}",
    input_variables=['question','text']
)

parser = StrOutputParser()

loader = WebBaseLoader(
    web_paths=[
        'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    ]
)

docs = loader.load()



# print(docs)
# print()
# print(len(docs))
# print()
# print(docs[0].page_content)
# print()
# print(docs[0].metadata)

chain = prompt | model | parser
result = chain.invoke({"question":"best phone" , "text":docs[0].page_content})

print(result)

