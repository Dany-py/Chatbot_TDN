from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables depuis le fichier .env

db_url = os.getenv("DATABASE_URL")


# Création du moteur asynchrone
engine = create_async_engine(db_url, echo=True)

# Création de la session
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base pour les modèles
Base = declarative_base()

# Dépendance pour récupérer la session
async def get_db():
    async with SessionLocal() as session:
        yield session
