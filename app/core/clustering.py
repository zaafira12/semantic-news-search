import numpy as np
import skfuzzy as fuzz


def perform_fuzzy_clustering(embeddings, n_clusters=10):

    data = np.array(embeddings)

    cntr, u, _, _, _, _, _ = fuzz.cluster.cmeans(
        data.T,
        n_clusters,
        2,
        error=0.005,
        maxiter=1000,
        init=None
    )

    return cntr, u