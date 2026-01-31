from sentence_transformers import SentenceTransformer
from scipy.spatial import distance

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(texts):
    if isinstance(texts, str):
        texts = [texts]
    return model.encode(texts)

def create_product_text(product):
    features_str = "; ".join(product.get('features', []))
    return f"""Title: {product['title']}
Description: {product['short_description']}
Category: {product['category']}
Features: {features_str}"""

def find_n_closest(query_vector, embeddings, n=3):
    distances = []
    for index, embedding in enumerate(embeddings):
        dist = distance.cosine(query_vector, embedding)
        distances.append({"distance": dist, "index": index})
    distances_sorted = sorted(distances, key=lambda x: x["distance"])
    return distances_sorted[0:n]

# --- SAMPLE DATA ---
products = [
    {"title": "Smartphone X1", "short_description": "Flagship 5G phone.", "category": "Electronics", "features": ["AI camera", "5G"]},
    {"title": "Smartphone Y2", "short_description": "Budget 4G phone.", "category": "Electronics", "features": ["Large battery"]},
    {"title": "Laptop Pro", "short_description": "High-end workstation.", "category": "Electronics", "features": ["M2 Chip"]},
    {"title": "Tablet Z", "short_description": "Portable touch device.", "category": "Electronics", "features": ["Stylus included"]}
]

last_product = {
    "title": "Smartphone X1",
    "short_description": "Flagship 5G phone.",
    "category": "Electronics",
    "features": ["AI camera", "5G"]
}


# Combine the features for last_product and each product in products
last_product_text = create_product_text(last_product)
product_texts = [create_product_text(product) for product in products]

# Embed last_product_text and product_texts
last_product_embeddings = create_embeddings(last_product_text)[0]
# Note: removed [0] here so we keep the full list of embeddings to search through
product_embeddings = create_embeddings(product_texts) 

# Find the three smallest cosine distances and their indexes
hits = find_n_closest(last_product_embeddings, product_embeddings, n=3)

print("Recommendations based on last visit:")
for hit in hits:
  product = products[hit['index']]
  print(f"- {product['title']} (Distance: {hit['distance']:.4f})")