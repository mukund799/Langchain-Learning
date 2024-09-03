from langchain_community.document_loaders import WebBaseLoader, TextLoader
from bs4 import BeautifulSoup
loader = WebBaseLoader(web_path="https://python.langchain.com/v0.2/docs/how_to/sequence/#the-pipe-method")
data = loader.load()
# print(data)

loader = TextLoader(file_path='DataLoader/example.txt')
data = loader.load()
print(data)

