import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction


# Create a persistant client
# Note: In a local environment, can pass a path like path="./my_vectordb" 
# to save data to a specific folder.
client = chromadb.PersistentClient()

# Create a netflix_title collection using the OpenAI Embedding function
collection = client.create_collection(
    name="netflix_titles",
    embedding_function=OpenAIEmbeddingFunction(
        model_name="text-embedding-3-small", 
        api_key=os.getenv("OPENAI_API_TOKEN")
    )
)

# List the collections
print(client.list_collections())