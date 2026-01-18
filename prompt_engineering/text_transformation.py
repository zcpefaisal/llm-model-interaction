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


marketing_message = """Introducing our latest collection of premium leather handbags. Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. With a variety of designs and colors, our handbags are perfect for any occasion. Shop now and experience the epitome of style and quality.
"""
# Craft a prompt that translates
prompt_translates = f"""Translates the delimited with triple backtricks text from English language to French, Spanish, and Japanese language ```{marketing_message}```
"""
 
response = get_response(prompt_translates)

print("English:", marketing_message)
print(response)
