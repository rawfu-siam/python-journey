'''
Chapter6, topic - connecting FastAPI to a database
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ROLES
# =====================================================================
# Database Engine -> The system highway link between Python and your hard drive.
# ORM (SQLAlchemy)-> The structural translator turning Python into database tables.
# Pydantic Schema -> The internet border guard validating request types at entry.
# SessionFactory  -> The gatekeeper spawning individual connection sessions.

# =====================================================================
# 📂 THE ENTERPRISE MODULE DESIGN PATTERN
# =====================================================================
# 1. database.py -> Coordinates connection setups, URLs, and session builders.
# 2. models.py   -> Sets up the permanent hard drive blueprints for SQL tables.
# 3. schemas.py  -> Configures network shape contracts using Pydantic parameters.
# 4. main.py     -> Exposes URL endpoint routes and executes real execution paths.

# =====================================================================
# ⚠️ THE CRITICAL JUNIOR PITFALLS
# =====================================================================
# Trap 1: Forgetting db.commit() -> Records stay on the desk and are never saved.
# Trap 2: Connection Leakage   -> Leaving sessions open until server crash.
# Trap 3: Async Engine Clashes   -> Running synchronous SQLAlchemy inside async def.

# =====================================================================
# 🇦🇺 🇸🇬 PREMIUM AGENCY BEST PRACTICES
# =====================================================================
# Rule 1: Always isolate credential URLs into external .env variables.
# Rule 2: Wrap execution commits inside protective try/except blocks.
# Rule 3: Run db.rollback() immediately if any write operation fails.
# Rule 4: Add indexing flags on high-frequency searching columns.
