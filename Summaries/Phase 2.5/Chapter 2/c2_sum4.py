'''
Chapter2, topic - Stream handlers (console output) vs File handlers (persistent storage)
'''
# =====================================================================
# 🧠 CORE LOGGING ARCHITECTURE DEFINITIONS
# =====================================================================
# Handlers     -> The delivery system deciding WHERE log data goes.
# StreamHandler-> Real-time, interactive, but completely volatile screen log.
# FileHandler  -> Permanent, disk-backed, non-volatile text log file storage.
# Formatter    -> Layout parser injecting structural context (times, lines).

# =====================================================================
# 📊 STREAM HANDLER VS. FILE HANDLER FACE-OFF
# =====================================================================
# 📺 STREAM HANDLER (Console Output):
#   - Piped directly to standard terminal display engines (sys.stdout).
#   - Highly efficient for rapid debugging cycles during local development.
#   - Volatile: Closing the active shell or instance wipes data instantly.
#
# 💾 FILE HANDLER (Persistent Storage):
#   - Appended explicitly onto the physical storage disk (e.g., app.log).
#   - Essential for background workers running headless on cloud servers.
#   - Creates immutable historical audit ledgers and incident records.

# =====================================================================
# 🛡️ ENTERPRISE GUARDRAILS & DESIGN RULES
# =====================================================================
# 1. Unicode Safety  -> Always enforce encoding="utf-8" inside file handles.
# 2. Duplicate Check  -> Use "if not logger.handlers:" to stop repeating outputs.
# 3. Stream Routing  -> Explicitly direct console streams using sys.stdout.
# 4. Zero Prints      -> Eliminate all native print() calls in production code.
