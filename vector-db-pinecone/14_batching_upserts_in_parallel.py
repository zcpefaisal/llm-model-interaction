import itertools
from pinecone import Pinecone

# The Chunking Helper Function
def chunks(iterable, batch_size=100):
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))

# Initialize the Pinecone client with a Thread Pool
# pool_threads=20 allows 20 concurrent network connections
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V", pool_threads=20)

# Assume 'vectors' is a large list of prepared dictionaries 
# (id, values, metadata) as we created in the previously.
# Let's pretend we have 2000 vectors for this example.
vectors = [{"id": f"id-{i}", "values": [0.1]*1536} for i in range(2000)]

# Use a Context Manager ('with' statement) for Parallel Upsert
# This is the most stable way to handle asynchronous requests
with pc.Index('my-index') as index:
    # Create a list of 'asynchronous handles' (promises)
    # Each chunk is 200 vectors, sent on its own thread
    async_results = [
        index.upsert(vectors=chunk, async_req=True) 
        for chunk in chunks(vectors, batch_size=200)
    ]
    
    # .get() blocks the script until ALL parallel requests are finished
    [async_result.get() for async_result in async_results]
    print("All parallel batches have been successfully sent!")

# Verify the results
print("Updated Index Metrics")
print(index.describe_index_stats())