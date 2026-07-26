'''
Chapter2, topic - API keys — how to use and protect them
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & BUSINESS LOGIC
# =====================================================================
# API Key      -> A unique, secret string acting as a digital passport.
# Identity     -> Tells external servers exactly who is running the code.
# Metering     -> Tracks real-time script usage for billing and invoicing.
# Rate Limits  -> Prevents network traffic jams by controlling request speeds.
# Status 401   -> The universal HTTP gatekeeper response for 'Unauthorized'.

# =====================================================================
# 🧩 ARCHITECTURE & SECURITY IMPLEMENTATION
# =====================================================================
# Headers Tray -> Keys belong inside hidden metadata request headers.
# Bearer Token -> The standard structural string format: "Bearer YOUR_KEY".
# Hardcoding   -> Storing raw keys inside code. The ultimate production sin!
# .env File    -> A local, hidden plain-text file used to isolate secrets.
# .gitignore   -> The critical Git filter. Must include '.env' on line one.

# =====================================================================
# 🧪 ENTERPRISE MINDSET & AGENCY GUARDRAILS
# =====================================================================
# Empty Engine -> Treat code strictly as logic. Fuel it with external envs.
# Fail-Fast    -> Perform sanity checks on your keys on line one of execution.
# .env.example -> A dummy configuration blueprint file built for teammates.
# Least-Priv   -> Issue keys with the absolute lowest permissions required.
# Scanners     -> Use pre-commit hooks to detect accidental string leaks.

# =====================================================================
# 💻 SUMMARY IMPLEMENTATION PATTERN (PSEUDO-FLOW)
# =====================================================================
# 1. From dotenv import load_dotenv
# 2. Import os, sys
# 3. load_dotenv()
# 4. key = os.environ.get("TARGET_KEY")
# 5. If not key: print("Error") -> sys.exit(1)
# 6. headers = {"Authorization": f"Bearer {key}"}
