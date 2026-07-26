'''
Chapter2, topic - HTTP methods — GET, POST, PUT, DELETE
'''
# =====================================================================
# 🧠 MASTER LESSONS SUMMARY — HTTP METHODS IN PYTHON
# =====================================================================

# 1. 🔍 THE GET METHOD LESSONS:
#    - Purpose: Fetching, reading, and viewing data from an external server.
#    - Rule 1: It is read-only and safe. It never alters database records.
#    - Rule 2: Never pass a payload body via 'json=' into a GET request.
#    - Pro-Move: Always pass filters using 'params=' to generate clean URLs.

# 2. 📝 THE POST METHOD LESSONS:
#    - Purpose: Creating and saving brand-new data records on a server.
#    - Rule 1: Always requires a data cargo body passed via the 'json=' argument.
#    - Rule 2: It is non-idempotent. Repeating it creates unwanted duplicate entries.
#    - Pro-Move: Always verify if an item exists before firing a POST action.

# 3. 🔄 THE PUT METHOD LESSONS:
#    - Purpose: Modifying, replacing, and completely overwriting an entry.
#    - Rule 1: Requires a data cargo body holding the refreshed values.
#    - Rule 2: It is idempotent. Running it 5 times leaves the exact same state.
#    - Pro-Move: Target the exact record path to ensure precise data overwrites.

# 4. 🗑️ THE DELETE METHOD LESSONS:
#    - Purpose: Removing, destroying, and purging records from existence.
#    - Rule 1: Typically requires no data cargo payload body to clear an asset.
#    - Rule 2: It is idempotent. Deleting an item multiple times yields the same result.
#    - Pro-Move: Use with extreme caution as this completely eliminates records.

# 5. 🛠️ PRODUCTION & AGENCY GRADE BEST PRACTICES:
#    - Rule 1: Never hardcode API keys or secret endpoints inside code strings.
#    - Rule 2: Always isolate system configurations securely inside hidden '.env' files.
#    - Rule 3: Always pack web interactions into 'try / except' blocks to block crashes.
#    - Rule 4: Always apply a 'timeout=' constraint so scripts never lag indefinitely.
#    - Rule 5: Always track the 'status_code' value alongside the 'json()' response.
