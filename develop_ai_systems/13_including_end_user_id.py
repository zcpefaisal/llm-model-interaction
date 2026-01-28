import os
import uuid
from openai import OpenAI

# Initialize the client
# It's safer to use environment variables for key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<OPENAI_API_TOKEN>"))

# Generate a unique ID (UUID version 4 is random)
unique_id = str(uuid.uuid4())
print(f"Generated Session ID: {unique_id}")

# Define conversation
messages = [
    {"role": "system", "content": "You are a helpful travel guide."},
    {"role": "user", "content": "Can you recommend a good restaurant in Berlin?"}
]

# Create the request with the 'user' parameter
try:
    response = client.chat.completions.create(  
        model="gpt-4o-mini", 
        messages=messages,
        # The 'user' field helps OpenAI detect and prevent abuse
        user=unique_id
    )

    # Print the response
    print("\n--- AI Response ---")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")