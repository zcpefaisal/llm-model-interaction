import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# Define the LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key="<OPENAI_API_TOKEN>")

# Create a structured Chat Prompt Template
# This uses "Few-Shot" prompting: System -> Human -> AI (example) -> Human (real)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a geography expert that returns the colors present in a country's flag."),
        ("human", "France"),
        ("ai", "blue, white, red"),
        ("human", "{country}")
    ]
)

# Build the LCEL (LangChain Expression Language) Chain
llm_chain = prompt_template | llm

# Invoke the chain with the variable
country = "Japan"
response = llm_chain.invoke({"country": country})

print(f"Colors of the {country} flag:")
print(response.content)