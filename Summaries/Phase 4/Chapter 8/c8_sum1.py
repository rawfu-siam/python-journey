'''
Chapter8, topic - what is LangGraph and when to use it over CrewAI
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# LangGraph -> A Python library for building stateful, multi-actor applications 
#              with LLMs using graphs (nodes, edges, and loops).
# CrewAI    -> An agent framework focused on role-playing agent teams working 
#              together autonomously with minimal setup.
# State     -> The central dictionary schema that holds all pipeline data 
#              as it flows between nodes.
# Node      -> A standard Python function that performs work (e.g., calling an LLM).
# Edge      -> A directional connection telling the graph where data goes next.
# Conditional Edge -> A traffic-cop function that inspects state to decide 
#                     which node to run next (enabling loops and forks).

# =====================================================================
# 🏢 LANGGRAPH VS. CREWAI FACE-OFF
# =====================================================================
# 🤖 CREWAI:
#   - Best for: Autonomous, collaborative team workflows (Researcher/Writer/Editor).
#   - Style: High-level abstraction; agents talk to each other freely.
#   - Control: Less deterministic; harder to enforce strict, looping guardrails.
#
# 🗺️ LANGGRAPH:
#   - Best for: Complex, deterministic, production-grade AI pipelines.
#   - Style: Low-level graph architecture (nodes and edges).
#   - Control: Granular control over state, retries, self-correction, and human approvals.

# =====================================================================
# 🛡️ AGENCY PRODUCTION TIPS
# =====================================================================
# - Always include retry counters in your TypedDict state to prevent infinite loops.
# - Use conditional edges to create self-healing loops (e.g., fix syntax errors).
# - Trace execution flows using LangSmith to debug edge cases in production.