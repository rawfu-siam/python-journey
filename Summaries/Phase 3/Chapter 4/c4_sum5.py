'''
Chapter4, topic - SQLAlchemy ORM — models and sessions
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# ORM (Object-Relational Mapper) -> A translator linking Python to SQL.
# SQLAlchemy -> The elite library used to talk to databases using OOP.
# Model      -> A Python class blueprint representing a database table.
# Session    -> A temporary transaction workspace (your shopping cart).
# Engine     -> The physical pipeline connection running to the database.
# Base       -> The master declarative registry brick all models inherit.

# =====================================================================
# 🛠️ DATA TRANSACTION STAGES
# =====================================================================
# Stage 1: Instantiation -> Create a regular Python object from a model.
# Stage 2: Staging       -> session.add(obj) places it in the active cart.
# Stage 3: Commitment    -> session.commit() writes it permanently to SQL.
# Stage 4: Cleanup       -> session.close() tears down connection pipelines.

# =====================================================================
# 🚀 AUSTRALIAN AI AGENCY BLUEPRINTS (PRO TIPS)
# =====================================================================
# 1. ALWAYS isolate connection strings inside a secure hidden .env file.
# 2. ALWAYS use Python 'with' context managers to handle session safety.
# 3. ALWAYS let primary_key=True generate unique IDs on the database side.
# 4. NEVER interact with database row objects after a session has closed.
