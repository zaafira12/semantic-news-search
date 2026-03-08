from app.data.loader import load_dataset
from app.data.preprocessing import clean_text
from app.core.embeddings import embed_batch
import numpy as np
import pickle


print("Loading dataset...")
documents = load_dataset()

print("Cleaning documents...")
documents = [clean_text(doc) for doc in documents]

print("Generating embeddings...")
embeddings = embed_batch(documents)

print("Saving embeddings...")

np.save("data/embeddings.npy", embeddings)

with open("data/documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Embeddings saved successfully!")