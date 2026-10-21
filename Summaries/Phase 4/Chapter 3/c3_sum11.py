'''
Chapter3, topic - LangServe — deploying LangChain as an API
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & LANGSERVE ARCHITECTURE
# =====================================================================
# LangServe -> A library that wraps LangChain logic into standard FastAPI code.
# Endpoint  -> Specific web paths (`/invoke`, `/stream`) providing API access.
# Playground-> A built-in web-chat interface (`/playground`) for instant testing.
# Remote    -> A tool (`RemoteRunnable`) that lets external scripts call your API.

# =====================================================================
# 🛠️ SERVICE DEPLOYMENT BLUEPRINT
# =====================================================================
# `app = FastAPI()` -> Initializes the underlying high-speed web gateway.
# `add_routes()`    -> Binds prompt-model pipelines directly onto a path.
# `uvicorn.run()`   -> Fires up the production-grade network web worker engine.
# Asynchronous      -> Uses `astream` to feed text tokens back word-by-word.

# =====================================================================
# 🏢 AGENCY PRODUCTION GUARDRAILS
# =====================================================================
# 🔒 CORS Control    -> Restrict origin configurations to block unauthorized apps.
# 🏷️ Input Pydantic  -> Declare explicit schema types to keep routes clean.
# 🧩 Microservices   -> Decouple the AI reasoning core from the primary app database.
# 🔗 Pitch Deliveries-> Deliver the public playground path to clients as a live demo.
