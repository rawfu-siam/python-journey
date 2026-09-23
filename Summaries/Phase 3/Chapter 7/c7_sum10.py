'''
Chapter7, topic - error handling in automation workflows
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & WORKFLOW PHILOSOPHY
# =====================================================================
# Exception      -> A real-world roadblock that interrupts code execution.
# Error Handling -> Providing a structural Plan B to keep pipelines alive.
# The Gold Rule  -> "Code defensively, fail gracefully, and never die in silence."
# EAFP Principle -> "Easier to Ask Forgiveness than Permission" (Try first, handle next).

# =====================================================================
# 🏗️ THE 4-PILLAR SAFETY SUIT
# =====================================================================
# 🔍 1. try:     -> Houses the volatile automation/network/API code.
# 🛡️ 2. except:  -> Captures targeted faults; deploys fallback actions.
# 🟩 3. else:    -> Fires exclusively when the try-block runs flawlessly.
# 🔒 4. finally: -> The absolute cleanup crew; runs win, lose, or draw.

# =====================================================================
# ⚠️ DEV TRAPS & ANTI-PATTERNS (WHAT TO AVOID)
# =====================================================================
# 🫣 Bare Except   -> Writing 'except:' catches typos; blinds your debugging.
# 🤫 Silent Pass   -> Hiding bugs with 'pass' corrupts databases down-stream.
# 🪆 Over-Nesting  -> Pyramids of try-blocks create unreadable spaghetti systems.

# =====================================================================
# 🕶️ PRODUCTION-GRADE AGENCY PROTOCOLS
# =====================================================================
# ⚡ Contextlib   -> Use 'contextlib.suppress()' to eliminate 4-line pass blocks.
# 🔄 Self-Healing -> Wrap flaky AI/web endpoints in Exponential Backoff retries.
# 🗺️ State Tracking-> Checkpoint your data loops to prevent double-processing on reboot.
# 📡 Telemetry    -> Pipe full tracebacks to Slack channels; never rely on raw console prints.
