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

# Integrating with an Agent

# In modern LangChain, ReAct agents require a specific prompt template
# We pull the standard 'hwchase17/react' prompt from the LangChain Hub
prompt = hub.pull("hwchase17/react")

# Define the ReAct agent logic
agent = create_react_agent(llm, [retrieve_customer_info], prompt)

# Create the AgentExecutor (the engine that runs the agent loop)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=[retrieve_customer_info], 
    verbose=True, 
    handle_parsing_errors=True
)

# Invoke the agent
user_input = "Create a summary of our customer: Peak Performance Co."
response = agent_executor.invoke({"input": user_input})

print("AI SUMMARY: ")
print(response["output"])