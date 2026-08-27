'''
Chapter3, topic - Credential hygiene principles — why raw strings break security
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# Credentials     -> Sensitive digital access keys (API keys, passwords).
# Hygiene         -> Best practices for keeping secrets safe from exposure.
# Raw Strings     -> Hardcoding actual secrets as text directly in code.
# Environment     -> The space where code runs (e.g., Local laptop vs Cloud).
#
# Golden Rule     -> "Code is public; credentials are private." 🔒

# =====================================================================
# 🛡️ THE THREE-LAYER ENTERPRISE SHIELD
# =====================================================================
# 1. 📄 The Vault (`.env`)
#    - A hidden plain-text configuration file stored in the project root.
#    - Stores sensitive keys as pairs (e.g., OPENAI_KEY=sk-proj-xyz).
#    - Must NEVER be shared, emailed, or tracked by version control.
#
# 2. 🙈 The Shield (`.gitignore`)
#    - A configuration file that tells Git exactly what to ignore.
#    - Must explicitly include `.env` before your first Git commit.
#    - Bypasses tracking so secrets stay on your local machine or server.
#
# 3. 🧪 The Bridge (`os.environ`)
#    - Built-in Python engine module used to interface with the system.
#    - `os.environ.get("KEY")` extracts the string value safely at runtime.
#    - Safer than square brackets because it returns None instead of a crash.

# =====================================================================
# ⚠️ PROFESSIONAL MISTAKES TO AVOID
# =====================================================================
# 🚨 Mistake 1 -> Pushing raw .env files to GitHub (Leaks keys to scraper bots).
# 🚨 Mistake 2 -> Logging/printing raw credentials to the console or logs.
# 🚨 Mistake 3 -> Hardcoding keys inside helper dicts or deep within files.
# 🚨 Mistake 4 -> Forgetting to provide a team template file (`.env.example`).

# =====================================================================
# 🚀 AGENCY BEST PRACTICES FOR JUNIOR DEVS
# =====================================================================
# ✅ Treat every repository like it is going public on the internet.
# ✅ Implement "Fail-Fast" architecture by checking keys on startup.
# ✅ Maintain a clean `.env.example` file for seamless team onboarding.
# ✅ Inject quick terminal variables using: KEY=value python script.py
