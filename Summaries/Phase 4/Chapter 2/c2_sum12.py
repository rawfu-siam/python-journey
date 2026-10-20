'''
Chapter2, topic - memory — ConversationBufferMemory, SummaryMemory
'''
# =====================================================================
# 🧠 CORE MEMORY DEFINITIONS
# =====================================================================
# Stateless    -> The native design of LLMs; they forget past inputs instantly.
# Message Turn -> A single set of paired exchanges between a Human and the AI.
# Buffer Array -> An exact, verbatim script log of the conversation turns.
# Context Map  -> A condensed summary log that preserves the key facts.

# =====================================================================
# 🗛 MEMORY ENGINES FACE-OFF
# =====================================================================
# 🪵 ConversationBufferMemory:
#   - Retains word-for-word accuracy of all previous text exchanges.
#   - Token cost grows exponentially with each back-and-forth turn.
#   - Best for short support chats where exact phrasing is required.
#
# ✂️ ConversationSummaryMemory:
#   - Uses an background LLM to update a running context summary sheet.
#   - Token cost stays flat, preventing context window crashes.
#   - Best for long consultation bots or multi-turn agent pipelines.

# =====================================================================
# 🛡️ PRODUCTION AGENCY ARCHITECTURE BLUEPRINT
# =====================================================================
# 🔒 Session Separation -> Bind history to a secure session_id to isolate data.
# 🛑 Token Window Guard -> Wrap history in a Token Buffer to cap max token cost.
# 💾 DB Persistence     -> Connect to external databases like Redis or local JSON.
# ❄️ Zero Temperature   -> Run background summary models at temp=0 to prevent hallucinations.
