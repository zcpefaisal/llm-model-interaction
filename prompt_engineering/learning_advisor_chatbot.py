
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



# Craft the system_prompt using the role-playing approach
system_prompt = "Act as a learning advisor who can interpret learner queries as described and provide the relevant textbook recommendations and the instruction to recommend beginner and advanced textbooks based on their background"

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)