import pandas as pd
import numpy as np
from uuid import uuid4
from openai import OpenAI
from pinecone import Pinecone

# Initialize Clients
# Use your actual API keys here
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V")
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

index = pc.Index('new-pinecone-index')

# Load the YouTube data
# Ensure you have 'youtube_rag_data.csv' in your project folder
youtube_df = pd.read_csv('youtube_rag_data.csv')

batch_limit = 100

print(f"Total rows to process: {len(youtube_df)}")

# Batch processing loop
# We divide the dataframe into manageable chunks
for batch in np.array_split(youtube_df, max(1, len(youtube_df) // batch_limit)):
    
    # Extract metadata including URL and Published date
    metadatas = [{
      "text_id": str(row['id']),
      "text": row['text'],
      "title": row['title'],
      "url": row['url'],
      "published": str(row['published'])} for _, row in batch.iterrows()]
    
    texts = batch['text'].tolist()
    
    # Generate unique IDs for each transcript chunk
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Create Embeddings (1536 dimensions)
    response = client.embeddings.create(
        input=texts, 
        model="text-embedding-3-small"
    )
    
    # Convert response into a list of arrays
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert to the 'youtube_rag_dataset' namespace
    # Note: We zip IDs, Embeddings, and Metadata together
    index.upsert(
        vectors=list(zip(ids, embeds, metadatas)), 
        namespace='youtube_rag_dataset'
    )
    
    print(f"Uploaded batch of {len(batch)} items...")

# Verify the upload
print("Final Index Statistics")
print(index.describe_index_stats())