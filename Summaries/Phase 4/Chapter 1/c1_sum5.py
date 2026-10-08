'''
Chapter1, topic - prompt engineering principles
'''
# =====================================================================
# 🧠 BASIC DEFINITIONS
# =====================================================================
# Prompt            -> The literal string input text sent to an LLM.
# Prompt Engineering-> Designing clear text inputs to make AI outputs predictable.
# Agency Rationale  -> Unmanaged AI causes unpredictable errors. We engineer 
#                      prompts to ensure clean data parsing and cut token bills.

# =====================================================================
# 🏗️ THE 4 GOLDEN PILLARS OF PROMPT DESIGN
# =====================================================================
# 1. 🎭 The Role       -> Defining the AI's persona (e.g., "Act as an auditor").
# 2. 📝 The Context    -> Isolating dynamic data targets using clean delimiters.
# 3. 🛡️ The Constraints-> Hard rules telling the AI exactly what NOT to execute.
# 4. 🗂️ Output Shape   -> Enforcing explicit schemas (usually structured JSON).

# =====================================================================
# 💻 HIGH-VELOCITY PRODUCTION SYNTAX RECAP
# =====================================================================
# Unstructured Text    -> Basic strings that cause messy conversational text outputs.
# Pure JSON Objects    -> Enforced using response_format={"type": "json_object"}.
# Pydantic Engineering -> The ultimate setup using client.beta.chat.completions.parse()
#                         to match models natively for 100% type safety.

# =====================================================================
# 🛡️ SENIOR GUARDRAILS & PRO HACKS
# =====================================================================
# ❌ Fluff Words       -> Avoid polite chatter to minimize expensive token overhead.
# 📅 Dynamic Realities -> Never use vague words like "yesterday". Pass calculated
#                         Python datetime values down into the prompt fields instead.
# ⚡ Few-Shot Injection -> Providing 2-3 input/output samples inside your text
#                         to immediately lock in hard logic formats without long rules.
# 🪄 Golden Spell       -> "Show, don't tell: Give the AI an exact role and concrete
#                         examples, then let Python manage the structure."
