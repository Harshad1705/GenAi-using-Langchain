from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

model = ChatOpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini"
)

prompt  =PromptTemplate(
    template="Write a joke om topic \n {topic}",
    input_variables=['topic']
)

prompt2  =PromptTemplate(
    template="Explain the following joke  \n {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)

result = chain.invoke({"topic":"AI"})

print(result)