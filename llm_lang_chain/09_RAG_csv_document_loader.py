from langchain_community.document_loaders.csv_loader import CSVLoader

# Create a document loader for fifa_countries_audience.csv
loader = CSVLoader('fifa_countries_audience.csv')

# Load the document
# This returns a list of 'Document' objects (one for each page)
data = loader.load()

# Explore the data
print(f"Total data Loaded: {len(data)}")
