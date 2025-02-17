from pydantic import BaseModel
from typing import List, Dict, Any

# Data models for request and response
class QuestionRequest(BaseModel):
    question: str
    pdf_paths: List[str]

class AnswerResponse(BaseModel):
    answer: str
    debug_info: Dict[str, Any] = {} # Added for returning debug info