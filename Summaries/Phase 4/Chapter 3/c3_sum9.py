'''
Chapter3, topic - agents with memory
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & AGENT MEMORY MECHANICS
# =====================================================================
# Stateless LLM -> Default AI behavior where each prompt has complete amnesia.
# Memory Buffer -> The active temporary workspace catching live conversational text.
# Storage        -> The database infrastructure (RAM, SQLite, Redis) saving chat logs.
# Context Window -> The strict token limit filtering out old logs to optimize costs.

# =====================================================================
# 🛠️ MEMORY IMPLEMENTATION FLAVORS
# =====================================================================
# ⏱️ Ephemeral (Short-Term):
#   - Stored in server RAM (`ChatMessageHistory`).
#   - Lightning fast, but completely wipes out if script crashes or restarts.
#
# 🛡️ Persistent (Enterprise):
#   - Stored in a durable database structure (`SQLChatMessageHistory`).
#   - Survived server reboots and maps history to unique `session_id` tokens.
#   - Critical for multi-user web apps to prevent private data leakage.

# =====================================================================
# 🏢 AGENCY PRODUCTION GUARDRAILS
# =====================================================================
# ✂️ Token Trimming  -> Use `trim_messages` to prevent exploding API bills.
# 🔑 Session Locking -> Always isolate data using strict database routing keys.
# 📝 State Audit     -> Expose memory tracks to a dashboard for easy client debugging.
