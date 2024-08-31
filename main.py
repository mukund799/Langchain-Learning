from langchain_google_genai import ChatGoogleGenerativeAI
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

'''

NORMAL PROMPT TEMPLATE

'''
from langchain_core.prompts import PromptTemplate
promptTemplate = PromptTemplate.from_template(input = ["adjective", "thing"] ,template="Tell me a {adjective} story about {thing}")

prompt = promptTemplate.format(adjective="sad", thing = "Horse")
print(f"prompt is: \n {prompt}")


# Createing prompt template for poem
poemPromptTemplate = PromptTemplate(input=['name','size'], template=" write a poem about the {name} in {size} word size")
poem = poemPromptTemplate.format(name="bird", size = 50)
print(f" prompt of poem is: \n {poem}")

# res = llm.invoke(prompt)
# print(res.content)

'''

CHATPROMPT TEMPLATE

'''

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

systemPrompt = PromptTemplate.from_template(input=['language'], template="You are an assistant which help human to find his answer. you will have to response back in {language}")
humanPrompt = PromptTemplate.from_template(input=['country'], template="What is the capital of {country}")
systemPrompt = systemPrompt.format(language = 'french')
humanPrompt = humanPrompt.format(country = "India")


chatPrompt = ChatPromptTemplate.from_messages(
    [
    SystemMessage(content=systemPrompt),
    HumanMessage(content=humanPrompt)
    ]
)
prompt = chatPrompt.format()

# print(f" chat prompt is: {prompt}")
# res = llm.invoke(prompt)
# print(res.content)

'''
GET PROMPT FROM A FILE
'''

filePrompt = PromptTemplate.from_file("prompt.txt")
# filePrompt = filePrompt.format()

chain = filePrompt | llm
res = chain.invoke({})
print(res.content)