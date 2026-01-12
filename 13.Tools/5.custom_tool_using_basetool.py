from langchain_core.tools import BaseTool
from pydantic import BaseModel,Field
from typing import Type

class MultiplyInput(BaseModel):
    a : int = Field(required=True,description="the first number to add")
    b : int = Field(required=True,description="the second number to add")


class MultiplyTool(BaseTool):
    name : str = "multiply"
    description : str = "Multiply two number"

    args_schema : Type[BaseTool] = MultiplyInput

    def _run(self,a:int,b:int) -> int:
        return a*b




multiply_tool = MultiplyTool()

result = multiply_tool.invoke({"a":2,"b":7})

print(result)

print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)

# what llm sees
print(multiply_tool.args_schema.model_json_schema())