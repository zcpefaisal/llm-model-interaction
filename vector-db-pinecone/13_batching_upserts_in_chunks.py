import itertools
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# Helper Function from previous step
def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))

# Initialize Pinecone and Model
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V") 
index = pc.Index('my-index')
model = SentenceTransformer('all-MiniLM-L6-v2')

# Prepare a large set of dummy data (simulating 'vectors' variable)
raw_texts = [f"This is document number {i}" for i in range(1, 251)] # 250 documents
vectors = []

print("Encoding texts into vectors")
for i, text in enumerate(raw_texts):
    vectors.append({
        "id": f"vec_{i}",
        "values": model.encode(text).tolist(),
        "metadata": {"text": text, "year": 2024}
    })

# Upsert vectors in batches of 100
print("Starting batched upsert...")
for chunk in chunks(vectors, batch_size=100):
    index.upsert(vectors=chunk) 
    print(f"Uploaded a chunk of {len(chunk)} vectors.")

# Print index statistics
# This confirms the total number of vectors currently in the index
print("Index Statistics")
print(index.describe_index_stats())