'''
Chapter7, topic - Make.com (Makefile) — visual workflow builder
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# Make.com -> A modern visual canvas platform used to link cloud apps
#             together using drag-and-drop bubbles (Modules) and lines.
#             Note: Not to be confused with the 1970s compilation 'Makefile'!
# Webhook   -> A unique web URL endpoint that acts as a digital mailbox,
#             allowing Python scripts to instantly drop data into Make.com.
#
# =====================================================================
# 🏢 SYSTEM ROLES: MUSCLE VS. MIND
# =====================================================================
# 🦿 Make.com (The Hands and Feet):
#   - Connects to third-party software (Google Sheets, Gmail, Slack).
#   - Manages complex OAuth credentials, multi-app routing, and timing maps.
#   - Saves hundreds of hours of mundane API integration code.
#
# 🧠 Python (The Brain):
#   - Handles heavy computations, machine learning, and AI agent logic.
#   - Performs deep calculations, text manipulation, and dynamic processing.
#   - Validates data payloads securely before they impact databases.
#
# =====================================================================
# 🛡️ PRODUCTION GUARDRAILS & PRO HACKS
# =====================================================================
# ⏳ The 30-Second Rule: Make.com webhooks will timeout if your backend 
#   script takes too long. Always pass long actions to Background Tasks!
# 🛡️ Data Defense: Always wrap your receiving routes in Pydantic models to
#   catch missing or malformed keys sent by unpredictable web forms.
# 🚀 The Single Pipe: Connect multiple automated processes through one
#   universal webhook/endpoint by passing an "action_type" indicator key.
# 📁 Git Alignment: Always export Make.com scenario blueprint JSON files 
#   and commit them alongside your Python source files in repository trees.
