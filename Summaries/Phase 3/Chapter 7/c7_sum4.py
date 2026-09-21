'''
Chapter7, topic - connecting n8n to external APIs
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# External API -> An application interface window left open for data exchange.
# HTTP Request -> The universal n8n node used to communicate with external web links.
# JSON Response -> The structured, clean key-value text format sent back by servers.

# =====================================================================
# 🚦 THE 5 PILLARS OF N8N API CONNECTIONS
# =====================================================================
# 1. URL Endpoint  -> The digital street address where data lives.
# 2. HTTP Method   -> The action verb:
#                     - GET    : Read / pull data from an external app.
#                     - POST   : Create / push new records out to an app.
#                     - PUT    : Update existing records on the server.
#                     - DELETE : Remove records permanently.
# 3. Auth Headers  -> Your digital passport (e.g., Bearer tokens, API Keys).
# 4. Parameters    -> The fine details (Query parameters or JSON body payloads).
# 5. Data Outcome  -> The incoming JSON package processed by down-stream nodes.

# =====================================================================
# 🛡️ PRODUCTION-GRADE AGENCY CHECKLIST
# =====================================================================
# 🔒 Key Hygiene     -> Never hardcode raw keys; use n8n Credentials or system envs.
# 🏷️ Header Safety   -> Verify 'Content-Type: application/json' is set for POST payloads.
# 🎛️ Traffic Control -> Toggle "Retry on Failure" to handle network dropouts cleanly.
# 🦥 cURL Engine     -> Import raw cURL specs directly to instantly auto-configure nodes.
# 🏷️ Node Semantics  -> Rename nodes logically (e.g., HTTP: Fetch Leads) for clean codebases.
