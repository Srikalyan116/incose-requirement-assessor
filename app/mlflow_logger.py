import mlflow

def log_result(result: dict):
    with mlflow.start_run():
        mlflow.log_param("input", result["input"])
