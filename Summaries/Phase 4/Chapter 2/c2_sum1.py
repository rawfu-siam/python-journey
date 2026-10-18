'''
Chapter2, topic - what is LangChain and why it exists
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# LangChain     -> A structured Python framework that connects AI brains to real tools.
# LLM Wrapper   -> A unified bridge letting you swap model vendors without breaking code.
# Prompt Template-> A reusable blueprint defining structural instructions for the AI.
# LCEL          -> LangChain Expression Language using the pipe operator (|) to chain steps.
# Vector DB     -> A specialized database storing private client data as math coordinates.
# AI Agent      -> An autonomous AI brain that decides which tools to use on the fly.
# Stateful      -> System architecture that remembers context across multiple chat turns.
# Stateless     -> System architecture that forgets transactions immediately after completion.

# =====================================================================
# 🏢 RAW MODEL API VS. LANGCHAIN FACE-OFF
# =====================================================================
# 📬 RAW API CALLS:
#   - Requires writing custom, repetitive connection wrappers per vendor (OpenAI, Claude).
#   - Every turn is stateless. Models forget past interactions completely out of the box.
#   - Developer manually handles token limits, regex text cleaning, and error handling.
#   - Hard to scale when building sequential multi-step automations for real businesses.
#
# 🛍️ LANGCHAIN PIPELINES:
#   - Swaps underlying model vendors instantly by changing just a single class setting.
#   - Locks prompts, models, and output parsers together using clean, readable pipe lines.
#   - Automates memory state tracking, background document loading, and tool execution.
#   - Provides enterprise blueprints for data searching (RAG) and self-healing agent workflows.

# =====================================================================
# 🛡️ THE SIX PILLARS OF LANGCHAIN AUTOMATION
# =====================================================================
# 1. Model I/O     -> Manages prompts, chat configurations, and raw text extraction.
# 2. Retrieval     -> Loads documents (PDFs, URLs), splits them, and searches vector stores.
# 3. Chains (LCEL) -> Links independent processing steps into one smooth conveyor belt.
# 4. Memory        -> Persists past conversation threads behind the scenes automatically.
# 5. Agents        -> Grants the AI tools (Web Search, SQL, Gmail API) to take real actions.
# 6. Callbacks     -> Logs token counts, costs, execution times, and errors for debugging.
