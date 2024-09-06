- [StrOutputParser](#strOutputParser)
- [Chaining](#chaining)
- [Retriver](#retriver)
- [DataLoader](#dataLoader)
- [Splitter](#splitter)
- [PromptTemplate](#promptTemplate)

## promptTemplate
1. `ChatPromptTemplate`
    - **from_message** and **from_strings** both works as similar. it takes a list of tuple and return the ChatPromptTemplate.
    - although **from_strings** is deprecated.

    ```python

    prompt1 = ChatPromptTemplate.from_messages(
                [
                    ("system","you are an assistant which will give answer of any question. you will always generate two answer."),
                    ("human","{question}")
                ]
            )
    prompt2 = ChatPromptTemplate.from_stringss(
                [
                    ("system","you are an assistant which will give answer of any question. you will always generate two answer."),
                    ("human","{question}")
                ]
            )

    ```

    
    - To convert this chatPromptTemplate, so we can pass to llm we use `invoke` or `format_message`.
    - `invoke` will take a json or dict as input while in `format_message` we can pass n no. of string.
    ```python
        prompt = prompt.invoke({"question":"what is mango?"})
        prompt = prompt.format_messages(question = "what is mango")
    ```


---
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

    a threshold value is set for the similarity score between the query and the documents. Documents with a similarity score above the threshold are considered relevant and are returned as results. This approach focuses on retrieving documents that are highly similar to the query, without considering the diversity of the results.
    Key characteristics:

    • Threshold-based: Documents are selected based on a predefined similarity score threshold.
    • Similarity-focused: The primary goal is to retrieve documents that are highly similar to the query.
    • No diversity consideration: The technique does not explicitly consider the diversity of the results.

````python
retriever = db.as_retriever(
    search_type= "similarity_score_threshold",
    search_kwargs = {'k':1,'score_threshold':0.7}
)
````


3. `Maximum marginal relevance retrieval` - MmrRetriver is a class that is used to perform maximum marginal relevance retrieval.

    `Diversity` In the context of Maximum Marginal Relevance (MMR), diversity refers to the degree of dissimilarity or uniqueness among the retrieved results. The goal of MMR is to maximize the diversity of the results while maintaining their relevance to the query.
    In other words, diversity in MMR means that the selected results should:

    • Cover different aspects: Represent different facets or perspectives of the topic, rather than repeating the same information.
    • Minimize redundancy: Avoid duplicating or closely resembling each other, providing a more comprehensive view of the topic.
    • Show varied content: Include a mix of different content types, such as images, videos, articles, or reviews, to cater to different user preferences.


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
    - lambda_mult: A float value that adjusts the trade-off between relevance and diversity. Values closer to 1 prioritize relevance, while values closer to 0 prioritize diversity.
    - k: The number of results to retrieve.
    - fetch_k: The number of documents to fetch from the index in each iteration.
    - score_threshold: The minimum score required for a document to be considered relevant.

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