from pinecone import Pinecone, ServerlessSpec

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V")

# Create Pinecone index
pc.create_index(
    name='new-pinecone-index', 
    dimension=1536,
    spec=ServerlessSpec(cloud='aws', region='us-east-1')
)

# Connect to index and print the index statistics
index = pc.Index("new-pinecone-index")
print(index.describe_index_stats())