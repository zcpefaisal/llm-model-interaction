import os
from openai import OpenAI

# Initialize the client
# Use an environment variable for security, or replace the placeholder
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<OPENAI_API_TOKEN>"))

# Define the user request
user_request = "Can you recommend a good restaurant in Berlin?"

# Define the messages (System Message + User Message)
messages = [
    {
        "role": "system", 
        "content": "Assess the question first: if it is allowed, provide a reply, otherwise provide the message: 'Apologies, but I am not allowed to discuss this topic.'"
    },
    {"role": "user", "content": user_request},
]

try:
    # Run the completion
    print("Sending request to OpenAI...")
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=messages
    )

    # Extract and print the content
    content = response.choices[0].message.content
    print("\n--- AI Response ---")
    print(content)

except Exception as e:
    print(f"An error occurred: {e}")