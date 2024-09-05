- [StrOutputParser](#strOutputParser)
- [Chaining](#chaining)
- [Retriver](#retriver)
- [DataLoader](#dataLoader)
- [Splitter](#splitter)

## strOutputParser
 **StrOutputParser**

from langchain.schema.output_parser import StrOutputParser
result = model.invoke(query).StrOutputParser()

--> What it does is we don't have to extract the answer from response. this parser  will do for me and give back the content that i want.



---

## chaining
** Chaining **

Chaining is a concept where tasks or methods are called automatically in sequence. Under the hood, it creates two components:

1. **RunnableSequence**
2. **RunnableLambda**

### RunnableSequence

`RunnableSequence` is a class that is used to call a sequence of operations.

When you execute the following code:

```python
chain = prompt | model | StrOutputParser()
chain.invoke()
```

It works as follows:

```python
chain = RunnableSequence(
    first=format_prompt, 
    middle=[invoke_model], 
    last=output_parser
)
```

`RunnableSequence` takes only three arguments: `first`, `middle`, and `last`. If you have a chain of 50 operations, the first and last will remain the same, and the rest will go into the `middle` as a list.

### RunnableLambda

`RunnableLambda` creates the functions that are going to be executed one by one.

Examples:

```python
format_prompt = RunnableLambda(lambda x: ...)
invoke_model = RunnableLambda(lambda x: ...)
output_parser = RunnableLambda(lambda x: ...)
```

---

## retriver
**RETRIVER**
`Retriver` is nothing but an interface which help to interact with vector store. it just used for retrival purpose, not for the store.

1. `similarity` - By default it does `similarity` search. `similarity` search only focus to find the most relevant items without considering their similarity to each other.


2. `similarity_score_threshold` - if we want to do search_type as `similarity_score_threshold` then it is mandatory to mention the `score_threshold` value explicitly.

````python
retriever = db.as_retriever(
    search_type= "similarity_score_threshold",
    search_kwargs = {'k':1,'score_threshold':0.7}
)
````


3. `Maximum marginal relevance retrieval` - MmrRetriver is a class that is used to perform maximum marginal relevance retrieval.

    ```python
    retriever = rvs.max_marginal_relevance_search(
            query=query,
            lambda_mult=0.90,
            k=10,
            fetch_k=20,
            score_threshold=0.4
            )
    docs = retriever.invoke("what did he  ...")
    ```
    -lambda_mult: A float value that adjusts the trade-off between relevance and diversity. Values closer to 1 prioritize relevance, while values closer to 0 prioritize diversity.
    -k: The number of results to retrieve.
    -fetch_k: The number of documents to fetch from the index in each iteration.
    -score_threshold: The minimum score required for a document to be considered relevant.

---
## dataLoader
** DATA LOADER **
-`langchain` provides the predefined function which will help you to read the data from any source(Ex. Webpage, Pdf, Txt file etc.)

1. ***WebPage*** :- You have to mention the URL & it's done.
    you just need to install the bs4 library
```python
from langchain_community.document_loaders import WebBaseLoader, TextLoader
loader = WebBaseLoader(web_path="https://python.langchain.com/v0.2/docs/how_to/sequence/#the-pipe-method")
data = loader.load()
print(data)
# for loading the textfile.
loader = TextLoader(file_path = "")
```
---

## splitter
**SPLITTER** :- How to split your document or text into chunks so that it will easy and correct value while retrieving.
1. ***RecursiveCharacterTextSplitter*** :- This is the best text splitter among all. Attempts for splitting the text into natural boundries(like paragraph,sentences etc.)

    ```python
    text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
    )
    doc = text_splitter.split_documents(document)

    ```
2. ***CharacterTextSplitter*** :- This is also a type of splitter. Useful for consistent chunk size regardless of content structure.
    ```python
    text_splitter = CharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
    )
    doc = text_splitter.split_documents(document)
    ```