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

# Create the instructions
instructions = "directions to infer the language and the number of sentences of the given delimited ```{text_input}```; then if the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title"

# Create the output format
output_format = "text, language, number of sentences, and title, each on a separate line,and ensure to use 'Text:', 'Language:', and 'Title:' as prefixes for each line"

# Input get from user
text_input = input("")

prompt = instructions + output_format + f"```{text_input}```"
response = get_response(prompt)
print(response)