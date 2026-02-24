from openai import OpenAI
from pinecone import Pinecone

# Initialize Clients
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V")
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")


index = pc.Index('new-pinecone-index')

# Define the retrieve function
def retrieve(query, top_k, namespace, emb_model):
    # Encode the input query using OpenAI
    query_response = client.embeddings.create(
        input=query,
        model=emb_model
    )
    
    query_emb = query_response.data[0].embedding
    
    # Query the index (ensure include_metadata is True to get text/urls)
    docs = index.query(
        vector=query_emb, 
        top_k=top_k, 
        namespace=namespace, 
        include_metadata=True
    )
    
    retrieved_docs = []
    sources = []
    
    for doc in docs['matches']:
        # Extract the text and source info from the metadata
        retrieved_docs.append(doc['metadata']['text'])
        sources.append((doc['metadata']['title'], doc['metadata']['url']))
    
    return retrieved_docs, sources

# Test the function locally
# Note: Ensure you've already upserted data to 'youtube_rag_dataset' 
try:
    documents, sources = retrieve(
      query="How to build next-level Q&A with OpenAI",
      top_k=3,
      namespace='youtube_rag_dataset',
      emb_model="text-embedding-3-small"
    )

    print("Retrieved Documents")
    for i, doc in enumerate(documents):
        print(f"Result {i+1}: {doc[:150]}")
        print(f"Source: {sources[i][0]} ({sources[i][1]})")

except Exception as e:
    print(f"Error: {e}. Check if your index name and namespace are correct.")