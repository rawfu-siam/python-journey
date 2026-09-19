'''
Chapter8, topic - Cachetools library — TTL (Time-To-Live) and 
                  LRU (Least Recently Used) caching
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & CACHING FUNDAMENTALS
# =====================================================================
# Cache     -> A ultra-fast, temporary notepad in RAM for storing repetitive results.
# Hit       -> When your code finds the answer instantly inside the cache notepad.
# Miss      -> When the cache is empty, forcing code to execute slow database/API logic.
# Decorator -> The `@` symbol shortcut used to wrap functions with caching guardrails.

# =====================================================================
# 🛠️ THE CACHETOOLS WORKHORSES: TTL VS. LRU
# =====================================================================
# ⏳ TTL (Time-To-Live):
#   - Tracks an expiration countdown clock for every single item stored.
#   - Automatically purges an entry when its timer hits zero.
#   - Perfect for stopping redundant API charges on moderately fresh data.
#
# 🧹 LRU (Least Recently Used):
#   - Tracks data based on popularity and access frequency.
#   - When capacity hits `maxsize`, it drops the least-looked-at item.
#   - Perfect for strict memory budgets to prevent server crashes.

# =====================================================================
# ⚠️ CACHING PITFALLS & PRODUCTION GUARDRAILS
# =====================================================================
# 🥬 Stale Data -> Setting a TTL too high causes users to see outdated information.
# 💥 Unhashable  -> Passing mutable lists `[]` or dicts `{}` as parameters crashes the cache.
# 👻 Unbounded  -> Forgetting to set a strict `maxsize` triggers Out-Of-Memory container drops.

# =====================================================================
# 🎬 THE PROS' GOLDEN RULES & SHORTCUTS
# =====================================================================
# 📦 Native Shortcut -> `from functools import lru_cache` provides free size-based caching.
# 🧙‍♂️ The Philosophy   -> Write exactly 1 line of decorator code to skip thousands of API steps.
# 🪄 The Magic Spell  -> "If the data hasn't changed, don't move the wires."
