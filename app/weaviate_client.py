import weaviate

client = weaviate.Client("http://localhost:8080")

client.schema.create_class({
    "class": "Requirement",
    "vectorizer": "text2vec-openai",
    "properties": [
        {"name": "text", "dataType": ["text"]}
    ]
})

samples = [
    "The system shall respond within 2 seconds",
    "The UI should be user friendly",
    "The system shall support 1000 concurrent users"
]

for s in samples:
    client.data_object.create({"text": s}, "Requirement")
