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


# Example 1: first we will get response, then will check that whatever response we got is true or not
message = [
    SystemMessage(content='You are an assistant whose duty is give a proper response'),
    HumanMessage(content="Tell me 3 good Joke about Engineeer")    
]
prompt1 = ChatPromptTemplate.from_messages(message)
chain = prompt1 | model | StrOutputParser()
response = chain.invoke({})

template = "you have to tell that on the given below make someone laugh or not. joke : {joke} "
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model | StrOutputParser()
res = chain.invoke({"joke":response})
# print(res)

# Example 2: other way of calling the two chain from single chain

message = [
    SystemMessage(content='You are an assistant whose duty is give a proper response'),
    HumanMessage(content="Tell me 3 good Joke about Engineeer")    
]
prompt1 = ChatPromptTemplate.from_messages(message)
template = "you have to tell that on the given below make someone laugh or not. joke : {joke} "
prompt2 = ChatPromptTemplate.from_template(template)

chain = prompt1 | model | StrOutputParser() | prompt2 | model | StrOutputParser()
res = chain.invoke({})
print(res)