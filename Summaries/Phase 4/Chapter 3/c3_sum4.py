'''
Chapter3, topic - building custom tools for agents
'''
# =====================================================================
# 🧠 CORE CUSTOM TOOL DEFINITIONS
# =====================================================================
# @tool Decorator -> Transforms any standard Python function into an AI superpower.
# Docstring (""") -> The absolute instruction manual read by the agent's brain.
# Type Hints (:)  -> Rigid data definitions forcing the LLM to format inputs correctly.
# Text Output     -> Flat strings or text-JSON returned as an explicit Observation.

# =====================================================================
# 🏢 AGENCY-GRADE ARCHITECTURE LAWS
# =====================================================================
# 🎯 Tool-Trigger Rule:
#   - Keep docstrings focused entirely on the real-world trigger conditions.
#   - Focus on WHAT problem it solves, not HOW the inner code is written.
#
# 🛡️ The Isolation Rule (Senior Secret):
#   - Never cram long, dirty business logic inside the tool wrapper function.
#   - Build pure Python service files first; import and call them inside the tool.
#
# 🛡️ Data & Crash Protections:
#   - Always wrap tool operations inside try-except blocks.
#   - Convert raw code exceptions into flat, explanatory string warning messages.
#   - Use Pydantic schemas (`args_schema`) when tools require multiple variables.

# =====================================================================
# 🛠️ QUICK REUSABLE TEMPLATE MATRIX
# =====================================================================
# from langchain.core.tools import tool
# from pydantic import BaseModel, Field
#
# class ToolSchemaInput(BaseModel):
#     item_id: str = Field(description="Must match exact corporate ID rules.")
#
# @tool("corporate_tool_name", args_schema=ToolSchemaInput)
# def enterprise_tool_wrapper(item_id: str) -> str:
#     """Trigger this tool whenever the user requests automated asset tracking actions."""
#     try:
#         # Call separate isolated service logic layer here
#         return "Clean string data returned to the agent's context window."
#     except Exception as err:
#         return f"Execution failed cleanly: {str(err)}. Inform user."
