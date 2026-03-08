from fastapi.responses import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import os
from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
import pickle

from app.core.query_engine import QueryEngine
from app.core.vector_store import VectorStore
from app.cache.semantic_cache import cache


router = APIRouter()

print("Loading saved embeddings...")

embeddings = np.load("data/embeddings.npy")

with open("data/documents.pkl", "rb") as f:
    documents = pickle.load(f)

dimension = embeddings.shape[1]

vector_store = VectorStore(dimension)
vector_store.add(embeddings, documents)

print("Vector database loaded!")

engine = QueryEngine(vector_store)



class QueryRequest(BaseModel):
    query: str


@router.post("/query")
def query_endpoint(request: QueryRequest):
    result = engine.process_query(request.query)
    return result


@router.get("/cache/stats")
def cache_stats():
    return cache.stats()


@router.delete("/cache")
def clear_cache():
    cache.clear()
    return {"message": "Cache cleared"}

from fastapi.responses import StreamingResponse
import io

@router.post("/query/pdf")
def query_pdf(request: QueryRequest):

    result = engine.process_query(request.query)

    results = result.get("results") or result.get("result")

    buffer = io.BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)

    y = 750

    c.drawString(50, y, f"Query: {request.query}")
    y -= 40

    for r in results:

        text = r["text"][:300].replace("\n", " ")
        score = r["score"]

        c.drawString(50, y, f"Score: {score}")
        y -= 20

        c.drawString(50, y, text)
        y -= 40

        if y < 100:
            c.showPage()
            y = 750

    c.save()

    buffer.seek(0)

    filename = f"{request.query.replace(' ', '_')}.pdf"

    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )
@router.get("/health")
def health_check():

    return {
        "status": "ok",
        "vector_db_loaded": True,
        "cache_entries": cache.stats()["total_entries"]
    }