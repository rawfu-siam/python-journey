'''
Chapter2, topic - LLMs and Chat Models in LangChain
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ECOSYSTEM ARCHITECTURE
# =====================================================================
# LLM        -> Text-completion engine. Takes raw string -> Returns string.
# Chat Model -> Conversation engine. Takes structured list -> Returns message.
# .invoke()  -> The standard uniform execution API for modern LangChain.

# =====================================================================
# 👤 THE STRUCTURED MESSAGE TRIFECTA
# =====================================================================
# 👤🛠️ SystemMessage -> Hardcoded agent rulebook, persona, and constraints.
# 👤💬 HumanMessage  -> The dynamic incoming query typed by the end-user.
# 🤖💬 AIMessage     -> Past outputs from the model used to preserve history.

# =====================================================================
# 🏢 AGENCY-GRADE AGENT DEPLOYMENT CHECKLIST
# =====================================================================
# 1. Credential Security:
#    - Keep keys out of code. Load via python-dotenv from protected files.
#
# 2. Temperature Tuning:
#    - Use `temperature=0.0` for structured extractions and deterministic bots.
#    - Use `temperature=0.7` for copywriting tools or human-like chatbots.
#
# 3. Payload Contracts:
#    - Avoid raw text parsers for downstream logic.
#    - Always bind models to Pydantic schemas using `.with_structured_output()`.
#
# 4. Context Window Safeguards:
#    - Never let message arrays grow infinitely in looping background tasks.
#    - Prune or summarize history arrays to avoid exponential token bills.
