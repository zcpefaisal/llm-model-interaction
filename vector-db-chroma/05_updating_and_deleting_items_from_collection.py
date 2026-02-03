import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# --- BACKEND SETUP ---
# Path to local database folder
client = chromadb.PersistentClient(path="./chroma_db")

# Sample data for the exercise
new_data = [
    {"id": "s1001", "document": "Title: Cats & Dogs (Movie)\nDescription: A look at the top-secret, high-tech espionage war going on between cats and dogs..."},
    {"id": "s6884", "document": 'Title: Goosebumps 2: Haunted Halloween (Movie)\nDescription: Three teens spend their Halloween trying to stop a magical book...'}
]


# Retrieve the collection
collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(
      model_name="text-embedding-3-small", 
      api_key=os.getenv("OPENAI_API_TOKEN")
  )
)

# Update or add the new documents
# Upsert = "Update" + "Insert"
collection.upsert(
    ids=[data["id"] for data in new_data],
    documents=[data["document"] for data in new_data]
)

# Delete the item with ID "s95"
collection.delete(ids=["s95"])

# Query to verify the updates (e.g., Cats & Dogs should now appear)
result = collection.query(
    query_texts=["films about dogs"],
    n_results=3
)
print(result)