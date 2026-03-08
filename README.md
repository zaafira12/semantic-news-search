![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

# Semantic News Search

A semantic search engine for news articles using sentence embeddings, vector similarity search, clustering, and caching.

## Features

- Semantic search using transformer embeddings
- Vector similarity search with FAISS
- Semantic query cache
- Cluster-aware retrieval
- Configurable similarity threshold
- Query latency tracking
- FastAPI API interface
- Docker container support

## Architecture

User Query
   │
   ▼
   
Query Embedding
(Sentence Transformer)

   │
   ▼
   
Cluster Detection
(KMeans)
   │
   ▼
   
Semantic Cache Lookup
   │
   ├── Cache Hit → Return Result
   │
   ▼
Vector Search
(FAISS Index)
   │
   ▼
Top Similar Documents
   │
   ▼
API Response
(FastAPI)

## Project Structure
semantic-news-search
│
├── app
│ ├── api
│ ├── core
│ ├── cache
│ └── data
│
├── scripts
│ ├── build_embeddings.py
│ ├── run_clustering.py
│ └── analyze_clusters.py
│
├── Dockerfile
├── requirements.txt


# Install dependencies:
pip install -r requirements.txt

# Run the API:
uvicorn app.main:app --reload

# Open API docs:
http://127.0.0.1:8000/docs

## API Interface
The project exposes a FastAPI REST API.

<img width="1920" height="1200" alt="Screenshot 2026-03-08 195353" src="https://github.com/user-attachments/assets/c97b7484-b336-4bf5-9ba6-571f3cc8fefa" />

## Example Query
POST /query
{
"query": "space exploration"
}

# Response:
{
"query": "space exploration",
"cache_hit": false,
"latency_ms": 37,
"results": [
{
"text": "...",
"score": 0.82
}
]
}

## Example Query Result

## Technologies Used

- Python
- FastAPI
- Sentence Transformers
- FAISS
- NumPy
- Docker

## Future Improvements

- UI dashboard for search
- Distributed vector search
- Advanced ranking models
  
## Author
Sk Zaafira Yumn
