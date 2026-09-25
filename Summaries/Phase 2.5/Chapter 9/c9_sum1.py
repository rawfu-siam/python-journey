'''
Chapter9, topic - uv library setup — lightning-fast package resolution replacing
                  traditional slow pip operations
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & SPEED BENEFITS
# =====================================================================
# uv        -> An ultra-fast, modern Python package manager written in Rust.
# Purpose   -> Designed as a blazingly fast drop-in replacement for slow 'pip'.
# Mechanism -> Uses a global cache vault to share files across local projects.
#              Instead of re-downloading, it creates instant hard shortcuts.

# =====================================================================
# 🛠️ THE EVERYDAY TERMINAL CHEAT SHEET
# =====================================================================
# Old Pip Approach                     | Modern Supersonic UV Way
# ---------------------------------------------------------------------
# pip install uv                       | # Installs uv into your global system
# python -m venv .venv                 | uv venv .venv
# pip install requests fastapi         | uv pip install requests fastapi
# pip install -r requirements.txt      | uv pip install -r requirements.txt
# pip list                             | uv pip list

# =====================================================================
# 🚀 AGENCY-GRADE ADVANCED CAPABILITIES
# =====================================================================
# 🛸 Zero-Setup Scripts (uv run):
#   - Executes standalone code using inline comments defining dependencies.
#   - Command: `uv run --with httpx bot.py`
#   - Spins up temporary background sandboxes and wipes them when done.
#
# 🛡️ Production Lockfiles (uv pip compile):
#   - Converts loose requirement names into frozen, hashed dependency lists.
#   - Command: `uv pip compile requirements.in -o requirements.txt`
#   - Prevents breaking changes from fracturing production agency apps.

# =====================================================================
# ⚠️ DEV GUARDRAILS & COMMON LANDMINES
# =====================================================================
# 1. The Missing Layer: Running `uv install` throws an error. 
#    - Solution: Always include the translation layer -> `uv pip install`.
# 2. Silent Slowdowns: Accidental use of regular `pip` inside a uv sandbox.
#    - Solution: Train muscle memory to type `uv pip` for maximum caching.
# 3. Activation Guard: `uv pip` refuses to run if an environment isn't live.
#    - Solution: Always run activation scripts before running setups.

# =====================================================================
# ✨ SENIOR MENTOR RULES OF THUMB
# =====================================================================
# - "If it's slow, you're doing it wrong; prepend `uv` and let it fly!"
# - Treat local sandboxes (.venv) as disposable. Break them, wipe them,
#   and recreate them instantly in 2 seconds flat with `uv`.
