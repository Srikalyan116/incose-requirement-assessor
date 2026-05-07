from app.weaviate_client import search_similar
from app.llm import generate_analysis
from app.mlflow_logger import log_result

def run_rag(text: str):
    retrieved = search_similar(text)
    analysis = generate_analysis(text, retrieved)

    result = {
        "input": text,
        "retrieved": retrieved,
        "analysis": analysis
    }

    log_result(result)
    return result
