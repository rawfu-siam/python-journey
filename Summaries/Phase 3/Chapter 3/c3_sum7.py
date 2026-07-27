'''
Chapter3, topic - storing scraped data to CSV/JSON
'''
# =====================================================================
# 🧠 CSV & JSON CONCEPTS
# =====================================================================
# CSV  -> Comma-Separated Values. Flat table format, row-by-row layout.
#      -> Ultimate business deliverable for Excel & CRM imports.
# JSON -> JavaScript Object Notation. Nested key-value dictionary layout.
#      -> Universal language of AI Models, APIs, and low-code n8n nodes.
#
# =====================================================================
# 🛠️ NATIVE PYTHON WRITE PATTERNS
# =====================================================================
# 📊 CSV Writing (Lists of Lists):
#   - Use `csv.writer(file)`
#   - `writer.writerow(headers)` sets column templates.
#   - `writer.writerows(matrix_rows)` writes all records at once.
#
# 📊 CSV DictWriter (Lists of Dictionaries):
#   - Use `csv.DictWriter(file, fieldnames=headers)`
#   - Maps object keys directly to matching spreadsheet columns.
#   - `writer.writeheader()` automatically deploys top fields.
#
# 📦 JSON Writing:
#   - Use `json.dump(data_object, file, indent=4)`
#   - Always inject `indent=4` to keep structural files readable.
#   - JSON Appends: Never use file mode "a". Read -> Append -> Save.
#
# =====================================================================
# 🛡️ THE PRODUCTION SPRINT GUARDRAILS (SENIOR DEV RULES)
# =====================================================================
# 1. Windows Blank Lines Fix -> Always pass `newline=""` into `open()`.
# 2. Character Crash Fix    -> Always pass `encoding="utf-8"` into `open()`.
# 3. Dynamic Pathing Fix    -> Import `pathlib.Path` to bypass cloud crashes.
# 4. Version Tracking Fix   -> Ingest `datetime` metrics into asset names.
# =====================================================================
