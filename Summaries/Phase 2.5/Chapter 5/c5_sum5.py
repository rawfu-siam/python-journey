'''
Chapter5, topic - Pandera basics — validating tabular pandas DataFrames
                  (Data Engineering checkpoint)
'''
# =====================================================================
# 🧠 PANDERA CORE DEFINITIONS
# =====================================================================
# DataFrame  -> A digital spreadsheet or table with rows and columns (pandas).
# Tabular Data -> Data organized neatly in rows and columns.
# Pandera    -> An automated security guard library for pandas DataFrames.
# Schema     -> The strict rulebook defining allowed columns, types, and ranges.

# =====================================================================
# 🏛️ THE 5 BUILDING BLOCKS OF A PANDERA SCHEMA
# =====================================================================
# 1. import pandera as pa -> Bring in the validation library.
# 2. pa.DataFrameSchema   -> Create the master rulebook for the whole table.
# 3. pa.Column            -> Target a specific column name and enforce its type (String, Int, Float).
# 4. pa.Check             -> Add extra precise rules (e.g., greater_than, str_contains, lambda).
# 5. schema.validate(df)  -> Run the security guard check; raises ValidationError if broken.

# =====================================================================
# ⚠️ PRO BEST PRACTICES & COMMON TRAPS
# =====================================================================
# - Always use Pandera types (pa.String, pa.Int) instead of native python types.
# - Validate data immediately at the entry gate (APIs, Webhooks, Web Scrapers).
# - Use nullable=False for mandatory fields, nullable=True for optional gaps.
# - Isolate your schemas in a separate file (e.g., schemas.py) for clean architecture.
# - Catch validation errors with try/except and route diagnostics to Slack alerts.
