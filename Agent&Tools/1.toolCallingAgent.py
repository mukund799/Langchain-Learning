from dotenv import load_dotenv
load_dotenv()

#load the llm
import os
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
MODEL_NAME = os.getenv('GOOGLE_MODEL_NAME')
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model=MODEL_NAME, api_key= GOOGLE_API_KEY)

from langchain.agents import tool
@tool
def summation(a:int, b:int, c:int) -> int:
    """ return the sum of three numbers"""
    return a + b + c


@tool
def wordLength(word: str) -> int:
    """return the length of a word"""
    return len(word)

@tool
def greet(name: str) -> str:
    """return a greeting message"""
    return f"Hello, {name}!"

# Load the tools
tools = [summation, wordLength,greet]


# creating agent
from langchain import hub

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")
print(prompt.messages)
from langchain.agents import create_tool_calling_agent

agent = create_tool_calling_agent(llm, tools, prompt)

from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# execute the agent
while True:
    query = input("enter query\n")
    if query.lower() == 'quit':
        print("Happy to end!")
        break
    result = agent_executor.invoke({'input':query})
    print(result)