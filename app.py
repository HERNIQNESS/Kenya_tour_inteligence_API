from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from rag_service import ask 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = "KENYA TOURING API ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Or your specific frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str 
    
class QuestionResponse(BaseModel):
    answer: str 
    sources: list
    
@app.get("/")
def root():
    return {"message":"TOUR API is running"}
    
@app.post("/ask", response_model = QuestionResponse)
def ask_qustion(request: QuestionRequest):
    try:
        answer, sources = ask(request.question)
        
        return QuestionResponse(
            answer=answer,
            sources = sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))