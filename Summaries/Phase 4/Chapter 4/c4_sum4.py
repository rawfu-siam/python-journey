'''
Chapter4, topic - tasks — description, expected output, agent assignment
'''
# =====================================================================
# 🧠 CORE DEFINITIONS: CREWAI TASK ANATOMY
# =====================================================================
# Task            -> A strict operational contract given to an AI Agent.
# Description     -> The step-by-step intern-style execution instructions.
# Expected Output -> The explicit delivery mold specifying format & shape.
# Agent           -> The specialized digital worker assigned to the job.
# Context         -> A pro pipeline list connecting prior task outputs.
#
# =====================================================================
# 🏢 THE THREE PILLARS OF A FAULT-TOLERANT TASK
# =====================================================================
# 📝 1. DESCRIPTION PRO-TIPS:
#   - Avoid conversational filler ("please", "kindly", "do your best").
#   - Use clinical, active command verbs (Extract, Validate, Format).
#   - Keep parameters open to runtime updates using {placeholder} keys.
#
# 🎁 2. EXPECTED OUTPUT PRO-TIPS:
#   - Never leave the final structural format up to the AI's imagination.
#   - Enforce markdown tables, exact bullet counts, or rigid files.
#   - Force enterprise safety by mapping directly to Pydantic objects.
#
# 👤 3. AGENT ASSIGNMENT PRO-TIPS:
#   - Match the specific agent persona directly to the problem domain.
#   - Never cram an entire multi-agent loop into one solo task object.
#   - Keep verbose settings active during debugging to trace exceptions.
#
# =====================================================================
# ⚠️ THE JUNIOR DESTRUCTIVE PITFALL MATRIX
# =====================================================================
# 👻 The Ghost Writer -> Missing the 'agent=' variable causing code death.
# 🗣️ The Vague Return -> Writing text descriptors instead of structured shapes.
# 🪵 The Pipeline Jam -> Cramming research, writing, & emailing into one task.
#
# =====================================================================
# 🎬 THE SENIOR DEV SHORTCUT MANIFESTO
# =====================================================================
# 🪄 Context Chains   -> Use context=[task1, task2] to bypass manual loops.
# 🧘 Wise Laziness    -> Offload data-scrubbing parameters onto the LLM rules.
# 🔮 The Golden Spell -> "If an intern gets confused, the AI will destroy it."
