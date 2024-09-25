'''

First we are setting up the tools using langchain. we are creating custom tool

'''

from langchain_core.tools import tool


@tool
def multiply(first_int: int, second_int: int) -> int:
    """Multiply two integers together."""
    return first_int * second_int

@tool
def add(first_int: int, second_int: int) -> int:
    """add two integers together."""
    return first_int * second_int

@tool
def greeting() -> str:
    """it will greet back when any greetings msg see"""
    return "Hii, Thank you. How can i help you! "

tools = [multiply,add,greeting]
a = multiply.invoke({"first_int": 4, "second_int": 5})
print(a)