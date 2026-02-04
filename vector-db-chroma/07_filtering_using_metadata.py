import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.PersistentClient(path="./chroma_db")

# Retrieve the netflix_titles collection
collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(
      model_name="text-embedding-3-small", 
      api_key=os.getenv("OPENAI_API_TOKEN")
  )
)

reference_texts = ["children's story about a car", "lions"]

# Query results using reference_texts with metadata filters
result = collection.query(
  query_texts=reference_texts,
  n_results=2,
  # Filter for titles with a G rating released before 2019
  where={
    "$and": [
        {"rating": {"$eq": "G"}},         # Matches the 'rating' field exactly
        {"release_year": {"$lt": 2019}}   # Matches 'release_year' less than 2019
    ]
  }
)

print(result['documents'])