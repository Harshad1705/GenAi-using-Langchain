from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableBranch

model = ChatOpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0.5
)


prompt1 = PromptTemplate(
    template="Write a detail report on topic \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="summarize the following text \n {text}",
    input_variables=['text']
)


parser = StrOutputParser()


report_gen_chain = RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x : len(x.split())>100 , RunnableSequence(prompt2,model,parser)),
     RunnablePassthrough()
)

report = RunnableSequence(report_gen_chain , branch_chain)
result = report.invoke({'topic': 'Russia vs Ukraine War'})

print(result)

report.get_graph().print_ascii()