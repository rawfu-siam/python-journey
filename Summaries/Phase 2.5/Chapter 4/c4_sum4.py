'''
Chapter4, topic - Deploying web services via cloud infrastructure 
                  providers (Railway / Render)
'''
# =====================================================================
# 🧠 CORE CLOUD DEPLOYMENT DEFINITIONS
# =====================================================================
# Deployment  -> Moving code from a local machine to a 24/7 remote server.
# Provider    -> Platforms like Railway or Render that run your apps.
# Localhost   -> Your personal computer network (isolated from the world).
# Web Service -> An app that stays alive indefinitely to answer web requests.

# =====================================================================
# 🏗️ THE 4 CRITICAL MOVING PARTS
# =====================================================================
# 1. 🐙 GitHub Repository:
#    - Holds your version-controlled source code.
#    - Cloud providers connect here to automatically pull code updates.
#
# 2. 📦 requirements.txt:
#    - The shopping list of packages (FastAPI, Uvicorn) the server must install.
#    - Generate automatically using: pip freeze > requirements.txt
#
# 3. 🔑 Environment Variables:
#    - Set directly inside the Railway/Render dashboard settings.
#    - Never push raw secret keys (.env files) directly to GitHub.
#
# 4. 🌐 Production Web Server Command:
#    - Runs your web app securely on the public internet.
#    - Format: uvicorn main:app --host 0.0.0.0 --port $PORT

# =====================================================================
# 🚨 COMMON REJECTIONS & CRASHES TO AVOID
# =====================================================================
# ❌ Hardcoding Ports  -> Using port=8000 breaks when the cloud sets a random $PORT.
# ❌ Localhost Binding -> Binding to 127.0.0.1 blocks external internet traffic.
# ❌ Missing Packages  -> Forgetting uvicorn in requirements leads to a boot crash.
# ❌ Missing Keep-Alive-> Simple linear scripts print once and exit, causing loops.

# =====================================================================
# 🇺🇸 AGENCY OPERATIONS STANDARDS
# =====================================================================
# ⭐ Rule 1 -> "It works on my machine" is unacceptable; it must work in the cloud.
# ⭐ Rule 2 -> Always include a clean .env.example file for your engineering team.
# ⭐ Rule 3 -> Build a explicit /health endpoint so cloud systems can monitor uptime.
