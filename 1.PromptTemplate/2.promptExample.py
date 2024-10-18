from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage 
import os

'''
Loading api keys to run gemeni
'''
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

'''
1. Learning PromptTemplate
'''

# to use from_template, We have to provide only the string. You can follow below example
basic_template = " you are a human, which can {action}"
basic_template1 = ChatPromptTemplate.from_template(basic_template)
basic1 = basic_template1.invoke({"action":"cry"})
print(f"basic1: \n {basic1}")

# to use from_message, We have to provide list of tuple
message = [
    ("system", "You are a good {noun}, you can find anything"),
    ("human", "where is {place}"),
]
basic_template2 = ChatPromptTemplate.from_messages(message)
basic2 = basic_template2.invoke({"noun":"person", "place":"India"})
print(f"basic2: \n {basic2}")

# extended version of above example
message3 = [
    ("human", "where is {place}"),
]
basic_template3 = ChatPromptTemplate.from_messages(message3)
basic3 = basic_template3.invoke({ "place":"India"})
print(f"basic3: \n {basic3}")



# first thing --> if you want to make changes in content then we will go with simple template form. We will not mention HumanMessage
# from langchain and put content in it.  That willl not work. See example 1 and 2;
# in example 3 you can see that only those in tuple format, is getting replaced by it's value. You can test Example 4 also. Incase you won't belive.


# Example 1: You can put value dynamicaly
template = ChatPromptTemplate(
    [
        ("system"," You are an stand up comedian which tells joke about {topic} "),
        ("human", "Tell me {count} joke about that topic?"),
    ]
)
prompt = template.invoke({"topic":"Life", "count":"4"})
print(prompt)

# Example 2: can't put 
template2 = ChatPromptTemplate(
    [
        SystemMessage(content="You are a good comedian. "),
        HumanMessage(content=" tell me 3 joke")
    ]
)

prompt2 = template2.invoke({})
print(prompt2)

# Example 3: Both(static and dynamic)
template3 = [
        SystemMessage(content="You are a good History teller. "),
        ("human", "Tell me history about the {topic} ?")
    ]
template3 = ChatPromptTemplate.from_messages(
    template3
)

prompt3 = template3.invoke({"topic":"First Atomic Bomb"})
print("I am example3 prompt: \n",prompt3)


# Example 4: Without tuple it won't replace. see below template 4 code
template4 = ChatPromptTemplate(
    [
        SystemMessage(content="You are a good Speaker "),
        HumanMessage(content = "Tell me history about the {topic}?")
    ]
)

prompt4 = template4.invoke({"topic":"dumb Socity"})
print(prompt4)