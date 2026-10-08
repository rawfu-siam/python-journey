'''
Chapter1, topic - chain of thought prompting
'''
# =====================================================================
# 🧠 CHAIN OF THOUGHT (CoT) ARCHITECTURAL FRAMEWORK
# =====================================================================
# CoT Defined -> Forcing an LLM to generate intermediate reasoning steps 
#                on a scratchpad before producing its final conclusion.
# Rule of Thumb -> If a human needs a pen and paper to calculate a task,
#                  the AI needs a Chain of Thought prompt to solve it.
# Target Tasks  -> Complex logic, multi-layer policies, and math workflows.

# =====================================================================
# 🗂️ THE 3 COMPONENTS OF A CoT WORKFLOW
# =====================================================================
# 1. 🎬 THE TRIGGER (System Level):
#    - Commands the AI's internal framework using explicit directives.
#    - Example Key Phrases: "Think step-by-step", "List your variables first".
#
# 2. 🧠 THE THOUGHT SANDBOX (Reasoning Steps):
#    - Plain markdown scratchpad where the model generates token-by-token logic.
#    - Each correct word generated locks the transformer onto a logical path.
#
# 3. 🎯 THE EXTRACTION NODE (Output Anchor):
#    - Isolates operational payloads from the conversational thought process.
#    - Uses clean tags like <thinking> or structural JSON boundaries.

# =====================================================================
# 🛑 CORPORATE AGENCY ANTI-PATTERNS (MISTAKES TO AVOID)
# =====================================================================
# ⚠️ Blind Accuracy Demands:
#    - Prompting "be 100% correct" changes nothing. Structure rules instead.
# ⚠️ Over-Constrained JSON:
#    - Never force CoT logic strictly *inside* early JSON schemas. It breaks
#      grammar prediction. Let it think in raw text, then dump JSON at the end.
# ⚠️ Token & Latency Burnout:
#    - Do not use CoT for low-stakes binary decisions (e.g., simple spam checks).
#    - Every reasoning word increases execution time and agency API costs.

# =====================================================================
# 🧪 SENIOR DEVELOPER PRODUCTION GUARDRAILS
# =====================================================================
# 🛡️ Temperature Zero: Always set model temperature to 0.0 for deterministic logic.
# 🛡️ Backstage Logs: Pipe intermediate thinking strings to rotating background files.
# 🛡️ Defensive Parsing: Always wrap extraction schemas in Pydantic/Try-Except blocks.
# 🛡️ Legal Cheats: Maximize native reasoning models (o1/o3-mini) to skip manual prompts.
# =====================================================================
