from transformers import pipeline

# Define the input text (example)
original_text = """
The solar system consists of the Sun and the objects that orbit it, whether they orbit it 
directly or indirectly. Of those objects that orbit the Sun directly, the largest eight 
are the planets, with the remainder being significantly smaller objects, such as dwarf 
planets and small Solar System bodies. Of the objects that orbit the Sun indirectly, 
the moons, two are larger than the smallest planet, Mercury.
"""

# Create the summarization pipeline
# This downloads the t5-small-booksum model to local cache (~/.cache/huggingface)
print("Loading summarizer...")
summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum")

# Summarize the text
# max_length and min_length help control the output size
summary_text = summarizer(original_text, max_length=50, min_length=10, do_sample=False)

# Compare the length (as per snippet)
print("\n--- Summary Result ---")
print(f"Summary: {summary_text[0]['summary_text']}")
print("-" * 30)
print(f"Original text length: {len(original_text)} characters")
print(f"Summary length: {len(summary_text[0]['summary_text'])} characters")