import os
import json
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<OPENAI_API_TOKEN>"))

# Define the helper function
def get_response(messages, tools):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    return response

# Define the first function (Unit Converter)
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "convert_units",
            "description": "Convert kilometers to miles",
            "parameters": {
                "type": "object",
                "properties": {
                    "km": {"type": "number", "description": "The distance in km"}
                }
            }
        }
    }
]

# Append the second function (Review Reply) - From snippet
function_definition.append({
    'type': 'function', 
    'function': {
        'name': "reply_to_review", 
        "description": "return the additional message responding to the customer review",
        "parameters": {
            'type': "object", 
            'properties': {
                'reply': {
                    "type": "string",
                    "description": "reply to post on their review platform"
                }
            }
        }
    }
})

# Create a prompt that triggers BOTH functions
messages = [{
    "role": "user", 
    "content": "Convert 50km to miles and draft a thank you reply to a 5-star review."
}]

# Run and Process
response = get_response(messages, function_definition)
tool_calls = response.choices[0].message.tool_calls

print(f"Total Tool Calls: {len(tool_calls)}\n")

for tool_call in tool_calls:
    print(f"Function: {tool_call.function.name}")
    print(f"Arguments: {tool_call.function.arguments}")
    print("-" * 20)