'''
Chapter9, topic - GitHub Actions CI/CD workflows — building a .github/workflows/ci.yml 
                  pipeline to auto-test and badge code on every push
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# GitHub Actions -> An automated engine running tasks in cloud servers.
# CI (Integration)-> Automatic testing of code components on every push.
# CD (Deployment) -> Auto-shipping verified code to live production servers.
# YAML (.yml)     -> The clean, space-sensitive structure language for CI.
# The Blueprint   -> Must live strictly at `.github/workflows/ci.yml`.

# =====================================================================
# 🗂️ THE 4 PILLARS OF A WORKFLOW CAPTAIN
# =====================================================================
# ⚡ 1. TRIGGER  (`on:`)       -> Defines the exact action (e.g. push, pr).
# 🖥️ 2. RUNNER   (`runs-on:`) -> Sets the specific cloud OS (e.g. ubuntu-22.04).
# 🪜 3. STEPS    (`steps:`)   -> The linear, ordered list of execution blocks.
# 🛠️ 4. ACTIONS  (`uses:`)    -> Community-built plugins to skip writing raw code.

# =====================================================================
# 🛡️ ENTERPRISE QUALITY CONTROL COMPLIANCE
# =====================================================================
# 📦 Package Management -> Switch from slow `pip` to `uv` for 10x speed.
# 🧼 Code Neatness     -> Run `ruff check` to ensure clean PEP8 formatting.
# 🔍 Security Auditing -> Run `bandit -r` to block credential or injection flaws.
# 🏅 Status Badges     -> Paste `![Build Status](.../badge.svg)` into README.md.

# =====================================================================
# 🧪 SENIOR DEV RULES FOR JUNIOR AUTOMATION ENGINEERS
# =====================================================================
# 🚨 Rule 1: Never use `ubuntu-latest` in production. Always lock the version!
# 💵 Rule 2: Turn on package caching (`enable-cache: true`) to save workflow mins.
# 🔑 Rule 3: Never put plain text passwords in YAML. Use GitHub Action Secrets!
# 🔔 Rule 4: Bind error triggers using `if: failure()` to sound Slack alerts.
