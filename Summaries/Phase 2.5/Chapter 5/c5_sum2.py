'''
Chapter5, topic - Type enforcement, coercion, and automatic casting
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# Type Enforcement -> Strict rule making to block invalid data types from entering.
# Type Coercion    -> Automatic conversion of compatible types (e.g., "5" -> 5).
# Pydantic Model   -> A data blueprint that enforces types and casts automatically.

# =====================================================================
# 🛡️ THE DATA GUARDRAILS & CASTING RULES
# =====================================================================
# 📋 Type Hints:
#   - Declares what data shape is expected (int, float, bool, str).
#
# 🪄 Automatic Coercion Rules:
#   - Strings of numbers (e.g., "42") cast to integers/floats.
#   - Truthy words/numbers ("yes", "1", "true") cast to Boolean `True`.
#   - Falsy words/numbers ("no", "0", "false") cast to Boolean `False`.
#
# ⚠️ Error Handling & Pro Tips:
#   - Un-castable text throws `ValidationError` and must be caught safely.
#   - Use `@field_validator(mode='before')` to clean prefixes like `$` or `,` 
#     before Pydantic attempts its standard type casting.
