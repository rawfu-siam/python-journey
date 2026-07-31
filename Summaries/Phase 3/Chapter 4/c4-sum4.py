'''
Chapter4, topic - WHERE, ORDER BY, GROUP BY, JOIN
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & KEYWORD SUMMARY
# =====================================================================
# WHERE    -> The Bouncer 🕵️‍♂️. Filters rows out based on explicit conditions.
# ORDER BY -> The Organizer 📐. Sorts records neatly (ASC/DESC).
# GROUP BY -> The Bucket Creator 🪣. Combines rows into aggregate data summaries.
# JOIN     -> The Matchmaker 🤝. Temporarily glues multiple tables together.

# =====================================================================
# ⏳ UNBREAKABLE EXECUTION & SYNTAX SEQUENCE
# =====================================================================
# Your SQL queries must ALWAYS follow this exact structural sequence:
# 1. SELECT   -> Specify the exact columns you want to view.
# 2. FROM     -> Declare the primary base table.
# 3. JOIN     -> Attach extra tables using 'ON table1.id = table2.id'.
# 4. WHERE    -> Filter out rows early to protect computer memory.
# 5. GROUP BY -> Consolidate duplicate criteria rows into matching buckets.
# 6. ORDER BY -> Sort the output result list rows before displaying.

# =====================================================================
# 🪣 AGGREGATE FUNCTIONS FOR GROUP BY BUCKETS
# =====================================================================
# COUNT()  -> Counts total matching row records inside each bucket.
# SUM()    -> Adds all numerical column values inside each bucket together.
# AVG()    -> Calculates the mathematical mean value inside each bucket.

# =====================================================================
# 🚨 COMMON MISTAKES TO AVOID
# =====================================================================
# * Writing WHERE after ORDER BY will throw an immediate syntax crash.
# * Selecting columns that aren't grouped or inside a math function.
# * Forgetting to prefix shared column IDs with 'table_name.column_name'.

# =====================================================================
# 🇦🇺 SENIOR ENGINEERING AGENCY INSIGHTS
# =====================================================================
# * Never use 'SELECT *' in automated scripts; fetch target columns only.
# * Write SQL keywords in ALL CAPS to keep codes clean and readable.
# * Filter data with WHERE inside SQL rather than filtering in Python loops.
# * Always handle connections using context manager 'with' blocks.
