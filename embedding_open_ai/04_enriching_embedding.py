from sentence_transformers import SentenceTransformer

# Define the sample data (added so the code has something to process)
products = [
    {
        "title": "Smartphone X1",
        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",
        "price": 799.99,
        "category": "Electronics",
        "features": [
            "6.5-inch AMOLED display",
            "Quad-camera system with 48MP main sensor",
            "Face recognition and fingerprint sensor",
            "Fast wireless charging"
        ]
    }
]

# Define the embedding model/function
# This 'all-MiniLM-L6-v2' model is fast and runs easily on a standard PC
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(texts):
    return model.encode(texts)


# Define a function to combine the relevant features into a single string
def create_product_text(product):
  # we join the list with semicolons.
  features_str = "; ".join(product['features'])
  return f"""Title: {product['title']}
Description: {product['short_description']}
Category: {product['category']}
Features: {features_str}"""

# Combine the features for each product
product_texts = [create_product_text(product) for product in products]

# Create the embeddings from product_texts
product_embeddings = create_embeddings(product_texts)


# Optional: Print results to verify
print(f"Created {len(product_embeddings)} embeddings.")
print(f"Embedding shape: {product_embeddings[0].shape}")