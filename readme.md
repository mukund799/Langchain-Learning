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

---

This markdown file is now correctly formatted with appropriate headings, code blocks, and explanations, making it more readable on GitHub.