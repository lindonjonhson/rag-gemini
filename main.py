from rag import rag_pipeline
from fastapi import FastAPI, HTTPException
from models import *
from urllib.parse import unquote, unquote_plus

app = FastAPI()

@app.get("/ask?q={question}")
async def answer_question(question):
    """Endpoint to answer a question using RAG."""
    try:

        question = unquote_plus(question)
        print(question)

        # question = "What are the documents about?"
        answer, debug_info = rag_pipeline(question)
        return AnswerResponse(answer=answer, debug_info=debug_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rag", response_model=AnswerResponse)
async def answer_question(request: QuestionRequest):
    """Endpoint to answer a question using RAG."""
    try:
        answer, debug_info = rag_pipeline(request.question)
        return AnswerResponse(answer=answer, debug_info=debug_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
