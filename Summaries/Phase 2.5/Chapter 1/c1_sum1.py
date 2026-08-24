'''
Chapter1, topic - Linear / Notion workspace setup for engineering Sprints
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & SPRINT BLUEPRINTS
# =====================================================================
# Workspace -> A shared digital board (Linear/Notion) tracking all team tasks.
# Sprint    -> A fixed 1-to-2 week time-box for completing specific features.
# Issue/Card-> A single unit of work with a unique ID, specs, and checklists.
# DoD       -> Definition of Done: The strict contract your script must meet.

# =====================================================================
# 🚜 THE ENTERPRISE STATUS PIPELINE
# =====================================================================
# 🗄️ Backlog     -> Future client requests and long-term feature ideas.
# 📋 Todo        -> Approved tasks selected specifically for the current Sprint.
# ⏳ In Progress -> Active development. A dev is actively coding this right now.
# 👀 Review/QA   -> Code is written, waiting for Senior PR review or testing.
# 🎉 Done        -> Code is fully verified, merged, and live in production.

# =====================================================================
# 🛠️ THE SENIOR WORKFLOW (TERMINAL COMMANDS)
# =====================================================================
# 1. Update your local environment:
#    `git checkout main && git pull origin main`
#
# 2. Isolate work by creating a dedicated issue branch:
#    `git checkout -b feature/issue-102`
#
# 3. Code the Python automation script to match the exact DoD spec.
#
# 4. Stage your files:
#    `git add config_validator.py`
#
# 5. Use automated Smart Commits to magically update your board:
#    `git commit -m "feat: validate environment keys, close #102"`
#
# 6. Ship it to review:
#    `git push origin feature/issue-102`

# =====================================================================
# 🛡️ THE AUTOMATION DEV'S GOLDEN RULES
# =====================================================================
# 🎰 Multi-Close -> Combine strings to close multiple tickets: `close #101, close #102`
# 🛑 Anti-Pattern -> Never write code or push directly to the `main` branch.
# 📝 Paper Trail -> Leave detailed technical comments on the card if you get blocked.
# 🪄 Catchphrase -> "Code in isolation, commit with intention, automate your status."
