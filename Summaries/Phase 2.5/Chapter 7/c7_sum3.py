'''
Chapter7, topic - Slack App creation basics via the Slack Developer Console
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & SLACK DEV CONSOLE
# =====================================================================
# Developer Console -> Factory website (://slack.com) to register apps.
# Bot User Token    -> Magical password (starts with xoxb-) giving app identity.
# Scopes            -> Explicit permissions (e.g., chat:write) given to a bot.
# Workspace Sandbox -> Free private slack workspace used to safely test code.

# =====================================================================
# 📬 COMMUNICATION ARCHITECTURES
# =====================================================================
# 📣 INCOMING WEBHOOKS:
#   - Simple, unique web addresses tied to one specific channel.
#   - Great for fast, unidirectional plain text error alerts.
#   - Fired using standard requests.post() without importing external libraries.
#
# 🧠 SLACK WEB API (slack_sdk):
#   - Powerful, multi-purpose client utilizing the xoxb- token payload.
#   - Can talk to multiple channels dynamically, attach reactions, upload files.
#   - Requires bots to be explicitly invited to channels via /invite.

# =====================================================================
# 🛠️ PRODUCTION & DESIGN BEST PRACTICES
# =====================================================================
# 🛡️ Credential Hygiene   -> Never hardcode tokens! Load them via os.environ.get().
# 🎨 Block Kit Builder    -> Visual drag-and-drop tool to output ready-made JSON layouts.
# 🚨 Fail-Safe Catching   -> Wrap pipelines in global try-except to funnel tracebacks.
# 🧵 Threading Hygiene    -> Capture response 'ts' to nest sub-alerts into tight threads.
