import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the variables from .env into the environment
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Retrieve the key using os.getenv

messages = [
    {"role": "system", "content": "You are a helpful math tutor that speaks concisely."},
    {"role": "user", "content": "Explain what pi is."}
]

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
print(messages) # [{'role': 'system', 'content': 'You are a helpful math tutor that speaks concisely.'}, {'role': 'user', 'content': 'Explain what pi is.'}, {'role': 'assistant', 'content': "Pi (π) is a mathematical constant representing the ratio of a circle's circumference to its diameter. It is an irrational number, meaning it cannot be expressed as a simple fraction, and its decimal representation goes on forever without repeating. The approximate value of pi is 3.14159. Pi is widely used in geometry, trigonometry, and various fields of science and engineering."}]
