from langchain_core.tools import tool


@tool
def multiply(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a*b

@tool
def add(a:int,b:int) -> int:
    """Addition of two numbers"""
    return a+b

class MathToolKit:
    def get_tools(self):
        return [add,multiply]


tool_kit = MathToolKit()

tools = tool_kit.get_tools()

for tool in tools:
    print(tool.name,"=>",tool.description)