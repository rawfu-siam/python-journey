'''
Chapter8, topic - Connecting Python scripts to a Redis instance via redis-py
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# ---------------------------------------------------------------------
# Redis       -> An ultra-fast database residing entirely inside the RAM.
# redis-py    -> The official Python bridge library to translate Python to Redis.
# Host/Port   -> Location identifiers. Standard Redis port is always 6379.
# Byte String -> Default Redis output layout (e.g., b'data'). Requires parsing.

# ⚡ PRODUCTION CONNECTION RULES
# ---------------------------------------------------------------------
# Rule A: Always use decode_responses=True to auto-stringify raw bytes.
# Rule B: Use ConnectionPools for high-traffic apps (FastAPI endpoints).
# Rule C: Isolate your credentials inside a secure, non-committed .env file.
# Rule D: Structure your keys using colons as folders -> 'app:user:101:status'

# =====================================================================
# 🛠️ ENTERPRISE-GRADE SYNTAX REFERENCE SHEET
# =====================================================================
#
# import redis
#
# # Standard baseline connection link:
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
#
# # --- STRINGS (The Basic Sticky Notes) ---
# r.set("key_name", "value_text", ex=300) # Saves key with a 5-minute TTL cache
# value = r.get("key_name")              # Fetches data (returns None if expired)
# r.ping()                               # Connection health-check (True/False)
#
# # --- HASH MAPS (The AI Agent Object/Profile Storage) ---
# profile = {"name": "Siam", "role": "Automation Engineer", "level": "Pro"}
# r.hset("agent:102:profile", mapping=profile)  # Stores an entire dictionary
# role = r.hget("agent:102:profile", "role")   # Extracts single inner value
# data = r.hgetall("agent:102:profile")        # Pulls complete clean dictionary
#
# =====================================================================
# 🪄 THE DEV MINDSET WEB PHRASE: "Set it, forget it, and let it expire!"
# =====================================================================
