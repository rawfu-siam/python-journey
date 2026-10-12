'''
Chapter4, topic - custom tools for CrewAI agents
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & BASIC UNDERSTANDING 
# =====================================================================
# Custom Tool -> A piece of your own Python code packaged nicely so an 
#                AI agent can run it to interact with the real world.
# Brain Bubble-> AI agents are great at text, but trapped. Tools act as a
#                digital bridge letting them leave their bubble to do work.
# The Protocol-> The agent reads the tool's name and instructions to decide
#                autonomously whether it needs to fire your code.

# =====================================================================
# 🏢 THE REAL-WORLD BUSINESS VALUE 
# =====================================================================
# • Zero Hallucinations: Keeps calculations accurate (LLMs fail at hard math).
# • Private System Access: Lets agents query internal enterprise databases.
# • Custom Integration: Connects workflows to unique client API endpoints.
# • Automation Output: Transforms basic chatbots into high-value active workers.

# =====================================================================
# 🧩 ANATOMY OF A PERFECT DECORATOR TOOL 
# =====================================================================
# 1. `@tool("Name")`  -> The magic stamp turning normal code into an AI widget.
# 2. Function Name    -> Clear, descriptive, action-oriented (e.g., fetch_data).
# 3. Type Hints       -> Explicit parameter styling rules (e.g., input_str: str).
# 4. Detailed Docstring-> The instruction manual the LLM reads before clicking.
# 5. String Return    -> The final data payload converted into a plain text string.

# =====================================================================
# ⚠️ THE JUNIOR TRAPS TO AVOID 
# =====================================================================
# ❌ Vague Docstrings: Writing summary comments that don't explain the "when".
# ❌ Complex Objects: Returning raw SQL engines or object instances instead of strings.
# ❌ Silent Death:   Forgetting try/except wrappers, causing script crashes on error.

# =====================================================================
# 🎬 THE SENIOR DEV SHORTCUTS & AGENCY EXPECTATIONS 
# =====================================================================
# • The Quick Conversion: Use `Tool.from_function()` to wrap old code in 1 line.
# • The Smart Lazy Rule:  Pull raw data out, let the LLM format it via prompts.
# • Golden Catchphrase:   "If an LLM can't do it with raw text, build a tool; 
#                          if a tool can do it, don't make the LLM guess."
# • Agency Guardrails:    Keep tools small, secure API tokens inside a hidden `.env`,
#                          and use structured logging instead of naked print statements.
