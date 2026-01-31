from sentence_transformers import SentenceTransformer
from scipy.spatial import distance

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(texts):
    # If a single string is passed, wrap it in a list
    if isinstance(texts, str):
        texts = [texts]
    return model.encode(texts)

def find_n_closest(query_vector, embeddings, n=3):
    distances = []
    for index, embedding in enumerate(embeddings):
        # Using distance.cosine as per previous logic
        dist = distance.cosine(query_vector, embedding)
        distances.append({"distance": dist, "index": index})
    distances_sorted = sorted(distances, key=lambda x: x["distance"])
    return distances_sorted[0:n]

# Sample data to make the search work
products = [
    {"title": "Smartphone X1", "short_description": "A mobile device.", "category": "Electronics", "features": ["5G"]},
    {"title": "Laptop Pro", "short_description": "High performance computer.", "category": "Electronics", "features": ["16GB RAM"]},
    {"title": "Office Chair", "short_description": "Ergonomic seating.", "category": "Furniture", "features": ["Lumbar support"]},
    {"title": "Gaming Desktop", "short_description": "Powerful gaming computer.", "category": "Electronics", "features": ["RTX 4090"]},
    {"title": "Bluetooth Speaker", "short_description": "Portable audio.", "category": "Electronics", "features": ["Waterproof"]}
]

# Pre-calculate embeddings for the products (from first exercise)
product_texts = [f"Title: {p['title']} Description: {p['short_description']}" for p in products]
product_embeddings = create_embeddings(product_texts)


# Create the query vector from query_text
query_text = "computer"
query_vector = create_embeddings(query_text)[0]

# Find the five closest distances
hits = find_n_closest(query_vector, product_embeddings, 5)

print(f'Search results for "{query_text}"')
for hit in hits:
  # Extract the product at each index in hits
  product = products[hit['index']]
  print(product["title"])

