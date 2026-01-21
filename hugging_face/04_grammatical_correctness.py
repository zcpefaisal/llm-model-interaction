from transformers import pipeline

# Initialize the pipeline
# This will download the model to my cache (~/.cache/huggingface) on the first run
print("Loading model... this might take a minute.")
# Create a pipeline for grammar checking

grammar_checker = pipeline(
    "text-classification", 
    model="abdulmatinomotoso/English_Grammar_Checker"
)

# Define the text to check
input_text = "I will walk dog"

# Get the prediction
output = grammar_checker(input_text)

# Display the result in a readable format
print("\n--- Result ---")
print(f"Input: {input_text}")
print(f"Prediction: {output[0]['label']}")
print(f"Confidence: {round(output[0]['score'] * 100, 2)}%")


