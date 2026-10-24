'''
Chapter7, topic - rate limiting AI endpoints
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & CONCEPTS
# =====================================================================
# Rate Limiting -> Restricting how many requests a user can make to an API
#                  within a specific time window to protect resources.
# HTTP 429      -> The standard status code for "Too Many Requests".
# Time Window   -> The rolling or fixed duration (e.g., 60 seconds) for counting.

# =====================================================================
# ⚙️ MOVING PARTS OF A RATE LIMITER
# =====================================================================
# 1. Identifier -> Tracking the client via IP address, User ID, or API Key.
# 2. Counter    -> Keeping track of how many requests the client made.
# 3. Storage    -> Where counts are saved (In-memory dict vs. Redis cluster).
# 4. Enforcer   -> Logic that blocks requests and returns a 429 error if limit exceeded.

# =====================================================================
# 🏢 AGENCY-GRADE PRODUCTION BEST PRACTICES
# =====================================================================
# 🚫 Avoid In-Memory Dictionaries for Multi-Server Deployments (e.g., Render/AWS)
#    because separate containers won't share state and users can bypass limits.
# 🚀 Use Redis to store rate limit counts centrally across all scaling servers.
# 📦 Use established packages like `slowapi` with simple decorators (`@limiter.limit`).
# 🏷️ Return standard headers (`X-RateLimit-Remaining`, `Retry-After`) so users know
#    precisely when they are cleared to make subsequent API calls.