from transformers import pipeline

# Create the pipeline
# This downloads a ~440MB model to the local cache (~/.cache/huggingface)
print("Loading QNLI model...")
classifier = pipeline(
    task="text-classification", 
    model="cross-encoder/qnli-electra-base"
)

# Define inputs
# Format: "Question, Passage/Sentence"
input_data = "Where is the capital of France?, Brittany is known for its stunning coastline."

# Predict the output
output = classifier(input_data)

# Print results
print("\n--- QNLI Result ---")
print(f"Input: {input_data}")
print(f"Result: {output}")

