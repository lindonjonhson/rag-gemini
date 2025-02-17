from pdf_utils import *
from embedding_utils import *
from llm_utils import *

def rag_pipeline(question):
    """Main RAG pipeline."""

    pdf_paths = [
        "data/2023-conocophillips-aim-presentation.pdf",
        "data/2024-conocophillips-proxy-statement.pdf"
        ] 

    documents = []
    embeddings = []

    for pdf_path in pdf_paths:
        text = load_pdf(pdf_path)
        chunks = chunk_text(text)

        for chunk in chunks:
            embedding = generate_embedding(chunk)
            if embedding:
                documents.append(chunk)
                embeddings.append(embedding)

    if not embeddings:
        return "No relevant information found in the documents."

    query_embedding = generate_embedding(question)

    if not query_embedding:
        return "Could not process your question."

    # Vector search
    relevant_documents = vector_search(query_embedding, embeddings, documents)

    # Create context from the retrieved documents
    context = "\n\n".join([doc for doc, score in relevant_documents]) # Added scores for debugging
    debug_info = {"relevant_documents": [(doc[:100] + "...", score) for doc, score in relevant_documents]} # Just the beginning of doc for brevity

    # Create prompt
    prompt = create_prompt(question, context)

    # Generate answer
    answer = generate_answer(prompt)
    return answer, debug_info