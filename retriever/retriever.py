from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader


import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
def __init__(self):
    GOOGLE_API_KEY

embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)


loader = PyPDFLoader('Home.pdf')
loader = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False)
split = splitter.split_documents(loader)


db = FAISS.from_documents(embedding=embedding_model, documents=split)
print(db)

retriever = db.as_retriever(
    search_type= "similarity_score_threshold",
    search_kwargs = {'k':1,'score_threshold':0.7}
)

query = "i want to know that who is father of nikit "
res = retriever.invoke(query)
print(res)
