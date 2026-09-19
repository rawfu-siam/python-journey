'''
Chapter7, topic - Slack Bolt Framework basics — handling custom
                  Slash commands (e.g., /run-scraper)
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & INTERFACE MECHANICS
# =====================================================================
# Slack Bolt    -> The official engine/toolkit used to build apps in Python.
# Slash Command -> A custom shortcut trigger word starting with a slash `/`.
# Triggering    -> Waking up your hidden Python script via a Slack chat box.
# Slack App     -> A plugin added to a workspace that gives it new powers.
# Webhook       -> The digital signal route Slack uses to contact your code.

# =====================================================================
# 🧩 INTERNAL COMPONENT ARCHITECTURE
# =====================================================================
# Client UI     -> The visual frontend application where the human types.
# Listener      -> The `@app.command()` decorator waiting for a command call.
# Payload       -> The dictionary bundle containing user info, text, and channels.
# command['text']-> The specific sub-variable used to read custom inputs.
# ack() method  -> CRITICAL: Must be fired within 3 seconds to avoid timeout.
# say() method  -> The quick messenger tool that drops text back into the chat.

# =====================================================================
# ⚠️ LANDMINES & SAFES-GUARDS (AGENCY LEVEL)
# =====================================================================
# Timeout Trap  -> Missing `ack()` early, causing red error logs for the user.
# Silent Death  -> Forgetting `try/except` blocks, letting a script crash die.
# Firewall Trap -> Running on localhost without a public url tunnel (ngrok).
# Security Leak -> Hardcoding live api tokens instead of using `.env` inputs.

# =====================================================================
# 🎬 THE SENIOR PASS: LAZY SHORTCUTS & ADVICE
# =====================================================================
# Golden Rule   -> "Ack immediately, log gracefully, run silently."
# Dict-Mapping  -> Using key-value lookups to route tasks without `if` chains.
# Block Kit     -> Drag-and-drop designer used to steal layout JSON codes.
# Decoupling    -> Putting web scrapers in a separate file away from Slack logic.
# Backgrounds   -> Offloading heavy tasks to threads so the script stays active.
