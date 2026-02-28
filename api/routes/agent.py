"""/agent endpoints (placeholder)."""

from fastapi import APIRouter

router = APIRouter()

@router.post("/run")
def run_agent():
    return {"status": "ok"}
