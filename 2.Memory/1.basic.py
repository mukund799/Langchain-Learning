from langchain_google_genai import ChatGoogleGenerativeAI
GOOGLE_API_KEY = 'AIzaSyCeopduiKBLnmxBGuu8ZJvR-HRPHZdujes'
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key= GOOGLE_API_KEY)



from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
memory = ConversationBufferMemory(memory_key="chat_history")

from langchain.chains import ConversationChain
conversation = ConversationChain(
    llm=llm, memory=ConversationBufferWindowMemory(k = 2)
)

while True:
    user_input = input("You: ")
    if user_input == "bye":
        print("it done")
        break
    res = conversation.predict(input=user_input)
    print(res)

# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain.schema.output_parser import StrOutputParser

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "you are a good assistant which answer only in english"),
#         ("human","{question}")
#     ]
# )

# res = prompt |  llm | StrOutputParser() 
# qes = ""
# while( qes.lower() != "exit"):
    # qes = input(" enter your question ")
    # result = res.invoke({"question":qes})
    # print(result)
    # memory.save_context({"input":qes},{"output":result})
    # # print(memory.load_memory_variables({"memory_key":"chat_history"}))