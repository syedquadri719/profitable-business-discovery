from fastapi import APIRouter
from app.services.discovery import get_ideas

router = APIRouter()

@router.get("/ideas")
async def ideas():
    return get_ideas()
