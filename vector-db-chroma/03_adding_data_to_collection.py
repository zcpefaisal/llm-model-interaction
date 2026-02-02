import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import csv

# --- BACKEND SETUP ---
client = chromadb.PersistentClient(path="./chroma_db")

# Optional: Delete the collection if it exists so can "recreate" it as per instructions
try:
    client.delete_collection(name="netflix_titles")
except:
    pass

# Mocking the data extraction logic from the problem statement
ids = ["s1", "s2"]
documents = [
    "Title: Dick Johnson Is Dead (Movie)\nDescription: Kirsten Johnson stages death...\nCategories: Documentaries",
    "Title: Blood & Water (TV Show)\nDescription: A teen suspects a swimming star...\nCategories: International TV Shows"
]


# Recreate the netflix_titles collection
collection = client.create_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key=os.getenv("OPENAI_API_TOKEN"))
)

# Add the documents and IDs to the collection
collection.add(ids=ids, documents=documents)

# Print the collection size and first ten items
print(f"No. of documents: {collection.count()}")
print(f"First ten documents: {collection.peek()}")