from datasets import load_dataset

# Load the "validation" split of the TIGER-Lab/MMLU-Pro dataset
# This will download the data to my local ~/.cache/huggingface directory
print("Loading dataset... this may take a moment.")
my_dataset = load_dataset("TIGER-Lab/MMLU-Pro", split="validation")

# Display dataset details (features, row count, etc.)
print("\n--- Dataset Summary ---")
print(my_dataset)

# Look at the first row to see the data structure
print("\n--- First Row Example ---")
print(my_dataset[0])




# Load the dataset
# We use '20220301.en' (English version) and 'streaming=True' 
# to avoid downloading 100GB to my hard drive.
wikipedia = load_dataset("wikipedia", "20220301.en", split="train", streaming=True)

# Filter the documents (from my sample)
# This checks each row's 'text' column for the word "football"
filtered = wikipedia.filter(lambda row: "football" in row["text"].lower())

# Create a sample dataset (from my sample)
# Since we are streaming, we use '.take(1)' instead of '.select(range(1))'
example = list(filtered.take(1))

# Display the result
if example:
    print(f"Match found! Title: {example[0]['title']}")
    print("-" * 30)
    print(example[0]["text"][:500] + "...") # Print first 500 characters
else:
    print("No matches found.")