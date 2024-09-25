from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
GOOGLE_API_KEY = "AIzaSyCeopduiKBLnmxBGuu8ZJvR-HRPHZdujes"
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
def step():
     #step 1: loading the data from web page
    # it will have List of Document: List[Document]
    from langchain_community.document_loaders import WebBaseLoader
    data = WebBaseLoader(web_path="https://ineuron.ai/one-neuron")
    data = data.load()
    print(f"data of web path is {data}")

    # step 2: chunking the list of document
    # it will have List of Chunk: List[Document]

    from langchain.text_splitter import RecursiveCharacterTextSplitter
    # from langchain_text_splitters import RecursiveCharacterTextSplitter
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 200 )
    chunk = splitter.split_documents(data)
    print(f"chunk is {chunk}")



    # step 3: create embeddings and store into some vector store

    from langchain_community.vectorstores import FAISS
    from langchain_community.docstore.in_memory import InMemoryDocstore  

    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    GOOGLE_API_KEY = "AIzaSyCeopduiKBLnmxBGuu8ZJvR-HRPHZdujes"
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
    embeddings = FAISS.from_documents(documents=chunk, embedding=embedding_model,docstore = InMemoryDocstore())
    print(f"embeddings of web path is {embeddings}")
    FAISS.save_local(embeddings,folder_path="/Users/mukundnarayan/Desktop/Github/Backend/Langchain/2.Memory")



# step 4: create retriever of that vector store
retriever = FAISS.load_local(embeddings= embedding_model,folder_path="/Users/mukundnarayan/Desktop/Github/Backend/Langchain/2.Memory", allow_dangerous_deserialization = True)
retriever = retriever.as_retriever()
print(f"retriever of web path is {retriever}")

# step 6: creating chain that will retrieve data from source or retriever(create_retrivel_cahin)
# then pass the data which we got from create retrivel chain to create_stuff_documents_chain
# which will provide us the final answer

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_google_genai import ChatGoogleGenerativeAI
GOOGLE_API_KEY = 'AIzaSyCeopduiKBLnmxBGuu8ZJvR-HRPHZdujes'
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key= GOOGLE_API_KEY)
from langchain_core.prompts import ChatPromptTemplate


# this will be context only bcz from RETRIEVal we get data in context node only.
prompt = ChatPromptTemplate.from_messages([
    ("system","you are a good assistant. you have to answer from the given context. <context>{context}</context>"),
    ("human","{input}")
])

combine_docs_chain = create_stuff_documents_chain(
    llm, prompt
)


chain = create_retrieval_chain(retriever,combine_docs_chain)


while True:
    user_input = input(" your question")
    res = chain.invoke({"input": user_input})
    print(res)




