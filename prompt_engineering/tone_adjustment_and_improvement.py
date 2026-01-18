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


sample_text = """Introducing our latest collection of premium leather handbags. Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. With a variety of designs and colors, our handbags are perfect for any occasion. Shop now and experience the epitome of style and quality.
"""
# Craft a prompt to change the tone
prompt_tone = f"""Transforms the email text delimited with triple backtricks changing its tone to be professional, positive, and user-centric. ```{sample_text}```
"""

# Craft a prompt to transform the text
prompt_improvement = f"""Writing improvement of delimited with triple backtricks text in multi step, first step will proofreads the text without changing its structure, and second step will adjusts its tone to be formal and friendly. ```{sample_text}``` 
"""

response_tone = get_response(prompt_tone)
response_improvement = get_response(prompt_improvement)

print("Original Text: \n", sample_text)
print("After tone adjustment: \n", response_tone)
print("After improvement: \n", response_improvement)
