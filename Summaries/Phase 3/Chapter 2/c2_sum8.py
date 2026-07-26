'''
Chapter2, topic - error handling for API failures
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# API Error Handling -> Safety-net code protecting scripts from external crashes.
# Happy Path         -> The ideal blueprint where APIs always work flawlessly.
# Unhappy Path       -> Real-world chaos: down servers, timeouts, dead internet.
# Blast Radius       -> How much of an app dies when one small API call fails.

# =====================================================================
# 📊 THE HTTP STATUS CODE REF MATRIX
# =====================================================================
# 🟢 2xx: Success       -> "No worries, mate!" (e.g., 200 OK)
# 🟡 4xx: Client Error  -> Your fault! (e.g., 401 Unauthorized, 404 Not Found)
# 🔴 5xx: Server Error  -> Their fault! (e.g., 500 Internal Error, 503 Overload)

# =====================================================================
# 🛡️ THE REQUESTS EXCEPTION HIERARCHY
# =====================================================================
# RequestException      -> Grandparent of all requests errors (catches everything).
# ├── HTTPError         -> Triggered manually by calling response.raise_for_status()
# ├── ConnectionError   -> Local internet down or server domain name is fake.
# └── Timeout           -> Server took too long to reply; script pulled the plug.

# =====================================================================
# ⚠️ THE JUNIOR TRAPS TO AVOID
# =====================================================================
# 🚨 Bare Except        -> Writing 'except:' catches syntax/typos. Never do it.
# 🚨 Silent Catch       -> Putting 'pass' in except blocks leaves zero diagnostic logs.
# 🚨 Naked Requests     -> Leaving out 'timeout=' parameters hangs processes forever.

# =====================================================================
# 🇦🇺 AGENCY-GRADE DEV STRATEGIES
# =====================================================================
# 1. Micro-Try Blocks   -> Keep try scopes tight to pinpoint specific error locales.
# 2. Central Settings   -> Use global constants like API_TIMEOUT = 5 for easy updates.
# 3. Log vs Print       -> Replace terminal print() blocks with rotating file loggers.
# 4. Fallback Logic     -> Code smart alternative endpoints if premium APIs go down.
# 5. Slack Alerts       -> Pipe unhandled exceptions into team channels automatically.
