'''
Chapter1, topic - Writing explicit engineering issues with functional specs
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# Explicit Issue -> A digital task card with zero guessing room.
# Functional Spec -> A written recipe defining data shapes and rules.
# Scope Creep     -> Adding extra features not requested in the task.

# =====================================================================
# 🦴 THE 5 VITAL PARTS OF AN ISSUE TICKET
# =====================================================================
# 🏷️ TITLE & ID:
#   - Unique code connecting code changes to tracking systems.
#   - Example: `[AUTO-102] Create Rotating App Logger Utility`.
#
# 👤 USER STORY:
#   - Written using formula: As a [Role], I want [Feature] so [Benefit].
#   - Helps the developer understand the real-world business reason.
#
# 📋 FUNCTIONAL SPECS:
#   - Strict layout detailing exact inputs, business logic, and outputs.
#   - Dictates how strings are modified, formatted, or calculated.
#
# 🚧 EDGE CASE GUARDRAILS:
#   - Instructions on how the code must react when data is corrupt.
#   - Prevents silent script deaths by handling exceptions cleanly.
#
# 🏁 DEFINITION OF DONE:
#   - A checklist proving the task matches the requested goals.
#   - Must be fully ticked before dragging card to 'Done' column.

# =====================================================================
# 🇦🇺🇸🇬 THE AGENCY WORKFLOW BLUEPRINT
# =====================================================================
# 🪄 THE MAGIC SPELL:
#   - "If it isn't in the spec, it doesn't exist in the code."
#
# ⏱️ THE 2-HOUR RULE:
#   - If stuck on a requirement for 2 hours, ask on the ticket.
#   - Never struggle in silence; communicate asynchronously.
#
# ⚛️ ATOMIC CODING:
#   - Write type hints and explicit docstrings mentioning issue IDs.
#   - Keep functions small. One function handles one rule.
