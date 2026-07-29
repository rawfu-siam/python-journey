'''
Chapter4, topic - what is a database and why it matters
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & FUNDAMENTALS
# =====================================================================
# Database   -> A permanent digital filing cabinet storing data safely on a disk.
# Persistent -> Unlike variables, database data survives script restarts.
# SQL        -> Structured Query Language. The universal dialect of databases.
# Schema     -> The blueprints, layout, and structural design of data tables.

# =====================================================================
# 🗄️ THE ARCHITECTURE BREAKDOWN
# =====================================================================
# Database    -> The master office filing cabinet containing multiple drawers.
# Table       -> A distinct drawer (e.g., `users`, `orders`). Holds structured data.
# Column      -> Table headers specifying data rules (e.g., `id`, `name`, `age`).
# Row / Record-> A single vertical slice containing one complete entry of data.
# Primary Key -> A completely unique data fingerprint column (usually an auto-incrementing ID).

# =====================================================================
# 🛡️ STRICT DATA TYPE GUARDRAILS
# =====================================================================
# TEXT / VARCHAR -> Handles all text formats (usernames, strings, emails).
# INTEGER        -> Handles all whole number records (count, index, age).
# REAL / FLOAT   -> Handles all precise decimal structures (currency, metrics).

# =====================================================================
# 🛠️ THE LOGICAL WORKFLOW (THE CRUD CHECKLIST)
# =====================================================================
# Create -> Adds fresh records safely into a table     -> SQL Command: `INSERT INTO`
# Read   -> Fetches or searches stored records         -> SQL Command: `SELECT FROM`
# Update -> Alters historical details of records       -> SQL Command: `UPDATE SET`
# Delete -> Removes unwanted records from system files -> SQL Command: `DELETE FROM`

# =====================================================================
# ⚠️ SENIOR DEV PRODUCTION GUARDRAILS & TRAPS TO AVOID
# =====================================================================
# 1. Forget to Commit   -> Always use `connection.commit()` to lock in changes.
# 2. Connection Leaks   -> Always call `connection.close()` or leverage `with` blocks.
# 3. SQL Injection Risk -> NEVER use f-strings for queries. Use `?` placeholders.
# 4. Idempotency        -> Use protective clauses like `CREATE TABLE IF NOT EXISTS`.
# 5. Fault-Tolerance    -> Wrap interactions inside `try/except` with a `rollback()`.
