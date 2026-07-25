'''
Chapter2, topic - environment variables (.env files)
'''
# =====================================================================
# 🧠 CORE CONFIGURATION & ENVIRONMENT DEFINITIONS
# =====================================================================
# Environment Variable -> A setting/secret kept completely outside code.
# .env File            -> A local text file storing secret keys and values.
# .gitignore File      -> A bouncer file that stops secrets going to GitHub.
# python-dotenv        -> The library used to load keys into memory.
#
# Rule 1: Always name the file exactly `.env` (no front name, no extension).
# Rule 2: Write parameters as `KEY=VALUE` with NO spaces around the `=` sign.
# Rule 3: Do NOT use quotation marks around strings inside the .env file.

# =====================================================================
# 🎛️ CORE IMPLEMENTATION WORKFLOW (STEP-BY-STEP EXECUTIONS)
# =====================================================================
# 1. Install dependency via terminal: `pip install python-dotenv`
# 2. Add `.env` as a clean string inside your local `.gitignore` file.
# 3. Call `load_dotenv()` at the absolute top of your main execution script.
# 4. Extract data safely using `os.environ.get("KEY_NAME", "DEFAULT_FALLBACK")`.

# =====================================================================
# 🏢 ENTERPRISE & AUSTRALIAN AGENCY STANDARDS
# =====================================================================
# Type Casting   -> Keys always load as strings. Cast them via int() or float().
# .env.example   -> A blank structural template file committed to GitHub.
# Crash-Safe     -> Use sys.exit(1) loops to block startup if keys are missing.
# Swapping Mode  -> Toggle backend routing smoothly without rewriting scripts.
