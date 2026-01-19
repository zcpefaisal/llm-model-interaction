
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

base_system_prompt = """You are the customer support chatbot for an e-commerce platform specializing in electronics. Your role is to assist customers with inquiries, order tracking, and troubleshooting common issues related to their purchases. Your primary audience consists of tech-savvy individuals who are interested in purchasing electronic gadgets. Maintain a professional and user_friendly tone in your responses.
"""

# Define the order number condition
order_number_condition = "What is your order number? if they submitted a query about an order without specifying an order number"

# Define the technical issue condition
technical_issue_condition = "I'm sorry to hear about your issue with ...  if the user is reporting a technical issue"

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)