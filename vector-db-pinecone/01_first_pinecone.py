from pinecone import Pinecone, ServerlessSpec

# Replace with actual API key from the Pinecone dashboard
PINECONE_API_KEY = "pcsk_5xc8Tq...V" 

# 1. Initialize the Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)


# Delete the index if it exists (useful for re-running scripts)
# Note: Checking if it exists first prevents errors
if "my-first-index" in [i.name for i in pc.list_indexes()]:
    pc.delete_index("my-first-index")

# Create Pinecone index
pc.create_index(
    name="my-first-index",
    dimension=256,
    metric="cosine",  # Metric is often required; cosine is standard for text
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

# Verify it was created
print(pc.describe_index("my-first-index"))