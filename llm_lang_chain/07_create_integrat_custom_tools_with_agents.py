import os
import pandas as pd
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Sample DataFrame representing data
customers = pd.DataFrame({
    "name": ["Peak Performance Co.", "Global Tech Inc.", "Eco-Smart Sol"],
    "plan": ["Enterprise", "Startup", "Enterprise"],
    "support_tier": ["Gold", "Silver", "Platinum"]
})

llm = ChatOpenAI(model="gpt-4o-mini", api_key="<OPENAI_API_TOKEN>", temperature=0)

# Defining the Custom Tool

@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name from the database."""
    # Filter the DataFrame for the specific customer
    customer_info = customers[customers['name'] == name]
    
    if customer_info.empty:
        return f"No customer found with the name: {name}"
    
    return customer_info.to_string(index=False)

# Verification the retrieve customer info
print(f"Tool Schema Arguments: {retrieve_customer_info.args}\n")
