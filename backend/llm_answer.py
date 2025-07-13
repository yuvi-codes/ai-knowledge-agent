"""
LLM answer module.
"""
from transformers import pipeline
generator = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")

def generate_answer(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    output = generator(prompt, max_new_tokens=100)[0]["generated_text"]
    return output.split("Answer:")[-1].strip()
