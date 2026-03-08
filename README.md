<p align="center">

# Semantic News Search

Semantic search engine for news articles using transformer embeddings, FAISS vector search, clustering and semantic caching.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

</p>

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

```mermaid
flowchart TD
A[User Query] --> B[Query Embedding]
B --> C[Cluster Detection]
C --> D[Semantic Cache Lookup]
D -->|Cache Hit| E[Return Result]
D -->|Cache Miss| F[Vector Search FAISS]
F --> G[Top Similar Documents]
G --> H[API Response FastAPI]
```

## Project Structure

```
semantic-news-search
│
├── app                # Main application code
│
├── scripts            # Data processing scripts
│   ├── build_embeddings.py
│   ├── run_clustering.py
│   └── analyze_clusters.py
│
├── Dockerfile         # Container setup
├── requirements.txt   # Python dependencies
└── .gitignore         # Ignored files
```

## Quick Start

Clone the repository

```bash
git clone https://github.com/zaafira12/semantic-news-search.git
cd semantic-news-search
# Install dependencies:
pip install -r requirements.txt
```
# Run the API:
uvicorn app.main:app --reload

# Open API docs:
http://127.0.0.1:8000/docs

## API Interface
The project exposes a FastAPI REST API.

<img width="1920" height="1200" alt="Screenshot 2026-03-08 195353" src="https://github.com/user-attachments/assets/c97b7484-b336-4bf5-9ba6-571f3cc8fefa" />

## Example Query
POST /query

```json
{
  "query": "space exploration"
}
```
# Response:
```json
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
```
## Example Query Result

<img width="1773" height="968" alt="Screenshot 2026-03-08 200603" src="https://github.com/user-attachments/assets/79329ac9-9b60-414f-885a-d7ba050a388a" />

<img width="1736" height="974" alt="Screenshot 2026-03-08 200614" src="https://github.com/user-attachments/assets/078822a0-74ed-42b4-8f11-75f79e661cc3" />

<img width="1737" height="811" alt="Screenshot 2026-03-08 200627" src="https://github.com/user-attachments/assets/503606ff-03c6-4fae-9973-b5c25626b1fa" />

<img width="1735" height="988" alt="Screenshot 2026-03-08 200641" src="https://github.com/user-attachments/assets/f774f0c5-5f13-4edb-bb8b-197549fa60bb" />

## Performance
```markdown
  - Semantic search powered by **FAISS vector indexing**

- **Semantic cache** reduces repeated query cost
- **Cluster-aware retrieval** improves relevance
- Query latency tracking included

Example:

Cache hit: **true**  
Latency: **37 ms**
```
## System Components
```markdown
| Component | Description |
|----------|-------------|
| Embeddings | Sentence Transformers generate semantic vectors |
| Vector Store | FAISS performs fast similarity search |
| Clustering | Groups documents for faster retrieval |
| Cache | Semantic cache avoids recomputation |
| API | FastAPI exposes query endpoint |
```

# Technologies Used
- Python
- FastAPI
- Sentence Transformers
- FAISS
- NumPy
- Docker

## Future Improvements
- Hybrid semantic + keyword retrieval
- Improved ranking models
- Web search interface
- UI dashboard for search
- Distributed vector search
- Advanced ranking models
  
## Author
Sk Zaafira Yumn
skzaafirayumn30669@gmail.com
