'''
Chapter4, topic - CrewAI installation and architecture
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# CrewAI      -> A powerful framework to orchestrate collaborative multi-agent teams.
# Agent 🤖     -> The worker persona defined explicitly by a Role, Goal, and Backstory.
# Tool 🛠️      -> Extensible capabilities (e.g., Web Search) given to agents to use.
# Task 📝      -> The explicit work assignment detailing actions and expected outputs.
# Crew 🚢      -> The central container managing the flow of tasks between agents.

# =====================================================================
# ⚙️ SYSTEM INSTALLATION & ENV SETUP
# =====================================================================
# Installation command: pip install crewai crewai-tools
# Always isolate sensitive credentials inside secured environment parameters:
#   os.environ["OPENAI_API_KEY"] = "sk-proj-..."
#   os.environ["SERPER_API_KEY"] = "..."

# =====================================================================
# 🛠️ PRODUCTION PIPELINE BUILD TEMPLATE
# =====================================================================
# from crewai import Agent, Task, Crew, LLM
# from crewai_tools import SerperDevTool
#
# # 1. Define target models explicitly to control cost and velocity
# agency_llm = LLM(model="gpt-4o-mini", temperature=0.1)
# search_tool = SerperDevTool()
#
# # 2. Configure hyper-focused expert personas
# research_agent = Agent(
#     role="Lead Research Analyst",
#     goal="Gather clean market metrics on target companies.",
#     backstory="You are a meticulous auditor who cross-verifies metrics.",
#     tools=[search_tool],
#     llm=agency_llm,
#     max_iter=3 # Safeguard to block infinite token drain loops
# )
#
# # 3. Map discrete operational assignments
# market_task = Task(
#     description="Identify 3 specific pain points of traditional accounting agencies.",
#     expected_output="A bulleted markdown list of explicit pain points.",
#     agent=research_agent,
#     output_file="market_analysis.md" # Automated persistence layer flag
# )
#
# # 4. Execute the structural workflow orchestrator
# production_crew = Crew(
#     agents=[research_agent],
#     tasks=[market_task],
#     verbose=True # Displays real-time operational traces in terminal
# )
# production_crew.kickoff()

# =====================================================================
# 🛡️ THE GOLDEN AGENCY RULE
# =====================================================================
# "Code the workflow framework, prompt the worker's execution."
# Use Python for structural tracks; use rich parameters to guide the AI.
