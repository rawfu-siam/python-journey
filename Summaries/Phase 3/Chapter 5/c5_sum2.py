'''
Chapter5, topic - Excel automation — openpyxl
'''
# =====================================================================
# 🧠 CORE AUTOMATION DEFINITIONS
# =====================================================================
# openpyxl   -> A Python library used to read, write, and edit .xlsx files.
# Workbook   -> The master Python object representing the whole Excel file.
# Worksheet  -> An individual sheet tab inside the file binder (e.g., Sheet1).
# Cell       -> A single coordinate block (like A1) holding a discrete value.
#
# =====================================================================
# 🏢 FILE OPERATIONS RULEBOOK
# =====================================================================
# 🆕 Fresh File:  Use openpyxl.Workbook() to spawn a blank file in RAM memory.
# 📂 Load File:   Use openpyxl.load_workbook("file.xlsx") to read existing files.
# 💾 Hard Disk:   Changes stay in RAM until you explicitly call wb.save("name.xlsx").
# 🔒 File Lock:   Always close Excel on your desktop or Python throws PermissionError.
#
# =====================================================================
# ⚡ PRODUCTION AUTOMATION BLUEPRINTS
# =====================================================================
# 1. Row Insertion: Use ws.append([data]) to automatically push to the bottom row.
# 2. Iteration:     Use ws.iter_rows(values_only=True) to extract raw data streams.
# 3. Clean Code:    Always separate numeric data logic from cell background styling.
# 4. Pro Finish:    Loop column widths dynamically to prevent cut-off visual layout text.
# 5. Resource Care: Call wb.close() after saving files to maintain high server health.
