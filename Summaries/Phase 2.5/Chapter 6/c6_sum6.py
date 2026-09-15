'''
Chapter6, topic - Pre-commit hook integration — running tests automatically
                  before a Git commit
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# Git Hook        -> An automated tripwire/script inside the hidden `.git/hooks/`
#                    vault that runs automatically when specific Git events happen.
# Pre-commit Hook -> A gatekeeper script triggered the millisecond you run a commit,
#                    but BEFORE Git actually saves your work to the timeline history.
# Exit Code Rules -> If the hook tools return an exit code of 0 (Pass), Git saves code.
#                    If tools return code 1+ (Fail), Git freezes and cancels the save!
#
# =====================================================================
# 🛠️ THE 3-PIECE PRE-COMMIT ARCHITECTURE
# =====================================================================
# 1. The Hidden Vault  -> `.git/hooks/` - Where the actual automated triggers live.
# 2. The Pip Manager   -> `pip install pre-commit` - The framework tool used to handle hooks.
# 3. The Instruction Manual -> `.pre-commit-config.yaml` - The configuration engine rules.
#
# =====================================================================
# 📜 PRODUCTION-GRADE CONFIGURATION TEMPLATE (`.pre-commit-config.yaml`)
# =====================================================================
# repos:
#   - repo: https://github.com
#     rev: 24.3.0                     # Always lock specific tool versions for the team!
#     hooks:
#       - id: black                   # Automated code styling guardrail
#
#   - repo: local
#     hooks:
#       - id: fastapi-pytest-check
#         name: Run App Test Suite    # Descriptive name for terminal logging
#         entry: pytest               # Runs local test suites automatically
#         language: system
#         types: [python]
#         pass_filenames: false
#
# =====================================================================
# ⚙️ MASTER TERMINAL COMMAND MANIPULATION
# =====================================================================
# `pre-commit install`        -> Links configuration settings directly to Git hooks.
# `pre-commit run --all-files` -> Pro-tip: Run checks manually anytime without committing.
# `--no-verify` or `-n`        -> The senior dev escape hatch to skip hooks legally.
#
# =====================================================================
# ⚠️ THE JUNIOR DEVELOPER ESCAPE MANUAL (COMMON TRAPS)
# =====================================================================
# 👻 Forgotten Installs -> Writing a YAML config file without running `pre-commit install`.
# 🔄 Formatting Loops   -> Code beautifiers (Black) change styles and fail the commit.
#                          Fix: Simply run `git add .` to stage updates and re-commit!
# 🌍 Environment Crashes-> Pre-commit fails because `language: system` cannot locate
#                          dependencies. Fix: Ensure your `venv` is active and built.
#
# =====================================================================
# 🪄 THE AUTOMATION GOLDEN SPELL
# =====================================================================
# "If it isn't automated locally, it isn't protected globally."
