'''
Chapter4, topic - CrewAI with LangChain tools
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & INTENTIONAL ALIGNMENT
# =====================================================================
# CrewAI Agent  -> The corporate worker brain. Capable of thought and execution, 
#                  but blind to real-time internet data out-of-the-box.
# LangChain Tool -> Pre-engineered physical utility gadgets (e.g., search engine lenses,
#                  file parsers) that connect LLM brains to external software environments.
# Adapter Engine -> The structural bridge (`LangchainTool`) required to convert a native
#                  LangChain object syntax into a valid, readable CrewAI tool list object.
#
# =====================================================================
# 🎯 THE BUSINESS STRATEGY & REAL-WORLD VALUE
# =====================================================================
# 1. Cost Containment: Uncapped search queries flood agent context windows. Clamping
#    tool outputs using parameters like `max_results=2` preserves critical agency API margins.
# 2. Strategic Laziness: Utilizing pre-verified enterprise tools prevents developers from 
#    wasting weeks writing brittle, custom scrapers that fail when CSS attributes change.
# 3. Security Isolation: API credentials (`TAVILY_API_KEY`) must never be hardcoded. 
#    Production code imports parameters via environment variables using `os.getenv()`.
#
# =====================================================================
# 🧩 STRUCTURAL ANATOMY OF AN INTEGRATION PIPELINE
# =====================================================================
# Step 1: Import -> Pull the raw tool package from `langchain_community.tools`.
# Step 2: Adapt  -> Wrap the instance inside CrewAI's adapter module: `LangchainTool(tool=...)`.
# Step 3: Belting -> Inject the adapted tool into the targeted Agent's `tools=[...]` property list.
# Step 4: Shielding -> Attach optional Pydantic contracts to `args_schema` to lock down tool arguments.
#
# =====================================================================
# ⚠️ THE JUNIOR TRAPS & DANGER SHIELDS
# =====================================================================
# ❌ The Direct Explode: Passing raw LangChain items into a Crew array crashes immediately.
#    ✅ The Solution: Always pass the raw tool object through the `LangchainTool` class wrapper.
#
# ❌ Agent Overwhelm: Arming every single agent with a massive array of tools causes chaos.
#    ✅ The Solution: Enforce the Principle of Least Privilege. Only hand tools to specific workers.
#
# ❌ Monolithic Architecture: Shoving tool initialization directly inside the crew setup block.
#    ✅ The Solution: Build a separate `utils/tools.py` utility module for high architectural reuse.
#
# =====================================================================
# 🔮 THE BACKSTAGE MAGIC SPELL & SENIOR PHILOSOPHY
# =====================================================================
# "Give an Agent a goal and it will think; give an Agent an adapted tool and it will act."
# High-velocity developers optimize for output volume with minimal custom codebase overhead.
