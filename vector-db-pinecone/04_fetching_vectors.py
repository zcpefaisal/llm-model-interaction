from pinecone import Pinecone

# Initialize the Pinecone client with API key
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V")

index = pc.Index('my-index')
ids = ['2', '5', '8']

# Fetch the vectors from the connected Pinecone index
fetched_vectors = index.fetch(ids)

# Extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors['vectors'][id]['metadata'] for id in ids]
print(metadatas)