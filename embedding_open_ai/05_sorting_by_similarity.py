from scipy.spatial import distance


def find_n_closest(query_vector, embeddings, n=3):
  distances = []
  for index, embedding in enumerate(embeddings):
    # Calculate the cosine distance between the query vector and embedding
    dist = distance.cosine(query_vector, embedding)
    # Append the distance and index to distances
    distances.append({"distance": dist, "index": index})
  # Sort distances by the distance key
  distances_sorted = sorted(distances, key=lambda x: x['distance'])
  # Return the first n elements in distances_sorted
  return distances_sorted[0:n]


# Example usage to test it
if __name__ == "__main__":
    # Sample "embeddings" (vectors)
    sample_embeddings = [
        [1.0, 0.2, 0.0], # Index 0
        [0.1, 0.9, 0.1], # Index 1
        [1.1, 0.3, 0.1], # Index 2 (Very close to query)
    ]
    
    # A sample query vector
    sample_query = [1.0, 0.3, 0.0]
    
    # Run my function
    results = find_n_closest(sample_query, sample_embeddings, n=2)
    
    print("Closest matches:")
    for res in results:
        print(f"Index: {res['index']}, Distance: {res['distance']:.4f}")