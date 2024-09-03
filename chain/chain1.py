from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage 
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash',api_key=GOOGLE_API_KEY)
def home():
    print("i am home")
# Example 1: basic way to call the model
message = [
    SystemMessage(content='You are an assistant whose duty is give a proper response'),
    HumanMessage(content="Tell me 3 good Joke about Engineeer")    
]
prompt = ChatPromptTemplate.from_messages(message)
prompt = prompt.invoke({})
# response = model.invoke(prompt)
# print(response.content)

# Example 2: By making a chain here
message = [
    SystemMessage(content='You are an assistant whose duty is give a proper response'),
    HumanMessage(content="Tell me 3 good Joke about Engineeer")    
]
prompt = ChatPromptTemplate.from_messages(message)
chain = prompt | model | StrOutputParser()
# res = chain.invoke({})
# print(res)



# Example 3: we can also create RunableLambda and call it through chain.
# in Below example we furthure calling two runnable method which will convert the response to capital letters and 
# find the size of response.
converter = RunnableLambda(lambda x : x.upper())
responseSize = RunnableLambda(lambda x: len(x))
message = [
    SystemMessage(content='You are an assistant whose duty is give a proper response'),
    HumanMessage(content="Tell me 3 good Joke about Engineeer")    
]
prompt = ChatPromptTemplate.from_messages(message)
chain = prompt | model | StrOutputParser() | converter | responseSize
res = chain.invoke({})
print(res)
