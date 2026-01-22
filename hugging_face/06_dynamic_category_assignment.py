from transformers import pipeline

# Define the input text
text = "AI-powered robots assist in complex brain surgeries with precision."

# Create the pipeline
# task="zero-shot-classification" tells the library how to use the model
print("Loading BART model (approx. 1.6GB)...")
classifier = pipeline(
    task="zero-shot-classification", 
    model="facebook/bart-large-mnli"
)

# Define custom categories
categories = ["politics", "science", "sports", "technology", "health"]

# Predict the output
# I can add multi_label=True if the text can belong to multiple categories
output = classifier(text, categories)

# Print the top results
print("\n--- Classification Results ---")
print(f"Text: \"{text}\"")
print("-" * 30)

# The 'labels' and 'scores' are returned in descending order of confidence
for label, score in zip(output['labels'][:3], output['scores'][:3]):
    print(f"Label: {label:12} | Confidence: {score:.2%}")