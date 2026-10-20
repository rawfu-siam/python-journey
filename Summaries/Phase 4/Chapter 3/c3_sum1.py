'''
Chapter3, topic - what are AI agents
'''
# =====================================================================
# 🧠 CORE AGENT DEFINITIONS & MECHANICS
# =====================================================================
# AI Agent   -> An LLM core given a goal, tools, and autonomous power.
# Brain      -> The reasoning model (e.g., GPT-4o) directing the system.
# Tools      -> Code hooks (APIs, DBs) the agent instructs the app to run.
# ReAct Loop -> The core framework pattern: Thought -> Action -> Observation.

# =====================================================================
# 🔄 THE WORKFLOW LOOP STATE MACHINE (CONCEPTUAL PROGRESSION)
# =====================================================================
# 1. GOAL        -> User inputs target (e.g., "Analyze competitor prices")
# 2. THOUGHT     -> Agent evaluates status and devises the next rational step.
# 3. TOOL CALL   -> Agent outputs structured JSON requesting external data.
# 4. EXECUTION   -> Your Python application intercepts JSON and fires the API.
# 5. OBSERVATION -> System feeds raw structural output data back to the LLM.
# 6. RESOLUTION  -> Agent loops until target met, then prints Final Answer.

# =====================================================================
# 🏢 AGENCY-GRADE ARCHITECTURAL SECRETS
# =====================================================================
# 🛡️ Loop Guardrails     -> Set hard boundaries (e.g., max 5 iterations)
#                           to halt infinite token bills if tools fail.
# 📦 Strict Contracts    -> Use Pydantic/JSON schemas for tool execution inputs
#                           instead of relying on erratic raw text parsers.
# 👥 Team Specialization -> Build multi-agent pipelines with discrete roles
#                           rather than a single fragile "do-everything" bot.
# 🤝 Human-in-the-Loop  -> Inject Slack confirmation gates before executing
