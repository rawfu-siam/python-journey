'''
Chapter8, topic - environment variables in Docker
'''
# =====================================================================
# 🧠 DOCKER ENVIRONMENT VARIABLES: THE AGENCY MANUAL
# =====================================================================
# Definition -> External "sticky notes" injected into isolated Docker
#               containers at boot time to alter script behavior.
# Core Rule  -> Keep code static and configuration dynamic. NEVER bake
#               passwords, tokens, or system keys into source images.
#
# =====================================================================
# 🧩 THREE-PART CONFIGURATION ENGINE
# =====================================================================
# 1. 🐍 Python Layer    -> Reads variables safely using `os.environ.get()`
#                           without hardcoding strings into code files.
# 2. 🐳 Dockerfile Layer -> Defines non-sensitive safe fallback values
#                           using the internal `ENV KEY=VALUE` directive.
# 3. 🚀 Runtime Layer    -> Injects production overrides dynamically 
#                           using `-e KEY=VALUE` or `--env-file .env`.
#
# =====================================================================
# ⚠️ THE JUNIOR LANDMINES TO AVOID
# =====================================================================
# 🔒 Git Leakage     -> Never commit `.env` files. Block them early using 
#                        a `.gitignore` file and ship `.env.example` templates.
# 🧵 String Typing   -> Remember: Docker variables arrive in Python as raw
#                        strings. Explicitly check for `"True"` or `"False"`.
# 🔠 Case Matching   -> Environment keys are strictly case-sensitive. Use
#                        universal UPPERCASE standard names by convention.
#
# =====================================================================
# 🏢 AGENCY WORKFLOW BEST PRACTICES
# =====================================================================
# 💥 Fail Loudly     -> Exit immediately (`sys.exit(1)`) if a critical API 
#                        credential or database link is missing at startup.
# 🛡️ Safe Logging    -> Do not output whole keys to standard console outputs;
#                        protect active access credentials inside logs.
# ⚙️ Clean Schemes   -> Use `pydantic-settings` to auto-parse and validate
#                        injected runtime variables with zero manual code.
