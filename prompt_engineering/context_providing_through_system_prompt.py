
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


# Define the system prompt
system_prompt = f"""Act as a chatbot to be a customer service chatbot for a delivery service that responds in a gentle way and point to a service description. Some information provided in delimited of triple backtricks ```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)