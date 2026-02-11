from pinecone import Pinecone

# Initialize Pinecone
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V") 
index_name = 'my-index'

# Connect to the index
index = pc.Index(index_name)

# Define your query vector (Matching the index dimension, e.g., 1536)
vector = [0.1] * 1536 

# Update the values of vector ID item2
index.update(
    id="item2", # previously inserted id
    values=vector
)

# Fetch vector ID item2
fetched_vector = index.fetch(
    ids=["item2"]
)
print(fetched_vector)