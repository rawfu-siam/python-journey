'''
Chapter6, topic - background tasks in FastAPI
'''
# =====================================================================
# 🧠 1. CORE ARCHITECTURAL DEFINITIONS
# =====================================================================
# Background Task  -> A non-blocking operation executed AFTER an API 
#                     sends its immediate HTTP response back to the client.
#
# Non-Blocking Code -> Scripts that execute asynchronously or in a separate 
#                     thread, preventing user interface freeze/timeouts.
#
# Task Truck       -> The 'BackgroundTasks' dependency injection class 
#                     provided by FastAPI to manage the background queue.
#
# The Task Chef    -> The standard Python function containing the slow,
#                     heavy, or third-party automated pipeline work.

# =====================================================================
# 🏢 REAL-WORLD BUSINESS APPLICATION MAP
# =====================================================================
# 📬 SCENARIO A: BLOCKING FLOW (Do NOT use Background Tasks)
#   - Action: User enters credentials to log in.
#   - Reason: User cannot proceed without immediate authentication verification.
#   - Design: Synchronous or inline await validation.
#
# 🚀 SCENARIO B: NON-BLOCKING FLOW (Mandatory Background Tasks)
#   - Action: Processing a CSV lead sheet, sending Slack alerts, firing LLMs.
#   - Reason: Operations take 3 to 60+ seconds. Web browsers drop connections.
#   - Design: Return '{"status": "processing"}' instantly. Run logic in background.

# =====================================================================
# ⚠️ THE JUNIOR ENG TRAPS & SENIOR GUARDRAILS
# =====================================================================
# ❌ TRAP 1: The Parentheses Execution Error
#   - background_tasks.add_task(my_worker_function(email))
#   - Result: Runs immediately, blocks the response loop, defeats the purpose.
#
# ✅ FIX 1: Pass Reference Separately
#   - background_tasks.add_task(my_worker_function, email)
#
# ❌ TRAP 2: The Silent Error Death
#   - Background workers execute independently from the active request scope.
#   - Unhandled exceptions crash the thread silently without alert triggers.
#
# ✅ FIX 2: Universal Try/Except Wrappers
#   - Always encompass your background worker logic inside error guardrails.
#   - Pipe exceptions directly into logging modules or remote Slack webhooks.

# =====================================================================
# 🧪 SENIOR CODE HIGHLIGHTS FOR AGENCY CODE REVIEWS
# =====================================================================
# 1. Clean Architecture: Keep main.py thin. Import workers from /tasks.
# 2. Data Safety     : Pass raw primitives (str, int) into tasks.
#                      Never pass live DB sessions across worker scopes.
# 3. Task Chaining   : Call .add_task() multiple times inside one endpoint
#                      to build sequential automated data pipelines.
# =====================================================================
