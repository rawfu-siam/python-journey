'''
Chapter3, topic - ReAct agent pattern
'''
# =====================================================================
# 🧠 CORE RECLASS DEFINITIONS: THE ReAct PATTERN
# =====================================================================
# ReAct Pattern -> Reasoning (Thinking) + Acting (Executing external tools).
# Thought       -> The agent's step-by-step internal reasoning log.
# Action        -> The deliberate tool selection + parameter generation step.
# Observation   -> The raw data output returned after executing the tool.
# Final Answer  -> The exit condition when the user query is fully resolved.

# =====================================================================
# 🛡️ PRODUCTION GUARDRAILS & DESIGN PRINCIPLES
# =====================================================================
# 📝 Explicit Docstrings:
#   - Tool docstrings are treated as direct prompt instructions by the LLM.
#   - Must define the tool's purpose, exact argument shape, and expected types.
#
# 🛑 Financial & Execution Protection:
#   - Always set `max_iterations` to prevent infinite text-parsing loops.
#   - Infinite loops run up heavy API token costs in automated pipelines.
#
# 🤝 Human-in-the-Loop (HITL) Protocol:
#   - Never let an autonomous agent execute destructive real-world actions.
#   - Route high-risk payloads (orders, deletes) to a Slack approval block first.

# =====================================================================
# 🛠️ MINIMAL CODE ARCHITECTURE REFERENCE
# =====================================================================
# @tool
# def custom_tool(param: type) -> str:
#     """Detailed description telling the AI exactly when to run this."""
#     return "Result string injected back as an Observation"
#
# llm = ChatOpenAI(model="gpt-4o", temperature=0)
# agent = create_react_agent(llm, tools=[custom_tool], prompt=hub_pull_prompt)
# executor = AgentExecutor(agent=agent, tools=tools, max_iterations=5)
# executor.invoke({"input": "Your query"})
