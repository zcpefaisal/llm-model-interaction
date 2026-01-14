import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the variables from .env into the environment
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Retrieve the key using os.getenv

messages = [
    {"role": "system", "content": "You are a data science tutor who provides short, simple explanation."},
]

user_qs = ["Why is python so popular?", "Summarize this in one sentence"]

for q in user_qs:
    print("User: ", q)
    user_dict = {"role":"user", "content": q}
    messages.append(user_dict)

    # Send the chat messages to the model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=100
    )

    # Extract the assistant message from the response
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}

    # Add assistant_dict to the messages dictionary
    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n") 

    # User: Why is python so popular?
    # Assistant: Python is popular xyz details .............
    # User: Summarize this in one sentence
    # Assistant: Python is popular xyz summary .............