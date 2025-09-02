"""# test_db.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base, get_db
from fastapi.testclient import TestClient
from main import app

# On crée une base SQLite en mémoire
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture pytest pour une session isolée
@pytest.fixture
def db_session():
    Base.metadata.create_all(bind=engine)  # recrée les tables
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)  # nettoie après chaque test

# On override la dépendance get_db
@pytest.fixture
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base, get_db
from fastapi.testclient import TestClient
from main import app

# Crée une base SQLite en mémoire pour les tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    # Recrée les tables pour chaque test
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session # Le test s'exécute ici
    finally:
        session.close() # La session est fermée à la fin du test
        Base.metadata.drop_all(bind=engine) # Nettoie les tables

# Surcharge la dépendance `get_db` pour chaque test
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    # Réinitialise les dépendances après le test
    app.dependency_overrides.clear()