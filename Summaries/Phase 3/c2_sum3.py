'''
Chapter2, topic - requests library — get(), post(), headers
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# requests library -> Python's digital smartphone to talk to the web.
# requests.get()   -> Asks a web server to GIVE you data (Read operation).
# requests.post()  -> Sends new data to a web server to SAVE (Write operation).
# response.json()  -> Magical translation tool converting web text to a Dict.

# =====================================================================
# 🛡️ THE PRODUCTION ENGINEER'S GUARDRAILS
# =====================================================================
# 1. Status Check -> Never parse .json() before checking .status_code == 200.
# 2. json= Param  -> Always pass payloads to json= (NOT data=) for clean APIs.
# 3. Timeout Rule -> Always set a timeout (e.g., timeout=5) so scripts don't freeze.
# 4. Credential   -> Never hardcode keys. Isolate tokens inside a hidden .env file.

# =====================================================================
# 🤵 THE REUSABLE SESSION BUTLER
# =====================================================================
# requests.Session() creates a persistent digital pipe to a web server.
# Benefits:
#   - Up to 3x faster executions (removes repetitive network handshakes).
#   - Automatically remembers authorization headers for all future requests.
