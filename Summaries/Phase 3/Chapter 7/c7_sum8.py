'''
Chapter7, topic - combining Python scripts with n8n workflows
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# n8n + Python -> Blending visual orchestrators with custom engine logic.
# n8n          -> Moves the boxes: logistics, app integrations, triggers.
# Python       -> Mutates the contents: regex parsing, AI data processing.
# Universal Link -> JSON payloads passed as Python dictionary structures.
#
# =====================================================================
# 🎛️ THE 3 CODE INTERACTION PATTERNS
# =====================================================================
# 🌐 1. FastAPI Webhooks (Production Standard):
#   - Python operates as an isolated, high-performance API microservice.
#   - n8n dispatches an HTTP POST request containing structured JSON data.
#   - Best for custom library extensions, high security, and easy scaling.
#
# 🐍 2. Native n8n Code Node (Local Sandbox):
#   - Python logic is executed directly inside the web browser sandbox.
#   - Uses internal variable models (e.g., standard item dictionary loops).
#   - Best for fast string operations, formatting, and quick data checks.
#
# 💻 3. Terminal Command Node (Shell Execution):
#   - n8n triggers terminal commands directly via host system shells.
#   - Data is handed over using command-line variables (sys.argv inputs).
#   - Output must be sent out cleanly via print(json.dumps(dictionary)).
#
# =====================================================================
# ⚠️ ARCHITECTURAL GUARDRAILS & COMMON MISTAKES
# =====================================================================
# ❌ The Print Trap      -> Printing loose text logs breaks JSON extraction.
# ❌ Environment Drift  -> Forgetting to call absolute virtual env pathways.
# ❌ Blocking Timeouts  -> Long scripts must use FastAPI BackgroundTasks.
# 🛡️ Self-Healing Rule  -> Always wrap flaky API endpoints in retry frameworks.
#
# =====================================================================
# 🪄 THE ELITE MASTER PHRASE
# =====================================================================
# "n8n moves the boxes; Python mutates the contents." 📦✨
