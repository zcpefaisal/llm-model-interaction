from pinecone import Pinecone

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V")
index = pc.Index('my-index')


# Define Dummy Value for vector_set1 (e.g., Finance Data)
# Each vector is a dictionary with an 'id' and a 'values' list
vector_set1 = [
    {"id": "fin_1", "values": [0.1] * 1536, "metadata": {"genre": "finance"}},
    {"id": "fin_2", "values": [0.2] * 1536, "metadata": {"genre": "finance"}}
]

# Define Dummy Value for vector_set2 (e.g., Tech Data)
vector_set2 = [
    {"id": "tech_1", "values": [0.3] * 1536, "metadata": {"genre": "tech"}},
    {"id": "tech_2", "values": [0.4] * 1536, "metadata": {"genre": "tech"}}
]


# Upsert vector_set1 to namespace1
index.upsert(
  vectors=vector_set1,
  namespace='namespace1'
)

# Upsert vector_set2 to namespace2
index.upsert(
  vectors=vector_set2,
  namespace='namespace2'
)

# Print the index statistics
print(index.describe_index_stats())