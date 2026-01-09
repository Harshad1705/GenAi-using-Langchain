from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableBranch ,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

model = ChatOpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0.5
)

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Give the sentiment of feedback")


parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Cassify the sentiment of following feedback text into postive or negative \n {feedback} \n {format_instruction} ",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)


prompt2 = PromptTemplate(
    template="Write an appropriate response to the positive feedback \n {feedback}",
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template="Write an appropriate response to the negative feedback \n {feedback}",
    input_variables=['feedback']
)


branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive' , prompt2 | model | parser ),
    (lambda x:x.sentiment=='negative' , prompt3 | model | parser ),
    RunnableLambda(lambda x : "Could not find sentiment")
)


classifier_chain = prompt1 | model | parser2


chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'This is terrible smartphone'})



print(result)


chain.get_graph().print_ascii()