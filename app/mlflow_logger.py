import mlflow

mlflow.set_experiment("ISO_29148_Compliance")

def log_result(result):

    with mlflow.start_run():
        mlflow.log_param("input", result["input"])
        mlflow.log_metric("latency", result["latency_sec"])
        mlflow.log_metric("retrieval_count", result["retrieval_count"])

        if isinstance(result.get("analysis"), dict):
            mlflow.log_metric(
                "compliance_score",
                result["analysis"].get("compliance_score", 0)
            )
