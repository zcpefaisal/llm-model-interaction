from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import time


# ====================================== #
#       index creation in Pinecone       #
# ====================================== #

# Initialize Pinecone connection
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V") 
index_name = "my-index"

# Check if the index exists; if not, create it
if index_name not in pc.list_indexes().names():
    print(f"Creating a new index named '{index_name}'")
    pc.create_index(
        name=index_name,
        dimension=384, # Dimensions must match the model (all-MiniLM-L6-v2 uses 384)
        metric="cosine", # Use cosine similarity to find the "closest" vectors
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    # Wait a few seconds for the index to be fully initialized on the server
    time.sleep(10)






# =========================================== #
#       Upsert vector in Pinecone Index       #
# =========================================== #

# Connect to the specific index
index = pc.Index(index_name)

# Load the Embedding Model
# This model converts text sentences into lists of numbers (vectors)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Prepare sample data for the database
documents = [
    {"id": "vec1", "text": "Pinecone is a managed vector database for AI applications."},
    {"id": "vec2", "text": "To query a vector database, you need to provide an input embedding."},
    {"id": "vec3", "text": "Python is a popular language for data science and machine learning."},
    {"id": "vec4", "text": "The solar system has eight planets orbiting the sun."}
]

# Convert text to vectors and upload (Upsert) to Pinecone
vectors_to_upsert = []
for doc in documents:
    # Generate the embedding vector for the text
    embedding = model.encode(doc["text"]).tolist()
    
    # Store the ID, the Vector values, and the original text in Metadata
    vectors_to_upsert.append({
        "id": doc["id"], 
        "values": embedding, 
        "metadata": {"text": doc["text"]} # This allows us to retrieve the text later
    })

# Push the data to the Pinecone index
index.upsert(vectors=vectors_to_upsert)
print("Data successfully uploaded to the index!")






# =========================================== #
#       Query/Search from Pinecone Index      #
# =========================================== #

# search text
search_text = "How do I query a vector database?"

# Convert the search string into the same vector format
search_vector = model.encode(search_text).tolist()

# Query the index for the top 3 most similar results
query_result = index.query(
    vector=search_vector,
    top_k=3,              # Return the 2 best matches
    include_metadata=True # Ensure we get the text back from the metadata
)

# Print the results
print("Search Results")
for match in query_result['matches']:
    # The 'score' indicates similarity (closer to 1.0 is a better match)
    print(f"Score: {match['score']:.4f} | Text: {match['metadata']['text']}")