'''
Chapter2, topic - output parsers
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# Output Parser -> A LangChain tool converting raw LLM text to strict data structures.
# Pydantic Layer -> The rigid validation rulebook defining field data types.
# LCEL Piping    -> Syntax (`prompt | model | parser`) passing data down the pipeline.

# =====================================================================
# 🛡️ THE THREE-STEP PRODUCTION CHECKLIST
# =====================================================================
# 1. Determinism -> Always configure `temperature=0` to suppress AI creativity.
# 2. Descriptions -> Embed strict, unambiguous instructions inside Pydantic fields.
# 3. Fallbacks    -> Wrap brittle pipelines in an automated `OutputFixingParser`.

# =====================================================================
# 🏢 AGENCY WORKFLOWS & DESIGN PATTERNS
# =====================================================================
# 📊 Classification -> Parsing text into unique enums ("SPAM", "SALES").
# 🌐 Web Scraping    -> Extracting unstructured text arrays into multi-item lists.
# 🔧 Self-Healing    -> Automatically re-prompting the LLM to fix broken JSON format.

# =====================================================================
# 🚀 SAMPLE ARCHITECTURE SNIPPET (FOR REVISION REFERENCE ONLY)
# =====================================================================
# from pydantic import BaseModel, Field
# from langchain_core.output_parsers import PydanticOutputParser
#
# class LeadSchema(BaseModel):
#     email: str = Field(description="Must be a valid business email address.")
#     budget: int = Field(description="Extracted financial allocation in USD.")
#
# parser = PydanticOutputParser(pydantic_object=LeadSchema)
# chain = prompt_template | deterministic_model | parser
# =====================================================================
