import os
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<OPENAI_API_TOKEN>"))

# Define the helper function (from sample)
def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content

# Sample data (measurements in km)
measurements = [10, 21, 42.2, 100]

# Initialize message list with a System Role
messages = [{
    "role": "system",
    "content": "Convert each measurement, given in kilometers, into miles, and reply with a table of all measurements."
}]

# Add measurements to the messages list
# Note: Using a standard loop is generally preferred over list comprehension for side effects
for i in measurements:
    messages.append({"role": "user", "content": f"{i} km"})

# Predict and Print
print("Calculating conversions...")
response_text = get_response(messages)

print("--- Resulting Table ---")
print(response_text)