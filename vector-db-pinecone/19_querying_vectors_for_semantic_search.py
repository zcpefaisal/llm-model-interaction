from openai import OpenAI
from pinecone import Pinecone

# Initialize Clients
# Ensure these match the keys you used in the Upsert step
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V")
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# Connect to the specific index
index = pc.Index('new-pinecone-index')

# Define the Natural Language Query
query = "What is in front of the Notre Dame Main Building?"

# Convert the Question into a Vector (Embedding)
# IMPORTANT: You must use the same model used for the database (text-embedding-3-small)
query_response = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
)

# Extract the numerical list (1536 dimensions)
query_emb = query_response.data[0].embedding

# Search the Specific Namespace
# We ask for the top 5 matches only within 'squad_dataset'
retrieved_docs = index.query(
    vector=query_emb,
    top_k=5,
    namespace='squad_dataset',
    include_metadata=True  # Add this to see the actual text answers!
)

# Print the Results
print(f"Search Results for: '{query}'")

for result in retrieved_docs['matches']:
    # Score represents cosine similarity (closer to 1.0 is better)
    print(f"ID: {result['id']} | Similarity Score: {round(result['score'], 2)}")
    
    # If you included metadata during upsert, you can see the text here:
    if 'metadata' in result:
        print(f"Text Snippet: {result['metadata'].get('text', 'No text found')[:200]}")
    print('-' * 40)