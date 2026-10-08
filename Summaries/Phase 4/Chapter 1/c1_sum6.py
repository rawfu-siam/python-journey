'''
Chapter1, topic - few-shot prompting
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# Few-Shot Prompting -> Guiding an AI model by providing a small number 
#                        of explicit input-output examples (shots) to 
#                        demonstrate a desired pattern or format.
# Zero-Shot Prompting -> Querying an AI model directly with instructions
#                        but giving it zero examples to learn from.
# Predictability     -> The core goal of few-shotting; forcing a creative
#                        AI to yield stable, reliable, structured data.
#
# =====================================================================
# 🏗️ THE 4 PILLARS OF A PROFESSIONAL FEW-SHOT PROMPT
# =====================================================================
# 1. Instruction     -> The high-level rulebook or persona definition.
# 2. Structured Shots-> Balanced pairs of example inputs and outputs.
# 3. Separators      -> Explicit structural markers (e.g., 'Text:', 'Date:')
#                       that isolate questions from answers neatly.
# 4. Target Query    -> The fresh runtime data left open for the AI to complete.
#
# =====================================================================
# ⚠️ ARCHITECTURAL GUARDRAILS & COMMON PITFALLS
# =====================================================================
# - Format Shifts    -> NEVER switch separator syntax mid-prompt. Keep it uniform.
# - Output Bias      -> Provide balanced outcome types to prevent the model
#                       from leaning toward one repetitive answer classification.
# - Token Bloat      -> Keep shots limited to 2-5 high-quality examples. Massive
#                       prompt lengths degrade memory and escalate API billing.
#
# =====================================================================
# 🎬 THE AGENCY-GRADE DEVELOPER MINDSET
# =====================================================================
# - Dynamic Assembly -> Store few-shot pairs in data objects and loop through
#                       them instead of hardcoding heavy text blocks.
# - Prompt Isolation -> Keep instructions isolated in designated config files
#                       away from structural script automation loops.
# - Show, Don't Tell -> Rely on pattern demonstration rather than writing 
#                       overly complex rules to process messy business data.
