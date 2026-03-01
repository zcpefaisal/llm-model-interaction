import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate


# Create the example dataset
examples = [
    {
        "question": "How many DataCamp courses has Jack completed?",
        "answer": "36"
    },
    {
        "question": "How much XP does Jack have on DataCamp?",
        "answer": "284,320XP"
    },
    {
        "question": "What technology does Jack learn about most on DataCamp?",
        "answer": "Python"
    }
]



#===================================#
#   Build the Few-Shot Template     #
#===================================#

# This template defines how ONE individual example looks
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")

# This combines the examples, the formatter, and the new input
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}\nAnswer:", # Added 'Answer:' to guide the AI
    input_variables=["input"],
)





#===================================#
#   Create and Invoke the Chain     #
#===================================#

llm = ChatOpenAI(model="gpt-4o-mini", api_key="<OPENAI_API_TOKEN>")

# Modern LCEL (LangChain Expression Language) Chain
llm_chain = prompt_template | llm

# Test the chain
query = "What is Jack's favorite technology on DataCamp?"
response = llm_chain.invoke({"input": query})

print("Final Formatted Prompt Sent to AI: ")
print(prompt_template.format(input=query))
print("AI Response: ")
print(response.content)