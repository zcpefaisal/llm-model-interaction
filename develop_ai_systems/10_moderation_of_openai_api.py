import os
from openai import OpenAI

# Initialize the client
# Best practice: set the environment variable OPENAI_API_KEY
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<YOUR_API_KEY_HERE>"))

# Define the message to check
message = "Can you show some example sentences in the past tense in French?"

# Use the moderation API
# This checks for harmful content across several categories
print("Checking moderation...")
moderation_response = client.moderations.create(input=message)

# Extract results
result = moderation_response.results[0]
is_flagged = result.flagged
categories = result.categories

# Handle the response
if is_flagged:
    print("Warning: Content violates OpenAI policies.")
    # Show only the categories that were flagged as True
    flagged_categories = [cat for cat, value in categories if value]
    print(f"Violations: {flagged_categories}")
else:
    print("Content is safe. No policy violations detected.")
    # Example of accessing a specific category
    print(f"Hate speech check: {categories.hate}")