'''
Chapter5, topic - Field validation guardrails — string lengths, numerical ranges, regex matching
'''
# =====================================================================
# 🧠 FIELD VALIDATION GUARDRAILS — CORE DEFINITIONS
# =====================================================================
# Field Validation Guardrails -> Security filters for incoming data.
# String Lengths              -> Limits for text size (`min_length`, `max_length`).
# Numerical Ranges            -> Safe boundaries for numbers (`ge`, `le`).
# Regex Pattern Matching      -> Exact character sequence enforcement (`pattern`).

# =====================================================================
# 📏 STRING LENGTH GUARDRAILS
# =====================================================================
#   - `min_length`: Ensures text is at least N characters long (prevents empty strings).
#   - `max_length`: Ensures text does not exceed N characters (prevents memory/buffer overflow).
#   - Example: `username: str = Field(min_length=3, max_length=15)`

# =====================================================================
# 🔢 NUMERICAL RANGE GUARDRAILS
# =====================================================================
#   - `ge` (Greater than or Equal to ≥): Sets the minimum numerical limit.
#   - `le` (Less than or Equal to ≤): Sets the maximum numerical limit.
#   - Example: `temperature: int = Field(ge=0, le=100)`

# =====================================================================
# 🕵️‍♂️ REGEX PATTERN MATCHING GUARDRAILS
# =====================================================================
#   - `pattern`: Forces text to match a regular expression format string.
#   - Always use raw strings (`r"..."`) to avoid backslash translation bugs.
#   - Example: `task_id: str = Field(pattern=r"^TASK-\\d+$")`

# =====================================================================
# 🏢 AGENCY BEST PRACTICES
# =====================================================================
#   - Centralize validation models in a clean `schemas.py` file.
#   - Catch `ValidationError` gracefully instead of letting apps crash.
#   - Let Pydantic handle validation automatically instead of manual `if/else`.
#   - "Define the shape once, trust the data forever."
