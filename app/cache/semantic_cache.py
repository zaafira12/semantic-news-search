import numpy as np
from app.config import SIMILARITY_THRESHOLD

class SemanticCache:

    def __init__(self, threshold=SIMILARITY_THRESHOLD):
        self.entries = {}
        self.threshold = threshold
        self.hit_count = 0
        self.miss_count = 0

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def lookup(self, query_embedding, cluster):

        cluster_entries = self.entries.get(cluster, [])

        for entry in cluster_entries:

            stored_embedding = entry["embedding"]

            similarity = self.cosine_similarity(
                query_embedding.reshape(1, -1),
                stored_embedding.reshape(1, -1)
            )[0][0]

            if similarity > self.threshold:

                self.hit_count += 1
                return entry["result"]

        self.miss_count += 1
        return None

    def store(self, query_embedding, cluster, result):

        if cluster not in self.entries:
            self.entries[cluster] = []

        self.entries[cluster].append({
            "embedding": query_embedding,
            "result": result
        })

    def stats(self):

        total = len(self.entries)

        hit_rate = 0
        if self.hit_count + self.miss_count > 0:
            hit_rate = self.hit_count / (self.hit_count + self.miss_count)

        return {
            "total_entries": total,
            "hit_count": self.hit_count,
            "miss_count": self.miss_count,
            "hit_rate": hit_rate
        }
   
    def clear(self):

        self.entries = []
        self.hit_count = 0
        self.miss_count = 0
cache = SemanticCache()