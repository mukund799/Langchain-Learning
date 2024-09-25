from langchain_google_genai import ChatGoogleGenerativeAI
GOOGLE_API_KEY = 'AIzaSyCeopduiKBLnmxBGuu8ZJvR-HRPHZdujes'
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key= GOOGLE_API_KEY)
from langchain_core.messages import HumanMessage

from langchain_core.chat_history import (
    BaseChatMessageHistory, InMemoryChatMessageHistory
)
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

config = {"configurable": {"session_id": "abc2"}}

# 1. A simple method to do conversation 




from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system","you are a good assistant"),
    ("human","{question}")
])
chain = prompt | llm

with_message_history = RunnableWithMessageHistory(chain, get_session_history)

# while True:
#     user_input = input("You: ")
#     if user_input == "bye":
#         print("it done")
#         break
#     response = with_message_history.invoke(
#         {"question":user_input},
#         config=config,
#     )

#     print(response.content)







# 2nd method 
"""



Dictionary input, message(s) output
Besides just wrapping a raw model, the next step up is wrapping a prompt + LLM. 
This now changes the input to be a dictionary (because the input to a prompt is a dictionary). 
This adds two bits of complication.

First: a dictionary can have multiple keys, but we only want to save ONE as input. 
In order to do this, we now now need to specify a key to save as the input.

Second: once we load the messages, we need to know how to save them to the dictionary. 
That equates to know which key in the dictionary to save them in. 
Therefore, we need to specify a key to save the loaded messages in.

Putting it all together, that ends up looking something like:





"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a assistant which can answer in {language}"),
        MessagesPlaceholder("history"),
        ("human","{question}")
    ]
)

chain = prompt | llm

with_message_history = RunnableWithMessageHistory(
    chain,get_session_history=get_session_history,input_messages_key="question", history_messages_key="history"
)

# while True:
    # language = input("answer language")
    # user_input = input(" user question ")
    # if user_input == "bye":
    #     break
    # res = with_message_history.invoke(
    #     {"language":language, "question":user_input},
    #     config=config
    # )
    # print(res.content)