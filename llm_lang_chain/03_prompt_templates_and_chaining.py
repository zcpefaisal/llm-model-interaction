import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Define the Template
# The {question} acts as a placeholder that LangChain will fill later
template = "You are an artificial intelligence assistant, answer the question. {question}"
prompt = PromptTemplate.from_template(template=template)

# Define the LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key="<OPENAI_API_TOKEN>") 

# Create the Chain using LCEL
# Think of the pipe '|' as a data pipeline
llm_chain = prompt | llm

# Invoke the chain
# We pass a dictionary where the key matches the placeholder in our template
question = "How does LangChain make LLM application development easier?"
response = llm_chain.invoke({"question": question})

print("--- Our AI Response Is ---")
print(response.content)