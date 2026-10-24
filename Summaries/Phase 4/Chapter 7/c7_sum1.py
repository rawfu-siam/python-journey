'''
Chapter7, topic - AI product architecture — backend + frontend + AI
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# Frontend -> What the user sees and clicks in their web browser.
# Backend  -> The secure server logic that processes requests.
# AI Layer -> The external model brain providing smart responses.

# =====================================================================
# 🏗️ THE 4-PART PRODUCT LAYERS
# =====================================================================
# 1. Interface -> HTML/JS browser elements for user inputs & buttons.
# 2. Server    -> FastAPI routes handling incoming client payloads.
# 3. Model     -> Secure API connection sending prompts to OpenAI.
# 4. Storage   -> Persistent database tracking profiles and chats.

# =====================================================================
# 🛡️ PRODUCTION GUARDRAILS & SENIOR SECRETS
# =====================================================================
# - Hide API keys: Keep secrets on the backend, never in frontend JS.
# - Separate concerns: Keep UI, server logic, and AI code modular.
# - Scale up: Transition to modern frameworks like React or Next.js.
# - Enable CORS: Configure server headers for secure browser communication.