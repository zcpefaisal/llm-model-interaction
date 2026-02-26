import os
from langchain_openai import ChatOpenAI

# Define the LLM
# In the latest LangChain (2026), we use the langchain_openai package
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="<OPENAI_API_TOKEN>", 
    temperature=0.7
)

# Define the prompt
prompt = 'Three reasons for using LangChain for LLM application development.'

# Invoke the model
# .invoke() is the standard method for getting a response in modern LangChain
response = llm.invoke(prompt)

# Print only the text content
print(response.content)
