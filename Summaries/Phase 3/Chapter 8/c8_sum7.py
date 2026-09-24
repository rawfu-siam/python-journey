'''
Chapter8, topic - deploying to Railway, Render, or Fly.io
'''
# =====================================================================
# 🧠 CORE DEPLOYMENT DEFINITIONS
# =====================================================================
# Deployment  -> Moving code from a local laptop to an always-on cloud server.
# Server      -> A powerful, remote computer running 24/7 in a datacenter.
# Cloud Hosts -> Digital landlords (Railway, Render, Fly.io) hosting your app.
# Port        -> The numeric digital door assigned to route web traffic to an app.

# =====================================================================
# 🏗️ THE 4 PILLARS OF A SUCCESSFUL DEPLOYMENT
# =====================================================================
# 🐙 1. GitHub Integration:
#   - Serves as the source code delivery pipeline for continuous deployment.
#   - Pushing code to your main branch triggers an automatic cloud rebuild.
#
# 📦 2. Dependency Manifest (requirements.txt):
#   - The environment blueprint detailing exactly what packages to install.
#   - Generated locally using: pip freeze > requirements.txt
#
# 📜 3. Startup Instructions (Procfile / Start Command):
#   - Tells the remote server engine how to execute the application process.
#   - Standard FastAPI setup: uvicorn main:app --host 0.0.0.0 --port $PORT
#
# 🔑 4. Secure Vaults (Environment Variables):
#   - Absolute isolation of sensitive production keys from public code repositories.
#   - Kept in .gitignore locally, but typed into the cloud host's web UI settings.

# =====================================================================
# ⚠️ CRITICAL SENIOR GUARDRAILS & COMMON PITFALLS
# =====================================================================
# 💥 Port Binding Failure: Hardcoding a static port (like 8000) causes crashes.
#   - Solution: Use the dynamic system-assigned '$PORT' environment variable.
#
# 👻 Silent Log Buffering: Print statements caching invisibly inside cloud terms.
#   - Solution: Pass 'flush=True' into print() or run with PYTHONUNBUFFERED=1.
#
# 📝 Ephemeral Disk Loss: App logs saved to disk vanish when cloud instances reboot.
#   - Solution: Stream logs directly to standard console output (stdout).
