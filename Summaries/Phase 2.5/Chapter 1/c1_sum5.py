'''
Chapter1, topic - Smart commits — closing issues automatically via Git commit messages
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & BASIC UNDERSTANDING
# =====================================================================
# Smart Commit -> A Git message with special keywords that hooks directly
#                 into project boards (Linear/Notion) via GitHub webhooks.
# Purpose      -> Automates business workflows by updating/closing issue
#                 cards directly from your dark terminal screen.
# Blueprint    -> [Prefix] + [Short Description] + [Trigger Verb] + [#ID]
#
# Examples of standard formats:
#   - "fix: repair broken selenium locator string closes #42"
#   - "feat: build incoming webhook receiver module resolve #105"

# =====================================================================
# 🎯 SYSTEM MECHANICS & VALID KEYWORDS
# =====================================================================
# Valid Action Prefixes (Semantic):
#   - `fix:`  -> Bug fixes, crash resolutions, logic patches.
#   - `feat:` -> Brand new automations, tools, endpoints, or features.
#   - `docs:` -> Markdown, README, or internal documentation changes.
#
# Valid Automation Trigger Verbs:
#   - `close`   / `closes`   / `closed`
#   - `fix`     / `fixes`     / `fixed`
#   - `resolve` / `resolves` / `resolved`

# =====================================================================
# ⚠️ CRITICAL RULES & DANGER ZONES TO AVOID
# =====================================================================
# 🚫 NO SPACES WITHIN ID TAGS:
#   - Wrong:  `close # 102` -> The automation script parser will fail!
#   - Right:  `close #102`  -> Keep the hashtag glued directly to digits.
#
# 🤫 REMOTE EXECUTIONS MANDATE A PUSH:
#   - Local commits will NEVER update your team's tracking board.
#   - The magic webhook triggers ONLY after running a clean `git push`.
#
# 🔀 BRANCH CORRELATION STRATEGY:
#   - Match your branch strings to ticket structures for high visibility:
#   - Example: `feature/issue-102-pydantic-gate`

# =====================================================================
# 🎬 THE PRO SHORTCUTS & AGENCY EXPECTATIONS
# =====================================================================
# 🏎️ MULTI-ISSUE ANNIHILATION:
#   - You can chain commands to close multiple tickets with one push:
#   - Message: "fix: solve request timeout error, closes #12, fixes #13"
#
# 🪄 THE MAGIC SPELL FOR YOUR MIND:
#   - "Command the action, tag the anchor, push to trigger."
