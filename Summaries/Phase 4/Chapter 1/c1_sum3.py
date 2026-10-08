'''
Chapter1, topic - chat completions — messages, roles, system prompts
'''
# =====================================================================
# 🧠 CORE CHAT COMPLETION ROLES & STRUCTURES
# =====================================================================
# Chat Completion -> A digital ledger passing structured message blocks to the AI brain.
# Payload Shape   -> A list containing dictionaries, where each dict has a role and content.
# Role Types      -> The structural categories that dictate authority and permissions.

# =====================================================================
# 🎭 ROLE CHARACTERISTICS & RESPONSIBILITIES
# =====================================================================
# 👑 SYSTEM ROLE:
#   - Establishes corporate persona, formatting rules, and strict operational laws.
#   - Hidden away from the client or front-end interface entirely.
#   - Acts as the primary security guardrail against malicious input strings.
#
# 👤 USER ROLE:
#   - Represents dynamic incoming strings (customer text, webhooks, or email bodies).
#   - Submits raw data payloads that need processing, parsing, or answering.
#   - Possesses zero operational authority; cannot alter system rules when isolated.
#
# 🤖 ASSISTANT ROLE:
#   - Represents past textual outputs generated directly by the AI model.
#   - Appended back manually into the array by the Python engine to mimic ongoing memory.
#   - Without this, the server treats every single execution turn with absolute amnesia.

# =====================================================================
# 🛠️ PRODUCTION APPLIED AUTOMATION PIPELINES
# =====================================================================
# Determinism     -> Set temperature to 0.0 for strict extraction and formatting workflows.
# Token Control    -> Implement sliding windows using array slicing to drop old history elements.
# Schema Safety   -> Explicitly command the system to bypass text markdown wraps for direct parsing.
