'''
Chapter4, topic - agents — role, goal, backstory, tools
'''
# =====================================================================
# 🧠 CREWAI AGENT CORE ARCHITECTURE — PRODUCTION CHEAT SHEET
# =====================================================================
# Designed for: Junior Python Automation Devs entering the US Market
# Core Module : crewai.Agent
# Concept     : Shifting generic chat models into deterministic workers.
# =====================================================================

# =====================================================================
# 👔 THE 4 PILLARS OF A ROBUST AGENT
# =====================================================================
# 1. role      -> The specialized corporate job title (e.g., 'Lead Auditor').
#                 Tricks the LLM to access high-quality professional weights.
#
# 2. goal      -> The crisp, metric-driven target starting with an action verb.
#                 Defines WHAT the agent must deliver to prevent wandering.
#
# 3. backstory -> The guardrails establishing corporate persona and rules.
#                 Acts as a text-based firewall to police behavior naturally.
#
# 4. tools     -> List of executable functions allowing physical interactions.
#                 Transforms an AI from a text generator into a system executor.

# =====================================================================
# ⚠️ SENIOR DEV PRODUCTION GUARDRAILS
# =====================================================================
# 🚫 Identity Crisis -> Avoid vague roles. Keep titles hyper-specific.
# 🚫 Tool Bloat      -> Limit tools to 1 or 2 per agent to prevent loops.
# 🚫 Infinite Loops  -> Never use open-ended goals. Always set numerical limits.
# ⚡ Pro-Shortcut    -> Separate text configs into external 'agents.yaml' files.
# ⚡ Performance     -> Keep temperature low (0.0 - 0.2) for analytical tasks.

# =====================================================================
# 🪄 THE AUTOMATION MAGIC SPELL
# =====================================================================
# "If a human intern cannot successfully do the job with your written 
#  instructions, your AI agent will definitely fail too. Be explicit!"
# =====================================================================
