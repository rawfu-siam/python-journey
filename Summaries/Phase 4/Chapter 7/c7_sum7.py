'''
Chapter7, topic - deploying AI apps — Railway, Render, AWS
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & CONCEPTS
# =====================================================================
# Deployment    -> Moving code from a local laptop to a 24/7 cloud server
#                  so global users can access it via a live URL.
# ASGI Server   -> An application engine (like Uvicorn) that keeps your
#                  FastAPI app running and listening for web traffic.
# Cloud Host    -> Online infrastructure that runs your app repository.

# =====================================================================
# ⚙️ MOVING PARTS OF DEPLOYMENT
# =====================================================================
# 1. Main Script  -> FastAPI app configured with dynamic port listening.
# 2. Dependencies -> A `requirements.txt` file listing all required packages.
# 3. Environment  -> Secure dashboard settings for private API keys.
# 4. Host Platform-> Online service that builds and hosts your repository.

# =====================================================================
# 🏢 AGENCY-GRADE PRODUCTION BEST PRACTICES
# =====================================================================
# 🚫 Avoid hardcoding ports; always use `os.environ.get("PORT")`.
# 🛡️ Never push private keys to `https://github.com`; use dashboard secrets.
# 🚀 Use Railway or Render for fast agency MVPs and automated webhooks.
# ☁️ Use AWS for massive enterprise scaling and strict security compliance.
# 🔍 Always inspect live cloud logs (e.g., `https://railway.app`) to debug.