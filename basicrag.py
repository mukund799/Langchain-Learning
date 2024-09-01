from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

GOOGLE_API_KEY = "AIzaSyCeopduiKBLnmxBGuu8ZJvR-HRPHZdujes"
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

def load_pdf():
    # Load a PDF file
    loader = PyPDFLoader('Home.pdf')
    pdf = loader.load()
    # result = ""
    # for page in pdf:
    #     result += page.page_content
    # return result
    return pdf

def split_into_chunk(pdf):
    # Split the PDF into chunks
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
    )
    texts = text_splitter.split_documents(pdf)
    chunks = [str(chunk) for chunk in texts]
    return texts
    
def create_vector_of_chunk(chunk):
    # embedding = embedding_model.embed_documents(chunk)
    db = FAISS.from_documents(chunk, embedding_model)
    return db
def main():
    # Load the PDF
    pdf = load_pdf()
    print(pdf)
    # Split the PDF into chunks
    chunk = split_into_chunk(pdf)
    db = create_vector_of_chunk(chunk)
    retriever = db.as_retriever()
    print(retriever)

main()