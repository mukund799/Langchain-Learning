**StrOutputParser**

from langchain.schema.output_parser import StrOutputParser
result = model.invoke(query).StrOutputParser()

--> What it does is we don't have to extract the answer from response. this parser  will do for me and give back the content that i want.


*** ChainIng ***

it is nothing but the call the things automaticallly. Under the hood it create two thing. 
1-> It call a method callled RunnableSequence
2-> It call a method called RunnableLambda.

*RunnableSequence*
it is a class that is used to call a sequence of things.

when we do chain = prompt | model |StrOutputParser and chain.invoke(); it means it works as below
chain = RunnableSequence(first = format_prompt, middle = [invoke_model], last = output_parser)
RunnableSequence takes only 3 args. but if we have like 50, then first and last will as it is. And for rest it will got to middle as list

* RunnableLambda *
It create all those function which are going to execute one by one.
format_prompt = RunnableLambda( lambda x: ....)
invoke_model = RunnableLambda( lambda x: ....)
output_parser = RunnableLambda( lambda x: ....)