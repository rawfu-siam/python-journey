'''
Chapter2, topic - LangChain Expression Language (LCEL)
'''
# =====================================================================
# 🧠 CORE DEFINITIONS: MODERN LCEL WIRING
# =====================================================================
# Runnable           -> The base class that standardizes all LangChain parts.
# Pipe Operator (|)  -> The syntax used to link components into an active stream.
# Handoff Contract   -> The rule where output of block A must match input of block B.

# =====================================================================
# 🏢 SYSTEM FUNCTIONS & STREAM PIPES
# =====================================================================
# 🔄 RunnablePassthrough:
#   - Acts as a bypass valve passing raw text into prompt keys automatically.
#   - Eliminates the need to wrap raw inputs in nested dicts before invoking.
#
# 👥 Dictionary Parallelism (RunnableParallel):
#   - Created by wrapping multiple independent chains inside a standard dict.
#   - LCEL executes all tracks concurrently to maximize API efficiency.
#
# 🛠️ Method Binding (.bind()):
#   - Attach runtime flags directly to the model inside the pipeline structure.
#   - Used for setting engine parameters like stop tokens, temperature, or tools.

# =====================================================================
# ⚠️ SENIOR ARCHITECTURE MATRIX & TIPS
# =====================================================================
# 1. Thread Guard: Always transition to `.ainvoke()` or `.astream()` inside FastAPI.
# 2. Structural Alignment: Keep inputs matching (Prompt expects dict -> Parser outputs str).
# 3. Visual Diagnosis: Turn on LangSmith dashboard tracking to audit complex pipes.
# 4. Engine Cleanliness: Never use legacy runtime wrappers; stay purely inside LCEL syntax.
