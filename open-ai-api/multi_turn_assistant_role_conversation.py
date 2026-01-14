import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the variables from .env into the environment
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Retrieve the key using os.getenv
response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        # System: controls assistant behavior
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        
        # User: Example Question
        {"role": "user", "content": "Give me a quick summary of Bangladesh."},
        # Assistant: Example Answer
        {"role": "assistant", "content": "Bangladesh is a country in Asia that borders India and Myanmar. The capital city is Dhaka."},
        
        # we can add multiple assistant role for more clrification to model assistant

        # User(for assistant): Example Question
        {"role": "user", "content": "Give me a quick summary of Bhutan."},
        # Assistant: Example Answer
        {"role": "assistant", "content": "Bhutan is a country in Asia that borders India. The capital city is Thimphu."},
        # User(for assistant): Example Question
        {"role": "user", "content": "Give me a quick summary of Nepal."},
        # Assistant: Example Answer
        {"role": "assistant", "content": "Nepal is a country in Asia that borders India. The capital city is kathmandu."},



        # User: Real Question prompt
        {"role": "user", "content": "Give me a quick summary of Poland."}
    ]
)

print(response.choices[0].message.content)
# Now model will response for Greece based on following the Assistant example answer like Bangladesh 