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


function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""modify the delimited with triple backtricks function according to the specified requirements: test if the inputs to the functions are positive, and if not, display appropriate error messages, otherwise return the area and perimeter of the rectangle.
```{function}```
"""

response = get_response(prompt)
print(response)


# Craft a chain-of-thought prompt that asks the model to explain what the function does
chain_of_thought_prompt = "explain provided delimited with triple backtricks function step by step of chain-of-thought prompt that asks the model to explain the ```{function}```"
 
response_chain_of_thought_prompt = get_response(chain_of_thought_prompt)
print(response_chain_of_thought_prompt)