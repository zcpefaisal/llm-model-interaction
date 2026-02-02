import tiktoken

# Sample data for local testing
documents = [
    "A story about a group of friends in 1980s Indiana.",
    "A documentary about the secrets of the deep ocean.",
    "A high-stakes thriller set in the world of international finance."
]


# Load the encoder for the OpenAI text-embedding-3-small model
enc = tiktoken.encoding_for_model("text-embedding-3-small")

# Encode each text in documents and calculate the total tokens
total_tokens = sum(len(enc.encode(d)) for d in documents)

cost_per_1k_tokens = 0.00002

# Display number of tokens and cost
print('Total tokens:', total_tokens)
print('Cost:', cost_per_1k_tokens * total_tokens / 1000)