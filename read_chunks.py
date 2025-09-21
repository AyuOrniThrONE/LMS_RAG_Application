import requests

def create_embedding(text):
    r = requests.post("https:localhost:11434/api/embeddings", json={
        "models":"bge-m3",
        "prompt":text
    })

    embedding = r.json("embedding")
    return embedding

create_embedding("Harry is good boy")