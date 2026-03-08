from app.data.loader import load_dataset
from app.data.preprocessing import clean_text
from app.core.embeddings import embed_batch
from app.core.clustering import perform_fuzzy_clustering


print("Loading dataset...")

documents = load_dataset()

print("Cleaning documents...")

documents = [clean_text(doc) for doc in documents]

print("Generating embeddings...")

embeddings = embed_batch(documents)

print("Running fuzzy clustering...")

centers, membership = perform_fuzzy_clustering(embeddings)

print("Clustering completed!")

print("Membership matrix shape:", membership.shape)