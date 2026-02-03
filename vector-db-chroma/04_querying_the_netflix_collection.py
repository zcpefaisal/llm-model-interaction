import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# Ensure the path matches where saved the database in the previous step
client = chromadb.PersistentClient(path="./chroma_db")

# Retrieve the netflix_titles collection
collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(
      model_name="text-embedding-3-small", 
      api_key=os.getenv("OPENAI_API_TOKEN")
  )
)

# Query the collection for "films about dogs"
result = collection.query(
  query_texts=["films about dogs"],
  n_results=3
)

print(result)

# Optional: Cleaner output for console
if result['documents']:
    print("\nTop 3 Dog Film Recommendations:")
    for i, doc in enumerate(result['documents'][0]):
        print(f"{i+1}. {doc[:100]}...")