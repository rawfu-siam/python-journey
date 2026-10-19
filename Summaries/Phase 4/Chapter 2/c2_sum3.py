'''
Chapter2, topic - prompt templates — PromptTemplate, ChatPromptTemplate
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE MATCHING
# =====================================================================
# PromptTemplate     -> String-based blueprint designed for raw completion LLMs.
# ChatPromptTemplate -> Message-based list blueprint optimized for Chat Models.
# LCEL Composition   -> Linking elements via the pipe (`|`) operator.

# =====================================================================
# 🎭 CHAT TEMPLATE ROLE SYNTAX
# =====================================================================
# ChatPromptTemplate.from_messages([
#     ("system", "Strict persona constraints and parameters go here."),
#     ("human", "Dynamic user queries containing variable placeholders like {task}."),
#     ("ai",     "Pre-baked historical responses if demonstrating few-shot behavior.")
# ])

# =====================================================================
# 🛡️ BOUTIQUE AGENCY SANITIZATION & SECURITY RULES
# =====================================================================
# 1. Bracket Collisions:
#    - Single curly brackets `{variable}` declare dynamic variable inputs.
#    - Double curly brackets `{{ "json": "literal" }}` output clean, raw text.
#
# 2. Input Isolation:
#    - Never append unchecked user input strings directly onto system instructions.
#    - Sanitize inputs inside a dedicated `HumanMessage` template layer.
#
# 3. Clean Separation of Concerns:
#    - Store massive prompt copy blocks outside of main logic execution files.
#    - Keep variables distinct from logic strings to maximize token efficiency.
