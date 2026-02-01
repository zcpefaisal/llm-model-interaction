from sentence_transformers import SentenceTransformer
from scipy.spatial import distance

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(texts):
    if isinstance(texts, str):
        texts = [texts]
    return model.encode(texts)

# --- SAMPLE DATA ---
sentiments = [
    {'label': 'Positive', 'description': 'A positive restaurant review'},
    {'label': 'Neutral', 'description': 'A neutral restaurant review'},
    {'label': 'Negative', 'description': 'A negative restaurant review'}
]

reviews = [
    "The food was delicious!",
    "The service was a bit slow but the food was good",
    "The food was cold, really disappointing!"
]


# Extract and embed the descriptions from sentiments
class_descriptions = [sentiment['description'] for sentiment in sentiments]
class_embeddings = create_embeddings(class_descriptions)
review_embeddings = create_embeddings(reviews)

def find_closest(query_vector, embeddings):
  distances = []
  for index, embedding in enumerate(embeddings):
    dist = distance.cosine(query_vector, embedding)
    distances.append({"distance": dist, "index": index})
  return min(distances, key=lambda x: x["distance"])

for index, review in enumerate(reviews):
  closest = find_closest(review_embeddings[index], class_embeddings)
  label = sentiments[closest['index']]['label']
  print(f'"{review}" was classified as {label}')
