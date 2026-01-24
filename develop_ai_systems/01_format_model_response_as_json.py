import os
import json
from openai import OpenAI

# Initialize the client
# If set the environment variable OPENAI_API_KEY, 
# I can just use: client = OpenAI()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<API_KEY_HERE>"))

# Create the request
# Note: JSON mode (json_object) requires the word "JSON" in message prompt.
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user", 
            "content": "I have these notes: The Beholders by Hester Musson, The Mystery Guest by Nita Prose. "
                       "Please organize the titles and authors in a JSON file."
        }
    ],
    response_format={"type": "json_object"}
)

# Parse and Print the response
# The output comes as a string, so we use json.loads to turn it into a Python dictionary
raw_content = response.choices[0].message.content
json_data = json.loads(raw_content)

print(json.dumps(json_data, indent=2))