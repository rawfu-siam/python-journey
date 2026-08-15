'''
Chapter6, topic - FastAPI installation and project structure
'''
# =====================================================================
# 🧠 CHUNK 9: CORE DEFINITIONS & ARCHITECTURE BLUEPRINT
# =====================================================================
# FastAPI       -> A modern, high-performance web framework for Python APIs.
# Uvicorn       -> An ASGI web server engine used to run FastAPI applications.
# Pydantic      -> Data validation gatekeeper used to check input schemas.
#
# Root Directory execution standard:
# Always run: `uvicorn app.main:app --reload` from the root directory.
# Never enter the app folder to spin up the uvicorn engine.

# =====================================================================
# 📁 FILE SYSTEM VISUALIZATION (PRODUCTION LAYOUT)
# =====================================================================
# my_automation_project/
# ├── app/
# │   ├── __init__.py
# │   ├── main.py             <- Web routing, endpoints, metadata config
# │   └── services/
# │       ├── __init__.py
# │       └── ai_agent.py     <- Pure Python automation & business logic
# ├── .env                    <- Hidden private credentials
# └── requirements.txt        <- fastapi, uvicorn, pydantic

# =====================================================================
# 🧪 AGENCY WORKFLOW BEST PRACTICES
# =====================================================================
# 1. Version Routes   -> Always use `/api/v1/` paths to avoid service drops.
# 2. Def vs Async Def -> Use basic `def` for standard blocking web scrapers.
#                        FastAPI automatically handles them in threads safely.
# 3. Interactive UX   -> Test your routes live on `http://127.0.0`.
