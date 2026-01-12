from langchain_core.tools import tool


@tool
def multiply(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a*b


result = multiply.invoke({"a":2,"b":7})

print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

# what llm sees
print(multiply.args_schema.model_json_schema())