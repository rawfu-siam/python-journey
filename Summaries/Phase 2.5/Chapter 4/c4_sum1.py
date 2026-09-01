'''
Chapter4, topic - FastAPI framework initialization basics
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ROLES
# =====================================================================
# FastAPI    -> A modern Python library that turns local code into a Web API.
#            -> Acts as a megaphone, exposing your scripts safely to the internet.
# Init       -> The act of creating the main server application object engine.
# Uvicorn    -> The lightning-fast ASGI web server companion (the "waiter").
#            -> Physically listens to the web and hands requests to your app.
#
# =====================================================================
# 🏢 AGENCY WORKFLOW & REAL-WORLD UTILITY
# =====================================================================
# Business   -> Solves the problem of client terminal fear.
#            -> Replaces scary command lines with a clickable, shareable web URL.
# Inter-op   -> Acts as the central hub connecting custom Python scripts directly
#            -> to automated workflows like n8n, Make.com, or frontend interfaces.
#
# =====================================================================
# 🧩 FRAMEWORK INITIALIZATION COMPONENTS
# =====================================================================
# 1. Import  -> `from fastapi import FastAPI` pulling the class blueprint.
# 2. Variable-> `app = FastAPI()` initializing the central manager instance.
# 3. Server  -> `uvicorn main:app --reload` launching local gateway traffic.
#            -> `main` stands for the filename: `app` is the variable inside.
#            -> `--reload` auto-restarts your server every single time you save.
#
# =====================================================================
# ⚠️ CRITICAL BEGINNER TRAPS TO AVOID
# =====================================================================
# Brackets   -> Never do `app = FastAPI`. You must include parentheses: `FastAPI()`.
# Filenames  -> Never name your script `fastapi.py`. It creates import deadlocks.
# Paths      -> Ensure terminal launches match `uvicorn filename:variable_name`.
#
# =====================================================================
# 🛡️ ENTERPRISE GUARDRAILS & AGENCY BEST PRACTICES
# =====================================================================
# Auto-Docs  -> FastAPI automatically generates live testing dashboards at `/docs`.
# Hidden Paths-> Hide `/docs` pathways in live production files using env logic.
# Lifespans  -> Use `lifespan` arguments inside `FastAPI()` initialization.
#            -> This fires safe startup/shutdown data hooks (DB connects/disconnects).
# Philosophy -> Write less code by letting the framework handle core automation data validation.
# Spell      -> "Initialize the app, let Uvicorn hold the lap, and test it on the interactive map!"
