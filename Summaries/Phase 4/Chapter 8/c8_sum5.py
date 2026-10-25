'''
Chapter8, topic - State persistence — implementing memory checkpoints and threads
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & CONCEPTS
# =====================================================================
# State Persistence -> Saving conversation history & agent states permanently.
# Checkpointer      -> The utility that automatically takes snapshots of state.
# Thread ID         -> A unique label separating individual user sessions.
# Config Dictionary -> A wrapper payload holding the thread identifier.

# =====================================================================
# 🏗️ ARCHITECTURE PATTERNS & SETUP
# =====================================================================
# TypedDict         -> Defines the exact schema shape for state data.
# StateGraph        -> The workflow builder mapping nodes and transitions.
# MemorySaver       -> In-memory checkpointer for local testing & development.
# Persistent DB     -> Production checkpointer (e.g., Postgres, Redis) for scale.

# =====================================================================
# 🚀 AGENCY BEST PRACTICES & PRODUCTION TIPS
# =====================================================================
# Dynamic IDs       -> Generate unique UUIDs per client session dynamically.
# Isolation         -> Ensure thread IDs never mix up multiple users' data.
# Server Reboots    -> Use durable storage so chat histories survive restarts.
# API Routing       -> Pass config dictionaries securely through endpoints.