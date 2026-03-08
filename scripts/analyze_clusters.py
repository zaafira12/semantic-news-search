import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

with open("data/documents.pkl", "rb") as f:
    documents = pickle.load(f)

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(documents)

terms = vectorizer.get_feature_names_out()

for i in range(10):
    top_terms = terms[np.argsort(X.mean(axis=0)).A1[-10:]]
    print(f"Cluster {i}:", top_terms)