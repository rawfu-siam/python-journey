'''
Chapter3, topic - LangChain tools — built-in and custom
'''
# =====================================================================
# 🧠 CORE LANGCHAIN TOOL DEFINITIONS
# =====================================================================
# Tool          -> A Python wrapper giving an LLM "hands" to act.
# Built-in Tool -> Pre-made ecosystem integrations (e.g., Wikipedia).
# Custom Tool   -> Tailored Python code you write to run unique tasks.
# Args Schema   -> Pydantic blueprints enforcing data validation guardrails.

# =====================================================================
# 🧩 THE FOUR PILLARS OF A SECURE TOOL CONTRACT
# =====================================================================
# 🏷️ name        -> Rigid alphanumeric snake_case tool identifier.
# 📝 description -> In-depth English string explaining *when* to execute.
# 📐 args_schema  -> Strict Pydantic model dictating variable types.
# 🐍 core_func    -> The actual functional script returning text outputs.

# =====================================================================
# 🏢 AGENCY-GRADE TOOL SECRETS & ARCHITECTURE
# =====================================================================
# 📝 Docstring Prompts -> The LLM reads function docstrings directly.
#                         Make them hyper-clear to prevent hallucination.
# 🧵 Flat Text Return  -> Tools must ALWAYS return raw, clean strings.
#                         LLMs cannot parse complex objects or references.
# 🩹 Self-Healing Logs -> Catch script exceptions using try/except blocks.
#                         Return errors as strings so the agent can retry.
# 🛡️ Pydantic Shields  -> Use StructuredTool pipelines to enforce type
#                         coercion and keep corrupt payloads out of DBs.
