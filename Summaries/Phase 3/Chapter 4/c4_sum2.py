'''
Chapter4, topic - SQLite with Python — sqlite3 module
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# SQLite   -> A built-in, lightweight, serverless relational database.
#             Stores permanent structured data inside one single file.
# sqlite3  -> The native Python module used to talk to the database file.
#
# Connection (conn) -> The active pipeline or cable to the database file.
# Cursor (cursor)   -> The robotic mouse tool used to execute SQL queries
#                      and pull data rows back into Python variables.

# =====================================================================
# 🗄️ DATABASE ANATOMY & STRUCTURE
# =====================================================================
# Database File -> The main container housing all project data.
# Tables        -> Grid sheets (like Excel) holding topic-specific data.
# Columns       -> Vertical blueprints defining strict type rules (TEXT, INT).
# Rows          -> Horizontal individual entries containing actual data records.

# =====================================================================
# 🛡️ THE 5-STEP LIFECYCLE & SECURITY RULES
# =====================================================================
# 1. CONNECT -> Open pipeline via sqlite3.connect("filename.db")
# 2. CURSOR  -> Spin up cursor instance via conn.cursor()
# 3. EXECUTE -> Send raw SQL string command using cursor.execute()
# 4. COMMIT  -> Permanently save changes via conn.commit() (Critical!)
# 5. CLOSE   -> Safely shut down pipeline using conn.close()
#
# ⚠️ ZERO-TRUST SECURITY RULE:
# Never inject Python variables into queries using f-strings or '+'.
# Always use safe '?' placeholders to prevent SQL Injection attacks.

# =====================================================================
# 🇦🇺 AGENCY-GRADE BEST PRACTICES
# =====================================================================
# 💎 Idempotency: Always append "IF NOT EXISTS" to table creation queries.
# 💎 Context Managers: Use "with sqlite3.connect() as conn:" blocks to 
#      guarantee files close safely even if background scripts crash.
# 💎 Single Source of Truth: Prevent data duplication across tables by 
#      relying on unique ID relational keys instead of raw data copies.
