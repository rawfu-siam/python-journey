'''
Chapter4, topic - PostgreSQL basics — connecting via psycopg2
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# PostgreSQL -> A massive, enterprise-grade multi-user cloud filing cabinet.
# psycopg2   -> The low-level translation wire/driver linking Python to Postgres.
#
# THE 5-STEP DATABASE CONNECTION PIPELINE:
#   1. Connection String -> Credentials detailing Host, DB, User, Pass, Port.
#   2. Connection (conn)  -> The live active network pipe to the database server.
#   3. Cursor (cur)       -> The robotic hand executing queries inside tables.
#   4. Commit             -> Changing data from pencil to ink (saving permanently).
#   5. Close              -> Safely closing hand and pipe to free up server slots.

# =====================================================================
# 🛡️ THE SECURITY GUARDRAIL: PARAMETERIZED QUERIES
# =====================================================================
# DANGER ZONE (F-STRINGS):
#   - query = f"SELECT * FROM users WHERE name = '{user_input}';"
#   - Never use f-strings or raw concatenation for variables in database scripts.
#   - It merges code with untrusted data, exposing apps to SQL Injections.
#
# SAFE ZONE (PLACEHOLDERS):
#   - query = "SELECT * FROM users WHERE name = %s;"
#   - cur.execute(query, (user_input,))
#   - Always use '%s' placeholders and pass values in a separate data tuple.
#   - psycopg2 sanitizes input data blocks, rendering hacker scripts harmless.

# =====================================================================
# ⚠️ OPERATIONAL TRIPWIRES TO DODGE
# =====================================================================
# 1. No Commit = No Data:
#    - INSERT, UPDATE, and DELETE actions require a manual 'conn.commit()'.
#    - Forgetting it causes changes to vanish when the script closes.
#
# 2. Dangling Connections:
#    - Always clean up resource links using try/except/finally blocks.
#    - Leaving connection ports open can crash and lock up database servers.
#
# 3. Syntax Rules:
#    - Unlike SQLite which uses '?', psycopg2 strictly requires '%s'.

# =====================================================================
# 🦘 AUSTRALIAN AGENCY AUTOMATION INSIDER TIPS
# =====================================================================
# - Beat Pacific Ocean network latency by grouping queries together.
# - Avoid repeating 'cur.execute()' inside loops for large data transfers.
# - Leverage bulk actions like 'cur.executemany()' to package data in one trip.
# - Keep code neat and manageable by isolating connectors in a 'database.py'.
