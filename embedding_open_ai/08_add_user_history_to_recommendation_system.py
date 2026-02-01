import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial import distance

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(texts):
    if isinstance(texts, str):
        texts = [texts]
    return model.encode(texts)

def create_product_text(product):
    features_str = "; ".join(product.get('features', []))
    return f"Title: {product['title']}\nDescription: {product['short_description']}\nCategory: {product['category']}\nFeatures: {features_str}"

def find_n_closest(query_vector, embeddings, n=3):
    distances = []
    for index, embedding in enumerate(embeddings):
        dist = distance.cosine(query_vector, embedding)
        distances.append({"distance": dist, "index": index})
    distances_sorted = sorted(distances, key=lambda x: x["distance"])
    return distances_sorted[0:n]

# --- SAMPLE DATA - USER HISTORY---
user_history = [
    {"title": "Smartphone X1", "short_description": "Flagship 5G phone.", "category": "Electronics", "features": ["5G"]},
    {"title": "Bluetooth Speaker", "short_description": "Portable audio.", "category": "Electronics", "features": ["Waterproof"]}
]

# --- SAMPLE DATA - PRODUCT---
products = [
    {"title": "Smartphone X1", "short_description": "Flagship 5G phone.", "category": "Electronics", "features": ["5G"]},
    {"title": "Smartphone Y2", "short_description": "Budget 4G phone.", "category": "Electronics", "features": ["Large battery"]},
    {"title": "Laptop Pro", "short_description": "High-end workstation.", "category": "Electronics", "features": ["M2 Chip"]},
    {"title": "Wireless Earbuds", "short_description": "Noise cancelling audio.", "category": "Electronics", "features": ["ANC"]}
]


# Prepare and embed the user_history, and calculate the mean embeddings
history_texts = [create_product_text(article) for article in user_history]
history_embeddings = create_embeddings(history_texts)
mean_history_embeddings = np.mean(history_embeddings, axis=0)

# Filter products to remove any in user_history
products_filtered = [p for p in products if p not in user_history]

# Combine product features and embed the resulting texts
product_texts = [create_product_text(product) for product in products_filtered]
product_embeddings = create_embeddings(product_texts)

hits = find_n_closest(mean_history_embeddings, product_embeddings)

print("Personalized Recommendations:")
for hit in hits:
  product = products_filtered[hit['index']]
  print(f"- {product['title']}")

