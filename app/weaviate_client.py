import weaviate
client = weaviate.Client("http://localhost:8080")

def search_similar(query: str):
    result = client.query.get("Requirement", ["text"]).with_near_text({"concepts": [query]}).with_limit(5).do()
    return result.get("data", {}).get("Get", {}).get("Requirement", [])
