from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

# using huggingace free llm , this works for all open source and free source llm
# StructuredOutputParser is removed in Lnagchain 2+ version

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1',description="Fact 1 about the topic"),
    ResponseSchema(name='fact_2',description="Fact 2 about the topic"),
    ResponseSchema(name='fact_3',description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me 3 fact about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({"topic":"black hole"})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)


chain = template | model | parser

result = chain.invoke({"topic":"black hole"})

print(result)