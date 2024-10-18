from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import faiss
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore

GOOGLE_API_KEY = "AIzaSyCeopduiKBLnmxBGuu8ZJvR-HRPHZdujes"
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

index = faiss.IndexFlatL2(len(embedding_model.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embedding_model,
    index=index,
    docstore= InMemoryDocstore(),
    index_to_docstore_id={}
)
def load_pdf() -> list[Document]:
    # Load a PDF file
    loader = PyPDFLoader('3.Rag/Home.pdf')
    pdf = loader.load()
    return pdf

def split_into_chunk(pdf:list[Document]) -> list[Document]:
    # Split the PDF into chunks
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
    )
    texts = text_splitter.split_documents(pdf)
    return texts
    
def create_vector_of_chunk(chunk : list[Document]):
    # embedding = embedding_model.embed_documents(chunk)
    # db = FAISS.from_documents(chunk, embedding_model)
    db = vector_store.add_documents(documents=chunk)
    return db
def main():
    # Load the PDF
    pdf = load_pdf()
    print(f" pdf is {pdf} and type is {type(pdf[0])}")

    # Split the PDF into chunks
    chunk = split_into_chunk(pdf)

    db = create_vector_of_chunk(chunk)
    # retriever = db.as_retriever()
    # print(retriever)
    # query = "i want to know that who is father of nikit "
    # res = db.invoke(query)
    # res = db.search(query=query, search_type="similarity")
    # print(res)
    results = vector_store.similarity_search(query="who is nikita",k=1)
    for doc in results:
        print(f"* {doc.page_content} [{doc.metadata}]")

main()