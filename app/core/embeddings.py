from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
def embed_text(text):

    return model.encode([text])[0]

def embed_batch(texts):

    return model.encode(texts)