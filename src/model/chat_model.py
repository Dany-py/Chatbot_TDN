from pydantic import BaseModel
from datetime import datetime

class ChatData(BaseModel):
    question: str
    response: str
    date: datetime