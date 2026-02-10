from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V") 
index_name = 'my-index'

# Connect to the index
index = pc.Index(index_name)

# This ensures your filter actually has something to find
dummy_vectors = [
    {
        "id": "item1", 
        "values": [0.1] * 1536, 
        "metadata": {"year": 2024, "text": "Relevant 2024 data"}
    },
    {
        "id": "item2", 
        "values": [0.2] * 1536, 
        "metadata": {"year": 2023, "text": "Old 2023 data"}
    }
]
index.upsert(vectors=dummy_vectors)

# Define your query vector (Matching the index dimension, e.g., 1536)
vector = [0.1] * 1536 

# Execute the Filtered Query
# $eq stands for "equals"
query_result = index.query(
    vector=vector,
    filter={
        "year": {"$eq": 2024}  # Only looks at 2024 records
    },
    top_k=1,                   # Retrieve only the MOST similar
    include_metadata=True      # Helpful to see the year in the output
)

print("Query Result with 2024 Filter")
print(query_result)