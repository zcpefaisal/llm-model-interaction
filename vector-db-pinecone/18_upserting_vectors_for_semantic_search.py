import pandas as pd
import numpy as np
from uuid import uuid4
from openai import OpenAI
from pinecone import Pinecone


# Initialize Clients
# Replace with actual keys
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V")
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

index_name = 'new-pinecone-index'
index = pc.Index(index_name)

# Load your local CSV data
# Make sure squad_dataset.csv is in the same folder as this script
df = pd.read_csv('squad_dataset.csv').head(200)

batch_limit = 100

for batch in np.array_split(df, len(df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='squad_dataset')

print(" Upsert Complete")
print(index.describe_index_stats())
