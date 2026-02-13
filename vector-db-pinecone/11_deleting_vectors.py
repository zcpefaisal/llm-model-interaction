from pinecone import Pinecone

# Initialize Pinecone
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V") 
index_name = 'my-index'

# Connect to the index
index = pc.Index(index_name)


# Delete vectors
index.delete(
    ids=['item1', 'item2']
)

# Retrieve metrics of the connected Pinecone index
print(index.describe_index_stats())