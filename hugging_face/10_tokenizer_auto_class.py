from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# Define the model ID
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Download/Load the model and tokenizer
# These will be cached locally in ~/.cache/huggingface
print(f"Loading {model_name}...")
my_model = AutoModelForSequenceClassification.from_pretrained(model_name)
my_tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create the pipeline
# We explicitly pass our model and tokenizer to the pipeline
my_pipeline = pipeline(task="sentiment-analysis", model=my_model, tokenizer=my_tokenizer)

# Predict the sentiment
text_input = "This course is pretty good, I guess."
output = my_pipeline(text_input)

# Display the result
label = output[0]['label']
score = output[0]['score']

print("\n--- Sentiment Analysis Result ---")
print(f"Input: \"{text_input}\"")
print(f"Label: {label}")
print(f"Confidence: {score:.2%}")