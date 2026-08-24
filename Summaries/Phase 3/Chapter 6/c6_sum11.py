'''
Chapter6, topic - CORS and middleware
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# Middleware -> A global handler layer that sits in front of your API.
#               It intercepts every incoming Request and outgoing Response.
# CORS       -> Cross-Origin Resource Sharing. A browser-enforced security
#               system that defines which outside web addresses are 
#               allowed to send requests and read data from your backend.
#
# =====================================================================
# 🧩 THE PIPELINE RECONSTRUCTION (HOW DATA FLOWS)
# =====================================================================
# [Client Browser] -> (1. CORS Origins Filter) -> (2. Custom Middleware)
#                                                          |
# [JSON Response]  <- (4. Response Tweak)      <- (3. Main API Route)
#
# =====================================================================
# 🛡️ PRODUCTION GUARDRAILS & TRAPS TO AVOID
# =====================================================================
# 1. EXECUTION ORDER: Always add CORSMiddleware at the top of your stack
#    right after instantiating `app = FastAPI()`.
# 2. THE ASYNC TRAP: Forget 'await' on `call_next(request)` and the API 
#    freezes. Always ensure async/await pairings are complete.
# 3. DOMAIN CLEANING: Never include trailing slashes ('/') or paths 
#    inside `allow_origins`. Use clean protocols (e.g., 'https://site.com').
# 4. WILDCARDS: Never use '["*"]' for production client databases. Always
#    isolate explicit client domains using secure environment variables.
# 5. LATENCY CHECKS: Do not perform slow or blocking synchronous operations
#    inside middleware. Use Redis/in-memory caches for fast verifications.
#
# =====================================================================
# 🧪 SENIOR DEVELOPER DESIGN PATTERNS
# =====================================================================
# - "Before" Logic: Placed BEFORE running `await call_next(request)`.
#   Used for logging visits, checking security keys, rate limiting.
# - "After" Logic: Placed AFTER running `await call_next(request)`.
#   Used for timing performance, injecting security headers, compression.
