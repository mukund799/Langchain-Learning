from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

GOOGLE_API_KEY="AIzaSyCeopduiKBLnmxBGuu8ZJvR-HRPHZdujes"
print(GOOGLE_API_KEY)
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',api_key=GOOGLE_API_KEY)

# This will be the response when you do AI search. Ai search return type will be List of Document
docs = [
    Document(page_content="Jesse loves red but not yellow"),
    Document(page_content = "Jamal loves green but not as much as he loves orange")
]

prompt = ChatPromptTemplate.from_messages(
    [
        ('human',' you have to find that who loves which color from the given . {context} '),
    ]
)
chain = create_stuff_documents_chain(llm,prompt)
res = chain.invoke({"context":docs})
print(res)



