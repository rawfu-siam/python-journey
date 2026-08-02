'''
Chapter4, topic - CRUD operations in Python
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & THE FOUR PILLARS
# =====================================================================
# CRUD stands for the four foundational actions allowed on any database:
#   - C -> CREATE : Adding brand-new rows/records into a data table.
#   - R -> READ   : Querying, looking up, or searching stored data.
#   - U -> UPDATE : Modifying values inside an already existing record.
#   - D -> DELETE : Permanently destroying or wiping out a data row.
#
# Without CRUD infrastructure, automated script data is highly volatile.
# Data stored in regular Python variables completely vanishes from memory 
# (RAM) the second the automation runner or background worker shuts down.

# =====================================================================
# 🏢 SQL COMMAND CORRESPONDENCE (THE ENGINE ROOM)
# =====================================================================
# Each CRUD operation maps directly to an explicit SQL syntax statement:
#   - CREATE -> Uses `INSERT INTO table_name (cols) VALUES (?, ?);`
#   - READ   -> Uses `SELECT cols FROM table_name WHERE condition;`
#   - UPDATE -> Uses `UPDATE table_name SET col = ? WHERE condition;`
#   - DELETE -> Uses `DELETE FROM table_name WHERE condition;`
#
# 🤝 THE COMMIT RULE: Create, Update, and Delete operations require a 
# execution handshake calling `.commit()` to permanently write to disk.

# =====================================================================
# ⚠️ JUNIOR DEVELOPER PITFALLS & THE DANGER ZONE
# =====================================================================
# 💥 Missing WHERE Trap:
#   - Forgetting a `WHERE` condition on an UPDATE or DELETE command clears
#     or alters every single row in the database instantly.
# ⚓ Single-Element Tuple Bug:
#   - Passing a solo parameter into an execute statement requires a 
#     trailing comma, for example: `(target_id,)` instead of `(target_id)`.
# 🔓 Resource Leaks:
#   - Forgetting to invoke `.close()` can easily lock database files and 
#     crash concurrent background workers running in multi-agent pipelines.

# =====================================================================
# 🇦🇺 AGENCY-GRADE PRODUCTION EXPECTATIONS (SENIOR DEV RULES)
# =====================================================================
# 🛡️ Zero-Trust SQL Injection Defense:
#   - Never inject variables into SQL commands using Python f-strings!
#   - Always pass values as tuple queries paired with `?` placeholders.
# 🧹 Context Manager Hygiene:
#   - Swap manual connect/close chains for python standard `with` statements.
#   - Automatically manages connection boundaries and safely closes tasks.
# 🪵 Enterprise Traceability:
#   - Ban the use of `print()` inside core data access operations.
#   - Track query pipelines using rotating log utility modules instead.
