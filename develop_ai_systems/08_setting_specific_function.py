import os
import json
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<OPENAI_API_TOKEN>"))

# Define the schema for review extraction
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_review_info",
            "description": "Extract structured info from a customer review",
            "parameters": {
                "type": "object",
                "properties": {
                    "sentiment": {"type": "string", "enum": ["positive", "negative"]},
                    "product_mentioned": {"type": "string"},
                    "star_rating": {"type": "integer", "minimum": 1, "maximum": 5}
                },
                "required": ["sentiment", "product_mentioned", "star_rating"]
            }
        }
    }
]

# Define the message listing (A messy customer review)
message_listing = [{
    "role": "user", 
    "content": "I bought the UltraClean Vacuum last week. It works great, definitely 5 stars!"
}]

# Create the request with forced tool_choice
# This ensures the model calls 'extract_review_info' specifically
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=message_listing,

    tools=function_definition,
    # Forced Tool Choice
    tool_choice={
        "type": "function",
        "function": {"name": "extract_review_info"}
    }
)

# Extract and print the arguments
tool_call = response.choices[0].message.tool_calls[0]
arguments = json.loads(tool_call.function.arguments)

print("\n--- Forced Tool Extraction Result ---")
print(json.dumps(arguments, indent=2))