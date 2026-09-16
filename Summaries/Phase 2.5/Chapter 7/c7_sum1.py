'''
Chapter6, topic - Remote agency engineering communication etiquette
                  (Threads, Slack Markdown)
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS (P2.5 — CHAPTER 7.1)
# =====================================================================
# Threads 🧵         -> Side-conversations that attach to a main message.
#                       Keeps the general workspace clean from spam.
# Slack Markdown 📝  -> Text formatting rules (*bold*, `code`) that make 
#                       updates scannable for managers in 2 seconds.
# Webhook Endpoint   -> A secure URL where our Python scripts drop a JSON
#                       package to post messages automatically.

# =====================================================================
# 🏢 AGENCY WORKSPACE HYGIENE & SOCIAL LAWS
# =====================================================================
# 🤫 MAIN CHANNELS ARE SACRED:
#   - Only post high-level statuses, new alerts, or clear roadblocks.
#   - Never dump raw code logs or multi-paragraph rants in the open.
#
# 🧵 THREAD-FIRST HYGIENE:
#   - When an automated alert fires, click "Reply to thread".
#   - Conduct all troubleshooting, code reviews, and updates inside.
#   - Keeps history perfectly grouped for engineers across timezones.

# =====================================================================
# 📝 THE SLACK MARKDOWN CHEAT SHEET FOR DEVELOPERS
# =====================================================================
# *Bold Text*           -> Used for severe warnings or main titles.
# _Italic Text_         -> Used for secondary data or timelines.
# ~Strikethrough~       -> Used to mark completed steps or changed ideas.
# `inline code`         -> Used for names like `main.py` or `api_key`.
# ```python             -> Open token for code blocks with active syntax
# [your code here]         coloring. Crucial for posting legible bugs.
# ```                   -> Closing token for code blocks.

# =====================================================================
# 🎬 THE SENIOR DEV LAWS (HOW TO STAND OUT IN A US AGENCY)
# =====================================================================
# 🛠️ CHEAT SHORTCUT     -> Use the official "Slack Block Kit Builder" web tool.
#                       Design visually, copy the JSON, paste into Python.
# 🦥 THE LAZY VALUE     -> Build a singular `slack_helper.py` utility module once.
#                       Import it across every script rather than rewriting alerts.
# 🪄 THE MAGIC SPELL     -> "If it's worth updating the main channel, it's 
#                       worth a bold title and a thread."
# 🚨 WEBHOOK SAFETY     -> Always wrap outgoing requests in `try/except` blocks
#                       so a network failure doesn't crash your core pipeline.
