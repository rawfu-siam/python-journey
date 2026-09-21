'''
Chapter7, topic - n8n — self-hosted setup with Docker
'''
# =====================================================================
# 🧠 DOCKERIZED N8N PLATFORM ARCHITECTURE 
# =====================================================================
# Self-Hosting    -> Running n8n on local machines or private cloud
#                    servers to eliminate monthly per-task execution fees.
# Docker Container -> An isolated digital box wrapping a software engine 
#                    so it runs flawlessly on Windows, Mac, or Linux.
# Docker Compose   -> An orchestration tool that boots up multi-container
#                    networks using a single plain text config file.
#
# =====================================================================
# 🐘 THE PRODUCTION INTEGRATION STACK
# =====================================================================
# 📦 SERVICE 1: n8n Core Engine
#   - Hosted inside: docker.n8n.io/n8nio/n8n:latest
#   - Default Network Interface Port: `5678`
#   - Purpose: Visual control panel to route enterprise automations.
#
# 🗄️ SERVICE 2: PostgreSQL Database Backend
#   - Hosted inside: postgres:16-alpine
#   - Default Network Interface Port: `5432`
#   - Purpose: Replaces default SQLite to prevent multi-threaded crashes.
#
# 💾 THE PERSISTENT VOLUME STORAGE
#   - Standard containers are ephemeral (data vanishes on crash).
#   - Named Volumes anchor container paths securely to local hard drives.
#   - Essential Path: `/home/node/.n8n` (Saves all automation steps).
#
# =====================================================================
# 🛡️ THE JUNIOR AGENCY DEVELOPER COMPLIANCE RULES
# =====================================================================
# 1. Never hardcode passwords inside `docker-compose.yml` configs.
# 2. Extract access secrets into hidden `.env` configurations.
# 3. Always reference cross-container hosts by their Compose service name.
# 4. Use `localhost` ONLY for scripts communicating from outside Docker.
# 5. Boot stacks using `docker-compose up -d` to run quietly in background.
#
# =====================================================================
# 🪄 THE PRODUCTION SYSTEM INFRASTRUCTURE GOLDEN SPELL
# =====================================================================
# "Containers handle the processing, but Volumes own the data."
# =====================================================================
