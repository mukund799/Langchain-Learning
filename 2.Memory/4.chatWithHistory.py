from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import (
    BaseChatMessageHistory, InMemoryChatMessageHistory
)
from langchain_core.runnables.history import RunnableWithMessageHistory


from dotenv import load_dotenv
import os
load_dotenv()

# Load environment variables from .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_MODEL_NAME = os.getenv("GOOGLE_MODEL_NAME")
print(f"api key {GOOGLE_API_KEY}, model name {GOOGLE_MODEL_NAME}")

# creating llm instance
llm = ChatGoogleGenerativeAI(model=GOOGLE_MODEL_NAME,api_key=GOOGLE_API_KEY)

prompt = ChatPromptTemplate(
    [
        ("system", "You are a assistant which help user to find their response."
          "and response back in suitable words."),
          MessagesPlaceholder("history"),
        (
            "human","{query}"
        )
    ]
)

chain = prompt | llm

# for history purpose

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

config = {"configurable": {"session_id": "abc2"}}
with_message_history = RunnableWithMessageHistory(chain, get_session_history, input_messages_key="query",history_messages_key="history")



# creating a question
while True:
    question = input("Enter a question: ")
    if question.lower() == "quit":
        break
    # generating an answer
    answer = with_message_history.invoke({"query":question},config=config)
    print(f"answer is {answer.content}\n")
    print(f"history is {get_session_history('abc2')}")
