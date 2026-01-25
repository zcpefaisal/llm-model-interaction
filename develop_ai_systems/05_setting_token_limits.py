import os
import tiktoken
from openai import OpenAI

# Initialize the OpenAI client
# It's safest to use an environment variable for API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<OPENAI_API_TOKEN>"))

# Define input message
input_message = {
    "role": "user", 
    "content": "I'd like to buy a shirt and a jacket. Can you suggest two color pairings for these items?"
}

# Use tiktoken to create the encoding for specific model
# 'gpt-4o-mini' uses the 'cl100k_base' encoding (or 'o200k_base' for newer versions)
encoding = tiktoken.encoding_for_model("gpt-4o-mini")

# Count the number of tokens in the message content
num_tokens = len(encoding.encode(input_message['content']))
print(f"Token count: {num_tokens}")

# Check the limit before sending the request
if num_tokens <= 100:
    print("Request within limit. Sending to OpenAI...")
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[input_message]
    )
    print("\n--- AI Response ---")
    print(response.choices[0].message.content)
else:
    print("Message exceeds token limit (100 tokens). Request cancelled.")