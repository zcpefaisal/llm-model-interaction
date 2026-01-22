from transformers import pipeline

# Define the input text
original_text = """
The Great Barrier Reef is the world's largest coral reef system, composed of over 
2,900 individual reefs and 900 islands stretching for over 2,300 kilometres over 
an area of approximately 344,400 square kilometres. The reef is located in the 
Coral Sea, off the coast of Queensland, Australia.
"""

# Create the pipeline with token constraints
# cnicu/t5-small-booksum is a lightweight model (~240MB)
print("Loading summarizer...")
short_summarizer = pipeline(
    task="summarization", 
    model="cnicu/t5-small-booksum", 
    min_new_tokens=1, 
    max_new_tokens=10
)

# Generate the summary
# min_new_tokens=1 ensures at least one token is generated
# max_new_tokens=10 forces a very concise output
short_summary_text = short_summarizer(original_text, do_sample=False)

# Display the result
print("\n--- Ultra-Short Summary ---")
print(short_summary_text[0]["summary_text"])