'''
Chapter4, topic - agent collaboration and delegation
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# Agent Collaboration -> Multiple specialized AI agents passing data 
#                         and sharing notes to complete a single project.
# Agent Delegation    -> An agent autonomously transferring a specific 
#                         sub-task to a teammate who has better tools/skills.
#
# =====================================================================
# ⚙️ KEY CONFIGURATION PARAMETERS IN CREWAI
# =====================================================================
# allow_delegation=True  -> Explicitly grants permission to the agent 
#                           to ask other crew members for help.
# allow_delegation=False -> Restricts the agent to a 'lone wolf' status;
#                           forces it to solve the task using only its parameters.
# context=[prior_task]   -> Manually links tasks together, serving as a 
#                           baton pass where output data runs downstream.
# verbose=True           -> Turns on terminal telemetry so you can read
#                           the real-time inner dialogue of the agents.
#
# =====================================================================
# 🛡️ AGENCY-GRADE PITFALLS & SOLUTIONS
# =====================================================================
# ❌ The Delegation Loop: Agents passing the same question infinitely.
#    ✔️ Fix: Only allow delegation on high-level coordinator agents.
#
# ❌ Tool Ambiguity: Giving every agent access to the entire toolbelt.
#    ✔️ Fix: Enforce isolation. Give specific tools only to the specialist.
#
# ❌ Token Bleeding: Running massive premium models during route testing.
#    ✔️ Fix: Test collaboration paths using cheap models (gpt-4o-mini).
#
# =====================================================================
# 🪄 THE SENIOR DEV GOLDEN SPELL
# =====================================================================
# "Role dictates goal, tools dictate actions, and delegation solves bottlenecks."
# Use Process.hierarchical to make a boss agent manage everything for you!
