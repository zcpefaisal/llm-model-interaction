import os
from openai import OpenAI

# Initialize the client
# Replace '<OPENAI_API_TOKEN>' with actual key or use an environment variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<OPENAI_API_TOKEN>"))

# Define the message (missing from original snippet)
message = {"role": "user", "content": "Hello! How are you?"}

# Use the try-except statement for robust error handling
try:
    print("Sending request to OpenAI...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[message]
    )
    # Print the response content
    print("\n--- AI Response ---")
    print(response.choices[0].message.content)

# Specifically catch authentication errors (wrong key, expired key)
except OpenAI.AuthenticationError:
    print("Error: Please double check authentication key and try again.")
    print("The one provided is not valid or has been revoked.")

# Good practice: Catch other potential API errors
except Exception as e:
    print(f"An unexpected error occurred: {e}")