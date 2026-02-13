import itertools

def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable (like a list) into an iterator
    it = iter(iterable)
    
    # Slice the iterator into the first chunk
    chunk = tuple(itertools.islice(it, batch_size))
    
    while chunk:
        # Yield the current chunk to the caller
        yield chunk
        # Get the next slice
        chunk = tuple(itertools.islice(it, batch_size))


# ============ Local Testing the Function ================

# Create a dummy list of 10 items (IDs of vectors)
my_vectors = [f"id_{i}" for i in range(1, 11)]

print(f"Original List: {my_vectors}")

# Use the function to process in batches of 3
for i, batch in enumerate(chunks(my_vectors, batch_size=3)):
    print(f"Batch {i+1}: {batch}")