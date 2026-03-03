import os
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, create_react_agent, AgentExecutor
from langchain import hub

# Setup
llm = ChatOpenAI(model="gpt-4o-mini", api_key="<OPENAI_API_TOKEN>", temperature=0) # Temperature 0 is best for agents

# Define the tools
# load_tools is a quick way to grab community-contributed tools
tools = load_tools(["wikipedia"])

# Get the "ReAct" Prompt
# The agent needs a specific set of instructions on how to use tools.
# 'hwchase17/react' is the most famous standard prompt for this.
prompt = hub.pull("hwchase17/react")

# Define the agent
# This combines the LLM, the tools, and the ReAct reasoning instructions
agent = create_react_agent(llm, tools, prompt)

# Create an AgentExecutor
# This is the "engine" that actually runs the agent loop
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Invoke the agent
# verbose=True lets you see the "Thought" process in your terminal
response = agent_executor.invoke({"input": "How many people live in New York City?"})

print("Final Answer: ")
print(response["output"])