from config import EMBEDDING_MODEL
import google.generativeai as genai
import numpy as np

def generate_embedding(text, model_name=EMBEDDING_MODEL):
    """Generates embedding for a given text using the Gemini embedding model."""
    try:
        embedding = genai.embed_content(
            model=model_name,
            content=text,
            task_type="retrieval_document",  # Important for RAG
            title=text[:50] # optional
        )
        return embedding['embedding']
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None

def vector_search(query_embedding, embeddings, documents, top_k=3):
    """Performs a simple vector search to find the most relevant documents."""
    scores = np.dot(embeddings, query_embedding)
    ranked_indices = np.argsort(scores)[::-1]
    return [(documents[i], scores[i]) for i in ranked_indices[:top_k]]