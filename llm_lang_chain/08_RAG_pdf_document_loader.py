from langchain_community.document_loaders import PyPDFLoader

# Initialize the loader
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')

# Load the document
# This returns a list of 'Document' objects (one for each page)
data = loader.load()

# Explore the data
print(f"Total Pages Loaded: {len(data)}")

# Print the content of the first page
print("\n--- Content of Page 1 ---")
print(data[0].page_content[:50]) # First 50 characters

# Print the metadata
print("\n--- Metadata of Page 1 ---")
print(data[0].metadata)