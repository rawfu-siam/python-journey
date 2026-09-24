'''
Chapter9, topic - pre-commit hooks
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# Pre-Commit Hook -> An automated robot security guard running locally.
# Trigger Point   -> Fires instantly right after you type `git commit`.
# Main Action     -> Runs scripts to inspect, format, and secure files.
# Result Gates    -> PASS: Saves commit history. FAIL: Blocks save event.
#
# =====================================================================
# ⚙️ THE THREE CORE PIECES
# =====================================================================
# 1. Framework Manager -> The global `pre-commit` CLI application package.
# 2. Config File       -> `.pre-commit-config.yaml` listing repo rules.
# 3. Hook Plugins      -> Individual worker tools (Ruff, Bandit, etc.).
#
# =====================================================================
# 💻 CRITICAL TERMINAL COMMAND MATRICES
# =====================================================================
# `pip install pre-commit`        -> Installs framework manager wrapper.
# `pre-commit install`            -> Binds manager into local `.git/hooks/`.
# `pre-commit run --all-files`    -> Manual full codebase pre-flight test.
# `git commit -m "msg" --no-verify` -> Emergency bypass (The Escape Hatch).
#
# =====================================================================
# 🛡️ ENTERPRISE QUALITY GUARDRAILS
# =====================================================================
# 🦅 Ruff   -> Lightning-fast auto-formatter & syntax checker (PEP 8).
# 🦝 Bandit -> Zero-Trust security scanner hunting for exposed API keys.
# 🎒 Builtin -> Trims trailing spaces and fixes empty file end lines.
#
# =====================================================================
# ⚠️ LANDMINES & AGENCY WORKFLOW LAWS
# =====================================================================
# * If a hook fails and auto-fixes your files, you MUST run `git add`
#   again to stage the newly cleaned changes before recommitting!
# * Never commit your local virtual environment cache directories.
# * "Fix it local, fix it automatically, or it never leaves your machine."
