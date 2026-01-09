from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

# using huggingace free llm , this works for all open source and free source llm

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template= "Write a detailed report on {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template= "Write a 5 line summary on following text \n {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({"topic":"Black Hole"})

result  = model.invoke(prompt1)

prompt2 = template2.invoke({"text":result.content})

result  = model.invoke(prompt2)

print(result.content)


