from langchain_openai import OpenAI,ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# it will not work
llm = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-3.5-turbo-instruct"
)

# this will work
llm = ChatOpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-3.5-turbo-instruct"
)

result = llm.invoke("What is the capital of India")

print(result)