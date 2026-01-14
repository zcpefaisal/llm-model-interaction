import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the variables from .env into the environment
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Retrieve the key using os.getenv

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=150,

    # Utilizing systems messages
    # System: controls assistant behavior
    # User: instruct the assistant
    # Assistant: response to user instruction

    messages=[
        # System: controls
        {"role": "system", # controls assistant behavior
            "content": "You are a study planning assistant that creates plans for learning new skills."},
        # User: instruct
        {"role": "user",
            "content": "I want to learn to speak Dutch."}
    ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)