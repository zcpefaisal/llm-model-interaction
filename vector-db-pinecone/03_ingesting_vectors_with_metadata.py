from pinecone import Pinecone
import random

PINECONE_API_KEY = "pcsk_5xc8Tq<OPENAI_TOKEN>4mrMv9V"
pc = Pinecone(api_key=PINECONE_API_KEY)

# Mocking the 'vectors' list to match required structure
# Ensure these have the same dimensions as index (e.g., 1536)
vectors = [
    {
        "id": str(i),
        "values": [random.random() for _ in range(1536)],
        "metadata": {"genre": "action", "year": 2024}
    } for i in range(5)
]

# Connect to index
index = pc.Index("datacamp-index")

# Ingest the vectors and metadata
# Upsert will insert new records or update them if the IDs already exist
index.upsert(
    vectors=vectors
)

# Print the index statistics (total vector count, namespaces, etc.)
print(index.describe_index_stats())