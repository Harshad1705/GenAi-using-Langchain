from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# this will not work because ChatAnthropic works with its native api
llm = ChatAnthropic(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="anthropic/claude-3.5-sonnet",
    temperature=0.5
)

# llm = ChatOpenAI(
#     api_key="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",
#     base_url="https://openrouter.ai/api/v1",
#     model="openai/gpt-4o-mini",
#     temperature=0.5
# )

result = llm.invoke("What is the capital of India")

print(result)