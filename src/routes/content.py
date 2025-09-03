from fastapi import APIRouter, Request, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.database import get_db
from src.models import ChatHistory
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/chat/content/", response_class = HTMLResponse)
async def get_content(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ChatHistory))
    content = result.scalars().all()

    # Convertir les objets SQLAlchemy en une liste de dictionnaires
    content_data = [{"id": t.id, "question": t.question, "response": t.response, "date": t.date.isoformat() if t.date else ""} for t in content]

    return templates.TemplateResponse("content.html", {"request": request, "test_data": content_data})
