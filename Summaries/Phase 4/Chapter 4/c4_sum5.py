'''
Chapter4, topic - crew — process types (sequential, hierarchical)
'''
# =====================================================================
# 🧠 CREWAI PROCESS TYPES: WORKFLOW ENGINE CHEAT SHEET
# =====================================================================
# 🏃‍♂️ 1. SEQUENTIAL PROCESS DEFINITION
# ---------------------------------------------------------------------
# - The default workflow engine in CrewAI.
# - Executes tasks one after another in a strict, straight line.
# - Follows the exact order defined in the Crew's `tasks` list.
# - Output from Task N cascades automatically as context into Task N+1.
# - Ideal for: Fixed, predictable, step-by-step automation pipelines.
#   (e.g., Scrape Data -> Summarize Text -> Save to SQLite database)

# 👑 2. HIERARCHICAL PROCESS DEFINITION
# ---------------------------------------------------------------------
# - Mimics a corporate ladder or movie set directed by a manager.
# - Requires setting `process=Process.hierarchical` in the Crew.
# - CRITICAL REQUIREMENT: Must be supplied with a `manager_llm` instance.
# - Tasks are NOT hardcoded to individual agents (`agent=...` is omitted).
# - The Manager LLM reads worker roles/goals and routes tasks dynamically.
# - The Manager inspects quality and can force agents to redo subpar work.
# - Ideal for: Complex, subjective, or open-ended business objectives.
#   (e.g., Code Review, Competitor Analysis, Strategic Problem Solving)

# 💰 3. AGENCY-GRADE BUDGET & ARCHITECTURE OPTIMIZATION
# ---------------------------------------------------------------------
# - THE MIXED-LLM ENGINE H-A-C-K:
#   - Set an elite, high-reasoning model (e.g., gpt-4o) as the `manager_llm`.
#   - Set ultra-cheap, fast models (e.g., gpt-4o-mini) for the worker agents.
#   - Result: Maximizes managerial control while cutting token bills by ~70%.
#
# - THE EMERGENCE KILL-SWITCH:
#   - Always set `max_iter` constraints on agents to break infinite loops.
#   - Use `allow_delegation=False` on pure technical execution specialists
#     to block them from passing the buck and generating token waste.

# =====================================================================
# 🪄 THE WORKFLOW MAGIC SPELL:
# "If the steps are a fixed checklist, run a Sequential line;
#  if the steps need a supervisor's eye, let a Hierarchical Manager shine."
# =====================================================================
