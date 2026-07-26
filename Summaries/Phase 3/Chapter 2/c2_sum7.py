'''
Chapter2, topic - parsing JSON responses
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# JSON         -> JavaScript Object Notation: Text format used to share data.
# JSON String  -> A raw Python text string ('str') that looks like a dict.
# Parsing      -> Unpacking a raw JSON text string into an actionable object.
# json.loads() -> "Load String" - Converts raw JSON text into a Python Dict/List.
#
# =====================================================================
# 🚰 THE AUTOMATION WORKFLOW
# =====================================================================
# 1. Receive data payload from Webhook/API/LLM as a raw 'str' object.
# 2. Run json.loads(payload) inside a try/except guardrail block.
# 3. Access elements safely using standard dictionary or list operations.
#
# =====================================================================
# ⚠️ COMMON TRAPS & SENIOR SOLUTIONS
# =====================================================================
# ❌ The json.load() Trap -> Missing the 's' causes crashes on string input.
# ❌ Dict Parsing Error   -> Running loads() on a dict object causes a TypeError.
# ❌ Direct Bracket Crash -> Using dict['key'] risk a production KeyError crash.
#
# ✅ The Defensive Move   -> Use dict.get('key', 'default') to safely read data.
# ✅ Exception Guardrail  -> Wrap logic in except json.JSONDecodeError block.
# ✅ Clean Debugging      -> Use json.dumps(data, indent=4) to format messy text.
