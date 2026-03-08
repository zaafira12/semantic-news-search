import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add(self, embeddings, docs):

        self.index.add(np.array(embeddings))
        self.documents.extend(docs)

    def search(self, query_vector, k=5):

        query_vector = np.array([query_vector])

        distances, indices = self.index.search(query_vector, k)

        results = []

        for i, idx in enumerate(indices[0]):

            if idx == -1:
                continue

            results.append({
                "text": self.documents[idx],
                "score": float(distances[0][i])
            })

        return results