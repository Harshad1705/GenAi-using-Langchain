from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field


class MultiplyInput(BaseModel):
    a : int = Field(required=True,description="the first number to add")
    b : int = Field(required=True,description="the second number to add")


def multiply_func(a,b):
    return a*b

multiply_tool = StructuredTool.from_function(
    func = multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({"a":2,"b":7})

print(result)

print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)

# what llm sees
print(multiply_tool.args_schema.model_json_schema())