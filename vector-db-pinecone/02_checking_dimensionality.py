from pinecone import Pinecone, ServerlessSpec

# --- CONFIGURATION ---
# Replace with actual Pinecone API key
PINECONE_API_KEY = "pcsk_5xc8Tq<OPENAI_TOKEN>4mrMv9V"

# 1. Initialize the Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Optional: Clean up existing index to ensure fresh creation
if "datacamp-index" in [i.name for i in pc.list_indexes()]:
    pc.delete_index("datacamp-index")

# Create Pinecone index
pc.create_index(
    name="datacamp-index", 
    dimension=1536, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)

# Mocking the vectors list for local execution (8 vectors of length 1536)
import random
vectors = [
    {
        "id": str(i),
        "values": [random.random() for _ in range(1536)],
        "metadata": {"genre": "action", "year": 2024}
    } for i in range(8)
]

# Check that each vector has a dimensionality of 1536
# This returns a list of Booleans: [True, True, ...]
vector_dims = [len(vector['values']) == 1536 for vector in vectors]

# all() returns True only if every single item in the list is True
print(f"All vectors match dimension 1536: {all(vector_dims)}")