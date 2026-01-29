import os
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<API_KEY_HERE>"))

# Sample products list
products = [
    {
        "title": "Smartphone X1",
        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",
        "price": 799.99,
        "category": "Electronics"
    },
    {
        "title": "EcoCoffee Maker",
        "short_description": "Sustainable drip coffee machine with reusable filters and energy-saving mode.",
        "price": 49.99,
        "category": "Appliances"
    }
]

# Extract descriptions for batch processing
product_descriptions = [product['short_description'] for product in products]

try:
    print(f"Generating embeddings for {len(products)} products...")
    # Create embeddings for the entire list in ONE call
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=product_descriptions
    )
    
    # Map the vectors back to product dictionaries
    # 'response.data' is a list of objects containing the embeddings in the same order
    for i, product in enumerate(products):
        product['embedding'] = response.data[i].embedding
        
    # Verify the first product
    first_item = products[0]
    print(f"\nSuccessfully embedded: {first_item['title']}")
    print(f"Vector size: {len(first_item['embedding'])} dimensions")
    print(f"Sample values: {first_item['embedding'][:3]}...")

except Exception as e:
    print(f"An error occurred: {e}")



# Create categories and embeddings lists using list comprehensions
categories = [product["category"] for product in products]
embeddings = [product["embedding"] for product in products]