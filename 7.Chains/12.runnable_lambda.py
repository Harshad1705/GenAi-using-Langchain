from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough, RunnableLambda

model = ChatOpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0.5
)


prompt1 = PromptTemplate(
    template="Write a joke on topic \n {topic}",
    input_variables=['topic']
)

def word_count(text):
    return len(text.split())


parser = StrOutputParser()


primary_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough() , 
    'word_count' : RunnableLambda(word_count)
})

chain = RunnableSequence(primary_chain , parallel_chain)
result = chain.invoke({'topic': 'AI'})

print(result)

parallel_chain.get_graph().print_ascii()