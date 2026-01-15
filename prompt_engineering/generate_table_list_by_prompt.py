import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the variables from .env into the environment
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Retrieve the key using os.getenv

# Create a function which take my prompt and will give response
def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# prompt generate with specific column title
prompt = "generates a table of 10 books, with columns for Title, Author, and Year, that you should read given that you are a science fiction lover"
# Test the function with my prompt
response = get_response(prompt)
print(response)