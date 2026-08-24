'''
Chapter6, topic - deploying FastAPI to Railway or Render
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# Deployment -> Moving code from your local laptop to a 24/7 cloud server.
# Railway    -> A cloud provider that clones your GitHub repo and runs it live.
# Render     -> A cloud platform that converts your code into public web URLs.
# Port       -> The communication pipe. Cloud uses a dynamic $PORT environment variable.
# Host       -> The network listener. Must be set to 0.0.0.0 to accept global traffic.

# =====================================================================
# 🏢 LOCAL VS. CLOUD PRODUCTION FACE-OFF
# =====================================================================
# 💻 LOCAL HOSTING:
#   - Runs on loopback URL paths (e.g., http://127.0.0.1:8000).
#   - Shuts down completely the moment you close your laptop lid.
#   - Hidden from the public internet. No external webhooks can connect.
#
# ☁️ CLOUD DEPLOYMENT:
#   - Runs on global listening paths using uvicorn main:app --host 0.0.0.0.
#   - Stays awake 24/7/365 to handle client automation workflows automatically.
#   - Generates a permanent public URL (e.g., https://onrender.com).
#   - Safe Credential Hygiene: Uses os.environ.get() instead of raw hardcoded keys.
#   - Requires a strict infrastructure file setup: Procfile and requirements.txt.
