from fastapi import APIRouter
from app.rag_pipeline import run_rag

router = APIRouter()

@router.post("/analyze")
def analyze(req: dict):
    return run_rag(req.get("text", ""))
