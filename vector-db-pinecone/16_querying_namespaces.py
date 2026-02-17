from openai import OpenAI
from pinecone import Pinecone

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V")

index = pc.Index('my-index')


client = OpenAI(api_key="openai-key")
# Generate a real 1536-dimension vector
response = client.embeddings.create(
    input="How do I query namespace1?",
    model="text-embedding-3-small" # This model output is 1536
)
vector = response.data[0].embedding


# Generate the 384-dimension vector
# model = SentenceTransformer('all-MiniLM-L6-v2')
# query_text = "Finding specific data in namespace one"
# vector = model.encode(query_text).tolist()


# Note: We will use the same model used for upserting so the math matches!


# Query namespace1 with the vector provided
query_result = index.query(
    vector=vector,
    namespace="namespace1",
    top_k=3
)
print(query_result)