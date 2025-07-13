"""
Retriever module.
"""
import chromadb
client = chromadb.Client()
collection = client.get_or_create_collection(name="docs")

def add_embeddings(embeddings, texts):
    for i, emb in enumerate(embeddings):
        collection.add(embeddings=[emb], documents=[texts[i]], ids=[f"doc_{i}"])

def query(question_embedding, top_k=3):
    results = collection.query(query_embeddings=[question_embedding], n_results=top_k)
    return results["documents"][0]
