import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the variables from .env into the environment
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Retrieve the key using os.getenv

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
  ]  
  response = client.chat.completions.create(
    model="gpt-4o-mini", 
    messages= messages, 
    temperature=0
  )
  
  return response.choices[0].message.content

# Try the function with a system and user prompts of your choice 
response = get_response("You are an expert data scientest that can explain complex data science concept", "What is data science")
print(response)