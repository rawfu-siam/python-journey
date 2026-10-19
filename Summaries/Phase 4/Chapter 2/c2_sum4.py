'''
Chapter2, topic - chains — LLMChain, SequentialChain
'''
# =====================================================================
# 🧠 CORE DEFINITIONS: MODERN LANGCHAIN CHAINS & LCEL
# =====================================================================
# Chain       -> An automated assembly line connecting multiple LLM operations.
# LCEL        -> LangChain Expression Language using the pipe operator (|).
# Component   -> Prompts, Models, Parsers, or Tools acting as Lego building blocks.

# =====================================================================
# 🧱 THE ASSEMBLY LINE BUILDING BLOCKS
# =====================================================================
# 📝 ChatPromptTemplate  -> Formats raw string variables into structured prompts.
# 🤖 ChatOpenAI          -> The primary deterministic LLM processing engine.
# 🧹 StrOutputParser     -> Strips metadata away, returning raw, clean text strings.
# 📊 JsonOutputParser    -> Marshals unstructured data into validated dictionary objects.

# =====================================================================
# 🔀 ARCHITECTURE PATTERNS
# =====================================================================
# 🔗 Standard LCEL Chain:
#   - Layout: chain = prompt | model | parser
#   - Pushes data straight from initialization to cleaned text.
#
# 🔁 Multi-Step Sequential Chain:
#   - Layout: pipeline = {"var_name": chain_one} | chain_two
#   - Injects the resolved string response of Chain 1 directly into Chain 2 inputs.

# =====================================================================
# ⚠️ SENIOR PRODUCTION TIPS & INJECTION GUARDRAILS
# =====================================================================
# 1. Deprecation Guard: Avoid old `LLMChain` / `SequentialChain` legacy classes.
# 2. Strict Determinism: Lock `temperature=0.0` when extracting structured outputs.
# 3. Pydantic Bindings: Enforce structural schema models on JsonOutputParser endpoints.
# 4. Scale Ready: Utilize async `.ainvoke()` pipelines for production workloads.
