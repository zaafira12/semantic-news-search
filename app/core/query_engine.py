import time
import logging
import numpy as np

from app.core.embeddings import embed_text
from app.cache.semantic_cache import cache


class QueryEngine:

    def __init__(self, vector_store):
        self.vector_store = vector_store


    def process_query(self, query):

        start = time.time()

        query_embedding = embed_text(query)

        cluster = int(np.argmax(query_embedding))

        logging.info(f"Assigned cluster: {cluster}")

        cache_result = cache.lookup(query_embedding, cluster)

        if cache_result:

            latency = time.time() - start

            return {
                "query": query,
                "cache_hit": True,
                "latency_ms": latency * 1000,
                "result": cache_result
            }

        results = self.vector_store.search(query_embedding)

        cache.store(query_embedding, cluster, results)

        latency = time.time() - start

        return {
            "query": query,
            "cache_hit": False,
            "latency_ms": latency * 1000,
            "results": results,
            "cluster": cluster
        }