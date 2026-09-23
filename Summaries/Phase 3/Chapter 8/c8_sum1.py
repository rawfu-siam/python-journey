'''
Chapter8, topic - what is Docker and why it matters
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# Docker      -> Magic tool to pack code + runtime into an isolated box.
# Container   -> A living, running, completely isolated sandbox app.
# Image       -> A frozen, read-only template used to spin up containers.
# Dockerfile  -> A plain text recipe file containing build instructions.
# Docker Hub  -> The global cloud marketplace for pre-made official images.

# =====================================================================
# ⚡ THE PRODUCTION LIFECYCLE
# =====================================================================
# 1. Write instructions inside a text file named: `Dockerfile`
# 2. Build the unchangeable frozen snapshot disk: `docker build`
# 3. Boot up the live, isolated sandbox container: `docker run`

# =====================================================================
# 🛡️ THE GOLDEN AGENCY RULES & BEST PRACTICES
# =====================================================================
# 📦 Size Matters:
#   - Avoid `FROM python:latest` (too heavy, bloats server costs).
#   - Always use lightweight bases like `FROM python:3.11-slim`.
#
# 🏎️ Layer Caching Speed:
#   - Copy `requirements.txt` and run `pip install` BEFORE copying code.
#   - This stops Docker from reinstalling all libraries on minor code edits.
#
# 🛑 Safety Guardrails:
#   - Use a `.dockerignore` file to block `venv/` and `.env` from leaking.
#   - Bind web apps to `--host 0.0.0.0` so they are accessible outside.
#   - Pass sensitive credentials dynamically at runtime, never hardcoded.
