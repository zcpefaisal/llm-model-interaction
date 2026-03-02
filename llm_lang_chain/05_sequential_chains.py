import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Setup Environment
llm = ChatOpenAI(model="gpt-4o-mini", api_key="<OPENAI_API_TOKEN>")

# Define Prompts

# The first prompt generates the "raw" idea
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

# The second prompt expects a variable called 'learning_plan'
time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a concise plan to help me hit this goal: {learning_plan}."
)

# The Sequential Chain

# Step-by-step breakdown of the LCEL sequence:
# 1. Takes {"activity": "..."}
# 2. Runs learning_prompt | llm | StrOutputParser()
# 3. Maps that result to a new dictionary: {"learning_plan": "The AI's Response"}
# 4. Passes that dictionary into time_prompt
# 5. Runs through the LLM again for the final 'condensed' version
seq_chain = (
    {"learning_plan": learning_prompt | llm | StrOutputParser()}
    | time_prompt
    | llm
    | StrOutputParser()
)

# Run the full sequence
# Note: Input key must match the first prompt's input_variables
activity_choice = "play the harmonica"
final_output = seq_chain.invoke({"activity": activity_choice})

print(f"Final 1-Week Plan for: {activity_choice}")
print(final_output)