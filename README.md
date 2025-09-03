# Chatbot_TDN
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![Licence](https://img.shields.io/badge/licence-Propriétaire-red)

Bienvenue dans le projet **Chatbot_TDN** : une API Python moderne basée sur [FastAPI](https://fastapi.tiangolo.com/) pour servir d'interface à un chatbot IA.  
Ce projet est conçu pour être rapide, modulaire et facilement extensible.

---

## 🚀 Fonctionnalités principales

- **API RESTful** rapide avec FastAPI
- Documentation interactive automatique (Swagger / ReDoc)
- Architecture modulaire et évolutive
- Prêt pour l'intégration avec Rasa ou d'autres moteurs IA
- Prise en charge des bases de données (SQLAlchemy, Prisma, etc.)
- Prêt pour le déploiement (Uvicorn, Docker...)

---

## 📦 Installation

### Prérequis

- Python 3.9 ou supérieur
- `pip` (gestionnaire de paquets Python)
- Postgresql-16

### Étapes

```sh
# 1. Clonez le dépôt
git clone https://github.com/Dany-py/Chatbot_TDN.git
cd Chatbot_TDN

# 2. Créez un environnement virtuel
python -m venv venv

# 3. Activez-le
# Sous Windows :
venv\Scripts\activate
# Sous Linux/Mac :
source venv/bin/activate

# 4. Installez les dépendances
pip install -r requirements.txt
```

---

## ▶️ Lancer le serveur

```sh
uvicorn main:app --reload
```
- Accès home page : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Accès chatbot : [http://127.0.0.1:8000/chat/](http://127.0.0.1:8000/chat/)
- Documentation Swagger : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Documentation ReDoc : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🗂️ Structure du projet

```Chatbot_TDN/
├── 📁 src/                         # Code source principal
│   ├── 📁 model/                   # Modèles de données
│   │   ├── 🐍 __init__.py
│   │   └── 🐍 chat_model.py         # Interactions du chatbot
│   ├── 📁 routes/                  # Définition des routes
│   ├── 🐍 __init__.py
│   │   ├── 🐍 chat.py               # Routes liées au chatbot
│   │   └── 🐍 home.py               # Route principale
│   ├── 🐍 __init__.py
│   ├── 🐍 database.py               # Connexion & gestion DB
│   ├── 🐍 gemini_api.py             # API externe (Gemini / IA)
│   └── 🐍 models.py                 # Définition des modèles ORM (SQLAlchemy, etc.)
│
├── 📁 static/                      # Fichiers statiques
│   ├── 📁 img/                     # Ressources graphiques
│   │   ├── 🖼️ man.png
│   │   └── 🖼️ sms.png
│   └── 📄 file.txt
│
├── 📁 templates/                   # Templates HTML
│   ├── 🌐 chat.html
│   ├── 🌐 index.html
│   ├── 🌐 page.html
│   └── 🌐 test.html
│
├── 📁 tests/                       # Tests unitaires
│   ├── 🐍 __init__.py
│   ├── 🐍 test_articles.py
│   ├── 🐍 test_chat.py
│   └── 🐍 test_db.py
│
├── 📄 LICENCE                      # Licence utilisateur final
├── 📖 README.md                    # Documentation du projet
├── ⚙️ alembic.ini                   # Config migrations BD
├── 🐍 create_db.py                  # Initialisation de la BD
├── 🐍 main.py                       # Point d’entrée FastAPI
├── ⚙️ pytest.ini                    # Configuration Pytest
├── ⚙️ pyvenv.cfg                    # Config env virtuel Python
└── 📄 requirements.txt              # Dépendances Python

```
---

## 📄 Licence

Ce projet est distribué sous **Licence Propriétaire**.  
L'utilisation, la copie, la modification ou la distribution du code source sont strictement encadrées par le [contrat de licence utilisateur final (CLUF)](./LICENCE).

---

## 🤝 Contribution

Les contributions sont les bienvenues !  
Pour contribuer :

1. Forkez ce dépôt
2. Créez une branche (`git checkout -b feature/ma-fonctionnalite`)
3. Commitez vos modifications
4. Pushez la branche (`git push origin feature/ma-fonctionnalite`)
5. Ouvrez une Pull Request

---

## 🙏 Remerciements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Gemini](https://gemini.google.com/)
- Toute la communauté open source

