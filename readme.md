1. [StrOutputParser][#StrOutputParser]


## StrOutputParser
 **StrOutputParser**

from langchain.schema.output_parser import StrOutputParser
result = model.invoke(query).StrOutputParser()

--> What it does is we don't have to extract the answer from response. this parser  will do for me and give back the content that i want.



---

# Chaining

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




# RETRIVER
`Retriver` is nothing but an interface which help to interact with vector store. it just used for retrival purpose, not for the store.

1. By default it does `similarity` search.
2. if we want to do search_type as `similarity_score_threshold` then it is mandatory to mention the `score_threshold` value explicitly.
````python
retriever = db.as_retriever(
    search_type= "similarity_score_threshold",
    search_kwargs = {'k':1,'score_threshold':0.7}
)
````
---