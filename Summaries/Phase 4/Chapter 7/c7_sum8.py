'''
Chapter7, topic - cost optimization — caching, batching
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & CONCEPTS
# =====================================================================
# Caching     -> Reusing saved past AI answers to avoid repeat API costs.
# Batching    -> Grouping multiple small tasks into a single request.
# TTL (Timer) -> Expiration rule determining how long data stays cached.

# =====================================================================
# ⚙️ MOVING PARTS OF OPTIMIZATION
# =====================================================================
# 1. Memory Store -> A Python dictionary or Redis database holding answers.
# 2. Cache Key    -> The unique text identifier used to check for matches.
# 3. Batch Queue  -> Grouping mechanism for bulk API processing.

# =====================================================================
# 🏢 AGENCY-GRADE PRODUCTION BEST PRACTICES
# =====================================================================
# 🚫 Avoid infinite caches that serve outdated data or broken keys with timestamps.
# 🛡️ Normalize text (lowercase, strip spaces) so slightly varied prompts match.
# 🚀 Use Redis (e.g., `https://redis.io`) for production-grade persistent caching.
# 💰 Optimize API token usage to maximize agency profit margins on client projects.