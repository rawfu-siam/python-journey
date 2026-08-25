'''
Chapter1, topic - Git branch naming conventions linked to Issue IDs
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & RULES
# =====================================================================
# Git Branch -> A safe, isolated sandbox workspace to copy and edit code.
# Issue ID   -> A unique tracking ticket number from Linear or Notion.
# Connection -> Linking them means naming your sandbox after your ticket.

# =====================================================================
# 📐 THE 3-PART BRANCH BLUEPRINT
# =====================================================================
# Formula: prefix/issue-id-descriptive-action-slug
#
# 📂 1. PREFIX TYPES:
#   - `feature/`  -> Building brand new automation pipelines or tools.
#   - `bugfix/`   -> Repairing broken keys, crashing endpoints, or scripts.
#   - `refactor/` -> Cleaning, restructuring, or renaming messy python code.
#   - `docs/`     -> Updating README files or internal project guides.
#
# 🆔 2. ISSUE ID RULES:
#   - Must match the ticket number exactly (e.g., `issue-102`, `lin-44`).
#   - Always write it in STRICTLY lowercase format for server safety.
#
# 📝 3. DESCRIPTIVE SLUG:
#   - Keep it short: 2-4 punchy, action-oriented words.
#   - Absolutely NO spaces! Bind words together using hyphens (`-`).

# =====================================================================
# 💻 TERMINAL COMMAND QUICK REFERENCE
# =====================================================================
# Create & Switch:  `git switch -c feature/issue-102-slack-bot`
# Check Workspace:  `git branch`
# Push to GitHub:   `git push --set-upstream origin feature/issue-102-slack-bot`

# =====================================================================
# 🦥 THE AUTOMATION MINDSET (GOLDEN SPELL)
# =====================================================================
# "If it does not have an Issue ID, it does not exist to the agency."
# Naming correctly lets GitHub trigger webhooks to automate your board!
