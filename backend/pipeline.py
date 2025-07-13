"""
Pipeline module: glue everything together.
"""
from .embedder import embed_texts
from .retriever import add_embeddings, query
from .llm_answer import generate_answer

def process_pdf_and_store(pdf_text):
    chunks = [pdf_text[i:i+500] for i in range(0, len(pdf_text), 500)]
    embeddings = embed_texts(chunks)
    add_embeddings(embeddings, chunks)

def answer_question(question):
    q_emb = embed_texts([question])[0]
    top_chunks = query(q_emb, top_k=3)
    return generate_answer(" ".join(top_chunks), question)
