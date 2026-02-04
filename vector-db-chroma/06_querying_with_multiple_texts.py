import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.PersistentClient(path="./chroma_db")


# Retrieve the collection with the proper embedding function
collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(
      model_name="text-embedding-3-small", 
      api_key=os.getenv("OPENAI_API_TOKEN")
  )
)

reference_ids = ['s999', 's1000']

# Retrieve the documents for the reference_ids
# .get() returns a dictionary; we extract the "documents" list
reference_texts = collection.get(ids=reference_ids)["documents"]

# Query using reference_texts
# This will return 3 results FOR EACH of the 2 reference texts
result = collection.query(
  query_texts=reference_texts,
  n_results=3
)

# Printing the nested list of results
print("Recommendations for each reference ID:")
print(result['documents'])


# Optional: Displaying them cleanly
for i, ref_id in enumerate(reference_ids):
    print(f"\nResults for {ref_id}:")
    for doc in result['documents'][i]:
        print(f" - {doc[:75]}...")