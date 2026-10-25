'''
Chapter8, topic - State management — defining and updating the overall GraphState
'''
# =====================================================================
# 🧠 CORE DEFINITIONS: STATE MANAGEMENT
# =====================================================================
# GraphState  -> The shared central memory notebook carrying data 
#              through all nodes in a LangGraph workflow.
# TypedDict   -> A Python structural blueprint enforcing strict key 
#              names and data types for your state schema.
# Reducer     -> A rule (like operator.add) controlling how new state updates 
#              merge with existing data (e.g., appending to a list instead of overwriting).

# =====================================================================
# 🏢 AGENCY PRODUCTION TIPS & GUARDRAILS
# =====================================================================
# - Always use Annotated[List, operator.add] for message history or logs to prevent data loss.
# - Return clean dictionary updates from nodes instead of mutating state objects directly.
# - Keep state schemas lightweight by storing IDs or text snippets rather than heavy objects.
# - Stick to flat, basic Python types (str, int, bool, list) for easy debugging.