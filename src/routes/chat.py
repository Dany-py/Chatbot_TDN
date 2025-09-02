import json
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.models import ChatHistory
from src.model.chat_model import ChatData
from src.gemini_api import get_gemini_response
import datetime
from pydantic import BaseModel

# Modèle Pydantic pour valider les données de la requête
class ChatRequest(BaseModel):
    message: str

router = APIRouter()

@router.post("/api/chat")
async def add_discussion(question: str, response: str, db: AsyncSession = Depends(get_db)):
    discussion = ChatHistory(question= question, response= response, date= datetime.datetime.now())
    db.add(discussion)
    await db.commit()
    await db.refresh(discussion)


@router.websocket("/api/ws/chat")
async def websocket_endpoint(websocket: WebSocket, db: AsyncSession = Depends(get_db)):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()

            try:
                user_message_dict= json.loads(data)
                user_message = ChatRequest(**user_message_dict)
            except (json.JSONDecodeError, TypeError):
                await websocket.send_json({"error": "Format JSON invalide"})
                continue
                
            # Récupère le message
            message_text = user_message.message
            
            # Traite le message et génère une réponse AI
            print(f"Message reçu : {message_text}")
            ai_response = get_gemini_response(message_text)
            
            # Enregistre l'historique directement
            await add_discussion(message_text, ai_response, db)
            
            # Envoie la réponse au client
            response = {"text": ai_response}
            await websocket.send_json(response)

    except WebSocketDisconnect:
        print("Le client s'est déconnecté.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
    finally:
        await websocket.close()
        print("Connexion WebSocket fermée.")
"""
            user_message = json.loads(data)
            message_text = user_message.get("message")
            
            if message_text:
                # Call gemini API
                ai_response = get_gemini_response(message_text)
                donne = {
                    "question" : message_text,
                    "response" : ai_response,
                    "date" : datetime.datetime.now()
                }
                await add_discussion(donne, db)
                response = {"text": ai_response}
                await websocket.send_json(response)
                
    except Exception as e:
        print(f"Erreur ou déconnexion : {e}")
    finally:
        await websocket.close()"""