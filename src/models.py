from sqlalchemy import Column, Integer, String, Date
from src.database import Base

## Modèle de la table Chat_history
class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    response = Column(String, index=True)
    date = Column(Date, index=True)

    def __repr__(self):
        return f"<ChatHistory(id={self.id}, question={self.question}, date={self.date})>"