'''
Chapter2, topic - authentication — Bearer tokens, OAuth basics
'''
# =====================================================================
# 🧠 CORE SECURITY DEFINITIONS
# =====================================================================
# Authentication (AuthN) -> Proving *who* your Python automation script is.
# Authorization (AuthZ)  -> Checking *what* actions your script is allowed to do.
# Bearer Token           -> A secret string value. The holder ("bearer") gets
#                           instant access without needing a master password.
# OAuth                  -> A secure framework enabling apps to grant limited,
#                           safe access to data without exposing user passwords.
# Scope                  -> Fine-grained permission settings (e.g., read-only)
#                           that restrict what an issued OAuth token can touch.

# =====================================================================
# 🗂️ THE AUTHORIZATION HEADER PATTERN
# =====================================================================
# - Every standard requests call wraps credentials inside the headers dict.
# - Key must be exactly: "Authorization"
# - Value must be exactly: "Bearer " + the secret token string.
# - DANGER: Forgetting the explicit single space after "Bearer" causes 401 errors.
#
# Correct Template:
# headers = {"Authorization": f"Bearer {SECRET_TOKEN}"}

# =====================================================================
# 🪓 THE JUNIOR DEV TRAPS & ANTIPATTERNS
# =====================================================================
# 1. Hardcoding Keys -> Pasting strings directly in the codebase. This leaks
#                       instantly if pushed to GitHub. Fix: Use python-dotenv.
# 2. Silent Death    -> Letting a token expiration crash a production script.
#                       Fix: Catch errors and send Slack alert diagnostics.
# 3. Scope Confusion -> Assuming a valid token can delete data when its scope
#                       is restricted to read-only, leading to 403 Forbidden errors.

# =====================================================================
# 🇦🇺 AUSTRALIAN AGENCY ENTERPRISE STANDARDS
# =====================================================================
# - Zero-Trust Guardrails: Add safety checkpoints at application startup.
#   Always exit execution early if required environment tokens are missing.
# - Token Isolation: Main code houses logic; .env files house identity.
# - Safe Team Operations: Maintain a clean .env.example file in the repo root
#   so senior developers can reproduce your local environment flawlessly.
# - Masked Logging: Never output full raw secret tokens into app logs or screens.
