import os
import json
import requests
from openai import OpenAI

# Initialize Clients
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<YOUR_OPENAI_TOKEN>"))
AIRPORT_API_KEY = api_key=os.environ.get("AIRPORT_API_KEY", "<YOUR_AIRPORT_API_KEY>")

# Define the local Python function that calls the External API
def get_airport_info(airport_code):
    url = f"https://api.api-ninjas.com/v1/airports?iata={airport_code}"
    response = requests.get(url, headers={'X-Api-Key': AIRPORT_API_KEY})
    
    if response.status_code == 200:
        return response.text  # Returns raw JSON from the external API
    else:
        return "Error: Could not retrieve airport information."

# Define the tool for OpenAI
tools = [{
    "type": "function",
    "function": {
        "name": "get_airport_info",
        "description": "Provide information about an airport using its IATA code",
        "parameters": {
            "type": "object", 
            "properties": {
                "airport_code": {
                    "type": "string",
                    "description": "The IATA airport code (e.g., LHR, JFK)"
                },
            },
            "required": ["airport_code"]
        }
    }
}]

# First Call: OpenAI detects the need for a tool
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an aviation assistant."},
        {"role": "user", "content": "I'm planning to land in JFK airport and need info."}
    ],
    tools=tools
)

# Handling the response and calling the External API
if response.choices[0].finish_reason == "tool_calls":
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    
    # Extract arguments and call our local function
    args = json.loads(tool_call.function.arguments)
    print(f"AI requested function: {function_name} with args: {args}")
    
    if function_name == "get_airport_info":
        api_result = get_airport_info(args['airport_code'])
        print(f"External API Result: {api_result}")
else:
    print(response.choices[0].message.content)