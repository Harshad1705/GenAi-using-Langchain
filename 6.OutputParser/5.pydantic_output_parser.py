from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field

# using huggingace free llm , this works for all open source and free source llm


llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it"
)

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):
    name : str = Field(description="Name of person")
    age : int = Field(gt=18 , description="Age of person")
    city : str = Field(description="name of the city from person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate a name, age and city of fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({"place":"indian"})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

print(prompt)

chain = template | model | parser

result = chain.invoke({"place":"indian"})

print(result)