'''
Chapter4, topic - output handling and parsing crew results
'''
# =====================================================================
# 🧠 1. CORE DEFINITIONS & COMPONENTS
# =====================================================================
# Output Handling -> Capturing the final answer of a Crew without the
#                    messy behind-the-scenes intermediate agent chatter.
# Parsing         -> Turning raw text strings into structured, type-safe
#                    formats (JSON or Python Objects) computers understand.
#
# CrewAI provides 3 primary properties to extract data from a result:
#   1. result.raw       -> Returns the direct plain-text string.
#   2. result.json      -> Returns a strict JSON-formatted text string.
#   3. result.pydantic  -> Returns a live, type-validated Python object.

# =====================================================================
# 🛠️ 2. THE THREE WORKFLOW KNOBS (ATTACHED TO TASKS)
# =====================================================================
# 📝 1. output_file="path.md"
#   - Automatically drops a copy of the final text on your hard drive.
#   - Eliminates standard 'with open()' boilerplate code entirely.
#   - Perfect for human-readable content (blogs, markdown reports).
#
# 🗂️ 2. output_json=True
#   - Instructs and forces the agent to structure text into a JSON object.
#   - Ideal for visual builders or no-code platforms (n8n, Make.com, Zapier).
#
# 🛡️ 3. output_pydantic=YourModelSchema
#   - The corporate agency standard. Injects a rulebook directly into the LLM.
#   - Guarantees the final output is returned as an operational Python Object.
#   - Essential for direct SQL database entries and robust backend pipelines.

# =====================================================================
# ⚠️ 3. PRODUCTION PITFALLS & ROOKIE ERRORS
# =====================================================================
# * Property Crashers: Trying to read result.pydantic or result.json when
#   the task was never explicitly configured with those parameters.
# * Prompt Disconnect: Keeping your Task descriptions completely vague
#   while expecting a highly structured Pydantic object back.
# * String Indices Mistake: Forgetting that result.json is still technically
#   a string, requiring a json.loads() call before reading fields.

# =====================================================================
# 🎬 4. THE SENIOR DEVELOPER RETROSPECTIVE (USA AGENCY EXPECTATIONS)
# =====================================================================
# * Semantic Guidance: Always use Field(description="...") on schemas because
#   the underlying LLM parses those descriptions as precise constraints.
# * Isolation Principle: Keep models and schemas decoupled inside a separate
#   models.py or schemas.py file to ensure architectural scalability.
# * Golden Rule: Fix your schema definitions and guide your task parameters
#   natively rather than writing long, fragile string-cleaning code.
#
# Magic Spell: "Fix the Schema, guide the Task, and let the Data catch itself."
# =====================================================================
