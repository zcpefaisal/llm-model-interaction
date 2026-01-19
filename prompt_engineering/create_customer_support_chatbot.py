
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


# Define the purpose of the chatbot
chatbot_purpose = "You are a customer support chatbot for an e-commerce company specializing in electronics and is there to assist with inquiries, order tracking, and troubleshooting"

# Define audience guidelines
audience_guidelines = " the target audience as tech-savvy individuals interested in purchasing electronic gadgets."

# Define tone guidelines
tone_guidelines = "Your tone for interactions and specify the intended audience as a professional and user-friendly"

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(system_prompt, "My new headphones aren't connecting to my device")
print(response)