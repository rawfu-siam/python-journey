'''
Chapter7, topic - Slack Block Kit Builder for designing rich, structured diagnostic reports
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# Slack Block Kit -> Slack's modular UI framework that uses JSON "blocks"
#                    to construct visually rich, organized messages.
# Block Builder   -> The web app at `https://slack.com`
#                    used to drag-and-drop elements and generate layout JSON.
# Diagnostic Card -> A highly structured, scannable status or error report
#                    dispatched by background scripts to production channels.
#
# =====================================================================
# 🧩 THE CORE LEGO BRICKS (BLOCK TYPES)
# =====================================================================
# 🏷️ Header   -> Strong, bold title text at the top. Supports `plain_text`.
# 📝 Section  -> Main text canvas. Supports `fields` for side-by-side grids
#               and `mrkdwn` for bolding (*), italics (_), and codes (```).
# ➖ Divider  -> A clean line separator that organizes card visual weight.
# 🖼️ Context  -> Small, muted metadata rows for tracking dates or versions.
# ⚡ Actions  -> Interactive layouts for buttons (`primary`/`danger` styles).
#
# =====================================================================
# ⚠️ ENTERPRISE GUARDRAILS & ROOKIE PITFALLS
# =====================================================================
# 🧱 String Limits -> Sections crash if text exceeds 3,000 characters.
#                     FIX: Slice data securely using `traceback[-2500:]`.
# 🔓 Secret Leak   -> Hardcoding webhook URLs compromises internal channels.
#                     FIX: Load URL safely using `os.environ.get("SLACK_URL")`.
# 🚦 Traffic Light -> Agency standards use Green (`primary`) for success,
#                     and Red (`danger`) for critical pipeline exceptions.
