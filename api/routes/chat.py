from fastapi import APIRouter, HTTPException
from core.client import create_client
from agent.runner import run_agent
from api.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/api",
    tags=["Agent"]
)

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        client = create_client()
        result = run_agent(
            client=client,
            user_prompt=request.message
        )
        
        return ChatResponse(response=result)
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Agent execution failed: {str(e)}"
        )