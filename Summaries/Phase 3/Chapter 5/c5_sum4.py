'''
Chapter5, topic - sending emails with Python — smtplib
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURAL TERMS
# =====================================================================
# smtplib     -> Built-in Python library that works like a digital postman.
# SMTP Server -> The internet post office address (e.g., `://gmail.com`).
# Port 587    -> The secure connection window using standard TLS encryption.
# starttls()  -> The command that turns on a secure shield for code data.
# App Password-> A unique 16-character code required instead of real passwords.
# MIME        -> A structural organizer that formats body text and attachments.

# =====================================================================
# ⚠️ LANDMINE DEFUSION & COMMON MISTAKE TRACKING
# =====================================================================
# * Invisible String Gaps -> Raw strings need `\n\n` between Subject and Body.
# * Hardcoded Credential Danger -> Plain passwords written in code get stolen by bots.
# * General Password Rejection -> Standard account logins cause authentication crashes.
# * Missing Attachment Flags -> Non-text attachments (PDF/Excel) must use read-binary (`"rb"`).

# =====================================================================
# 🧠 THINKING LIKE AN AGENCY-GRADE AUTOMATION EXPERT
# =====================================================================
# * Isolate Core Utilities -> Build a reusable `mailer.py` script instead of copying code.
# * Defensive Exception Guardrails -> Always wrap server handshakes inside `try/except` loops.
# * Clean Connection Management -> Use `with smtplib.SMTP()` to close connections automatically.
# * Production Grade Monitoring -> Swap out standard terminal `print` calls for official log files.
# * Optimize Network Handshakes -> Keep server logins OUTSIDE loops when sending bulk emails.
# =====================================================================
