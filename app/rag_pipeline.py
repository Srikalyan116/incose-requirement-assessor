import time
from app.weaviate_client import search_similar
from app.llm import generate_analysis
from app.mlflow_logger import log_result

def run_rag(text: str):
    start = time.time()

    retrieved = search_similar(text)

    analysis = generate_analysis(text, retrieved)

    latency = round(time.time() - start, 2)

    result = {
        "input": text,
        "retrieval_count": len(retrieved),
        "retrieved_context": retrieved,
        "analysis": analysis,
        "latency_sec": latency
    }

    log_result(result)
    return result
``
