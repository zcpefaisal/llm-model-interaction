import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Ensure the PDF file is in the same directory as this script
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')
data = loader.load()

# Split the document into smaller chunks
# chunk_size: maximum characters per chunk
# chunk_overlap: number of characters to carry over from the previous chunk to maintain context
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
docs = splitter.split_documents(data) 

# Initialize the OpenAI Embedding function
# Replace 'your-api-key-here' with your actual OpenAI API Key
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
embedding_function = OpenAIEmbeddings(model='text-embedding-3-small')

# Ingest documents into a persistent Chroma vector database
# This will create a folder named 'chroma_db' on your local machine to store the data
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_function,
    persist_directory="./chroma_db"
)

# Configure the vector store as a retriever
# search_type="similarity": finds the most mathematically similar text chunks
# k: 3 means it will return the top 3 most relevant documents for your query
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

print("Vector database created and retriever is ready for use!")

# Test the retriever with a query
query = "What are the tradeoffs of RAG vs Fine-tuning?"
results = retriever.get_relevant_documents(query)
for doc in results:
    print(f"Content: {doc.page_content}\n")