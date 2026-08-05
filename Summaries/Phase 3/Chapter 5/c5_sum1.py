'''
Chapter5, topic - CSV processing — csv module and pandas basics
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# CSV    -> Comma-Separated Values. Plain text grid files with zero formatting.
# reader -> Built-in stream engine parsing raw text into row-by-row lists.
# writer -> Built-in writing engine converting lists to comma-separated text.
# df     -> DataFrame. Pandas memory-resident interactive data matrix.

# =====================================================================
# 🛠️ NATIVE CSV MODULE VS. PANDAS SELECTION RULES
# =====================================================================
# 🐍 Native csv:
#   - Memory efficient. Streams files row-by-row without overhead.
#   - Best choice for simple file creation or massive multi-gigabyte logs.
#   - Requires manual iteration loops and positional element index array parsing.
#
# 🐼 Pandas Basics:
#   - Highly optimized. Loads the entire dataset as an in-memory database table.
#   - Best choice for column filtering, aggregation math, and fast slicing.
#   - Automatically converts numbers and strings into standard types.

# =====================================================================
# 🛡️ THE ENTERPRISE INTERPOLATION GUARDRAILS
# =====================================================================
# 🪟 Windows Fix   -> Always pass `newline=""` inside open() to avoid blank rows.
# 🌍 Unicode Fix   -> Explicitly specify `encoding="utf-8"` to handle special characters.
# 🛑 Crash Control -> Run `if not row: continue` checks to safely skip empty trailing lines.
# 📤 Export Clean  -> Always pass `index=False` inside `.to_csv()` to omit index columns.
# 🦘 Agency Standard -> Filter payload columns before calling LLMs to minimize costs.
