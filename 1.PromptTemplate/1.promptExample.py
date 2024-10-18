from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyCeopduiKBLnmxBGuu8ZJvR-HRPHZdujes")
# 1
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are an assistant which will give answer of any question. you will always generate two answer."),
        ("human","{question}")
    ]
)
prompt = prompt.invoke({"question":"what is mango?"})
# res = llm.invoke(prompt)
# print(res.content)

#2
prompt = ChatPromptTemplate.from_strings (
    [
        ("system","you are an assistant which will give answer of any question. you will always generate two answer."),
        ("human","{question}")
    ]
)
# prompt = prompt.invoke({"question":"what is mango?"})
prompt = prompt.format_messages(question = "what is mango")
res = llm.invoke(prompt)
print(type(res))

#3
prompt = ChatPromptTemplate (
    [
        ("system","you are an assistant which will give answer of any question. you will always generate two answer."),
        ("human","{question}")
    ]
)
prompt = prompt.invoke({"question":"what is mango?"})
print(prompt)
from langchain import hub

