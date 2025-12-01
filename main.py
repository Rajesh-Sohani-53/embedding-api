from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()

model = SentenceTransformer("all-MiniLM-L6-v2")

class Single(BaseModel):
    text: str

class Batch(BaseModel):
    texts: list[str]

@app.get("/")
def home():
    return {"message": "Embedding API running!"}

@app.post("/embed")
def embed(req: Single):
    emb = model.encode([req.text]).tolist()[0]
    return {"embedding": emb}

@app.post("/embed_batch")
def embed_batch(req: Batch):
    embs = model.encode(req.texts).tolist()
    return {"embeddings": embs}
