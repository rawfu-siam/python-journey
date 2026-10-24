'''
Chapter6, topic - AI agents with database memory
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# Agent Memory   -> Giving AI persistent storage to recall past data.
# SQLite         -> A lightweight, file-based database for local apps.
# Session ID     -> A unique tag to separate different users' chats.

# =====================================================================
# 🗄️ THE 4-STEP MEMORY WORKFLOW
# =====================================================================
# 1. Initialize  -> Create database tables if they do not exist.
# 2. Load History-> Query database using session ID to fetch past chats.
# 3. Append & Run-> Add new user input, combine history, send to LLM.
# 4. Save Record -> Write both user prompt and AI reply back to DB.

# =====================================================================
# 🛡️ PRODUCTION GUARDRAILS & SENIOR SECRETS
# =====================================================================
# - Isolate sessions: Always filter database queries by session ID.
# - Prevent bloat: Use a sliding window or summary to limit token costs.
# - Scale up: Transition to PostgreSQL and ORMs as user bases grow.
# - Optimize speed: Add indexes on foreign keys and session identifiers.