import os
import json
from openai import OpenAI

# Initialize the client
# Ensure API key is set as an environment variable or replace below
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<API_KEY_HERE>"))

# Text input to be embedded
text_to_embed = "Creating OpenAI embeddings for test purpose"

try:
    print(f"Generating embeddings for: '{text_to_embed}'")
    # Create the embedding request
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text_to_embed
    )

    # Convert the response into a dictionary for inspection
    response_dict = response.model_dump()
    
    # Extract the actual embedding vector
    # This is a list of 1,536 floating-point numbers
    embedding_vector = response_dict['data'][0]['embedding']

    print("\n--- Embedding Summary ---")
    print(f"Model Used: {response_dict['model']}")
    print(f"Vector Length: {len(embedding_vector)}")
    print(f"First 5 numbers in vector: {embedding_vector[:5]}")

    # Extract the total_tokens from response_dict
    print(response_dict['usage']['total_tokens'])
    
except Exception as e:
    print(f"An error occurred: {e}")


