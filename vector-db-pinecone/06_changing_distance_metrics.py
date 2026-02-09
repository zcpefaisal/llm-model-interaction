import os
from pinecone import Pinecone, ServerlessSpec

# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V") 

index_name = "my-dotproduct-index"

# Get the list of current indexes to check if ours exists
existing_indexes = [index.name for index in pc.list_indexes()]

# Create the index with the 'dotproduct' metric
if index_name not in existing_indexes:
    print(f"Creating index: {index_name}")
    pc.create_index(
        name=index_name,
        dimension=1536,         # Using 1536 to match OpenAI standard
        metric="dotproduct",    # This is the specific requirement for this exercise
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
    print("Index created successfully.")
else:
    print(f"Index '{index_name}' already exists.")

# List all indexes to verify the settings
# This will show you the name, dimension, and metric of all your indexes
index_list = pc.list_indexes()
print("Current Pinecone Indexes")
print(index_list)

# Verify the metric specifically for our new index
for index in index_list:
    if index.name == index_name:
        print(f"Verification: Index '{index.name}' is using the '{index.metric}' metric.")