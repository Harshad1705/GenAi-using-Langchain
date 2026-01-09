from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence

model = ChatOpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0.5
)


prompt1 = PromptTemplate(
    template="Generate a tweet about topic \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post about \n {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1 , model , parser) , 
    'linkedin' : RunnableSequence(prompt2 , model , parser)
})


result = parallel_chain.invoke({'topic': 'AI'})

print(result['tweet'])
print(result['linkedin'])

parallel_chain.get_graph().print_ascii()