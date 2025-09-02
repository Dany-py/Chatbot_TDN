
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables depuis le fichier .env

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY") )

theme_instructions = """
Tu es un assistant sur Togo Daily News dont l'adresse est https://tdn.tg. 
Ta mission est d'aider l'utilisateur à naviguer sur le site et à trouver des informations ou articles.
- Ne fais aucune introduction inutile sur toi-même.
- Donne des réponses courtes, concises et précises.
- Si la question est trop vague, indique-le poliment et propose une reformulation.
- Garde toujours le contexte de la conversation pour mieux comprendre les questions suivantes.
- Propose régulièrement d'autres articles pertinents afin de garder l'utilisateur engagé sur le site.
"""

conversation_history = theme_instructions + "\n\n"

def get_gemini_response(question):

    try:
        # Créez le prompt de conversation avec le contexte
        prompt = conversation_history + f"Utilisateur: {question}\n"
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents = prompt,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            ),
        )

        if response.text:
            return response.text
        else:
            return "Désolé, je n'ai pas pu générer de réponse."
    except Exception as e:
        return f"Une erreur est survenue : {e}"