'''
Chapter4, topic - CREATE, INSERT, SELECT, UPDATE, DELETE
'''
# =====================================================================
# 🧠 CORE SQL COMMAND DEFINITIONS (CRUD)
# =====================================================================
# CREATE TABLE -> Tells the database to build a brand new empty table container.
# INSERT INTO  -> Adds fresh rows of data into an existing table structure.
# SELECT       -> Looks up, filters, and reads data cards from the database drawers.
# UPDATE       -> Edits or fixes existing cellular values inside specific rows.
# DELETE FROM  -> Permanently shreds and deletes unwanted records from a table.

# =====================================================================
# 🗂️ THE 5 MAGIC SPELLS: ANATOMY BREAKDOWN
# =====================================================================
# 1. 🏗️ STRUCTURING THE CABINET (CREATE):
#    CREATE TABLE IF NOT EXISTS users (
#        id INTEGER PRIMARY KEY,   # Essential unique identification passport
#        name TEXT,                # Equivalent to a Python string type
#        balance REAL              # Equivalent to a Python float decimal type
#    );
#
# 2. 📥 DROPPING DATA CARD IN (INSERT):
#    INSERT INTO users (id, name, balance) VALUES (1, 'Mateo', 150.75);
#
# 3. 👀 READING RECORD DATA (SELECT):
#    SELECT name, balance FROM users WHERE balance > 100.0;
#    # Pro-tip: Always list target columns explicitly instead of using 'SELECT *'
#
# 4. ✏️ EDITTING INNER CELLS (UPDATE):
#    UPDATE users SET balance = 200.0 WHERE id = 1;
#    # WARNING: Omitting the WHERE filter will overwrite every single row!
#
# 5. 🗑️ CLEARING OLD DATA (DELETE):
#    DELETE FROM users WHERE id = 1;
#    # WARNING: Omitting the WHERE filter will completely wipe the whole table clean!

# =====================================================================
# 🛡️ ENTERPRISE GUARDRAILS & SENIOR DESIGN PATTERNS
# =====================================================================
# 🔐 BLOCKING SQL INJECTION:
#   - Never use Python f-strings or raw string formatting to pass variables to SQL.
#   - Always apply placeholder parameter markers: cursor.execute("...", (variable,))
#
# 🔋 ATOMIC OPERATIONS & MANAGING SYSTEM RESOURCES:
#   - Wrap actions using Python's native context manager block: 'with sqlite3.connect() as conn:'
#   - Context blocks auto-commit edits and securely close connections during crashes.
#   - Capitalize SQL operational terms (SELECT, FROM, WHERE) to keep code clean.
