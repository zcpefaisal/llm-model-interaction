from sentence_transformers import SentenceTransformer
from scipy.spatial import distance

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(texts):
    if isinstance(texts, str):
        texts = [texts]
    return model.encode(texts)

# --- SAMPLE DATA ---
sentiments = [{'label': 'Positive'},
              {'label': 'Neutral'},
              {'label': 'Negative'}]

reviews = ["The food was delicious!",
           "The service was a bit slow but the food was good",
           "The food was cold, really disappointing!"]


# Create a list of class descriptions from the sentiment labels
class_descriptions = [sentiment['label'] for sentiment in sentiments]

# Embed the class_descriptions and reviews
class_embeddings = create_embeddings(class_descriptions)
review_embeddings = create_embeddings(reviews)


# --- LOGIC TO SEE RESULTS (Zero-Shot Classification) ---
print("Sentiment Analysis Results:")
for i, review_emb in enumerate(review_embeddings):
    # Find which class_embedding is closest to this review_embedding
    distances = [distance.cosine(review_emb, class_emb) for class_emb in class_embeddings]
    best_match_index = distances.index(min(distances))
    
    predicted_label = class_descriptions[best_match_index]
    print(f"Review: \"{reviews[i]}\"")
    print(f"Predicted Sentiment: {predicted_label}\n")