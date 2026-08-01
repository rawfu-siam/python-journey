'''
Chapter4, topic - database design — tables, keys, relationships
'''
# =====================================================================
# 🧠 DATABASE DESIGN REFERENCE SHEET (TABLES, KEYS, RELATIONSHIPS)
# =====================================================================
# This reference file outlines agency-grade data modeling structures.
# Use this configuration to guarantee clean, non-duplicated production schemas.

# =====================================================================
# 📊 CORE LAYOUT ELEMENTS
# =====================================================================
# Table    -> A structured data sheet made of clean Columns & rows.
# Column   -> The structural pillar defining the data type constraint.
# Row      -> One unique individual object entry (Record).

# =====================================================================
# 🔑 THE KEY CODES
# =====================================================================
# Primary Key (PK) -> Completely unique row ID passport. Never blank/Null.
# Foreign Key (FK) -> A copy of an external PK used to lock tables together.

# =====================================================================
# 🎭 LINK TYPES & HANDSHAKES
# =====================================================================
# 1. One-to-Many (1:N) [Most Common]:
#    - Rule: One entity maps to multiple target entries.
#    - Build: Place parent PK as an FK inside the child table.
#    - Example: One Client -> Many Automated Invoices.
#
# 2. One-to-One (1:1):
#    - Rule: An individual row maps to exactly one individual target row.
#    - Build: Place parent PK as an FK with a strict 'unique=True' flag.
#    - Example: One Employee -> One Assigned Workspace Laptop.
#
# 3. Many-to-Many (N:M):
#    - Rule: Multiple entries link to multiple external items.
#    - Build: Never link directly! Use a separate Junction/Bridge Table.
#    - Example: One Student -> Many Classes | One Class -> Many Students.

# =====================================================================
# ⚠️ AGENCY BEST PRACTICES (SENIOR DEV GUARDRAILS)
# =====================================================================
# - Keep Data DRY: Never duplicate structural info. Split into tables.
# - Guard Constraints: Enforce 'nullable=False' on required FK columns.
# - Production Security: Use UUIDs instead of simple 1,2,3 IDs for public URLs.
# - Schema Integrity: Use Alembic for tracking migration layouts in Git.
