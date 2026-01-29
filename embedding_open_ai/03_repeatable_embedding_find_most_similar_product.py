import os
import numpy as np
from scipy.spatial import distance
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<API_KEY>"))

# Sample data
products = [
    {"title": "Organic Bar Soap", "short_description": "Handmade lavender scented soap bar."},
    {"title": "Power Drill", "short_description": "Cordless 18V drill for home improvement."},
    {"title": "Liquid Cleanser", "short_description": "Gentle soap for sensitive skin."}
]

# Define the reusable embedding function
def create_embeddings(texts):
    # Ensure input is a list even if a single string is passed
    if isinstance(texts, str):
        texts = [texts]
        
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [data.embedding for data in response.data]

# Pre-embed the product catalog
# In a real app, do this once and save it to a database
print("Encoding product catalog...")
descriptions = [p['short_description'] for p in products]
product_embeddings = create_embeddings(descriptions)

for i, product in enumerate(products):
    product['embedding'] = product_embeddings[i]

# Perform Semantic Search
search_text = "cleaning soap"
print(f"Searching for: '{search_text}'")
search_embedding = create_embeddings(search_text)[0]

distances = []
for product in products:
    # Calculate how 'far' the search is from each product
    dist = distance.cosine(search_embedding, product["embedding"])
    distances.append(dist)

# Find and print the result
min_dist_ind = np.argmin(distances)
best_match = products[min_dist_ind]

print(f"\nBest Match: {best_match['title']}")
print(f"Description: {best_match['short_description']}")
print(f"Cosine Distance: {distances[min_dist_ind]:.4f}")