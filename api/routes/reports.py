"""/reports endpoints (placeholder)."""

from fastapi import APIRouter

router = APIRouter()

@router.get("/reports/latest")
def latest_report():
    return {"report": None}

@router.get("/reports/history")
def reports_history():
    return {"reports": []}
