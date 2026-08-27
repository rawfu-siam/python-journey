'''
Chapter2, topic - RotatingFileHandler — setting maxBytes and backupCount 
to prevent memory overflow
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# RotatingFileHandler -> A smart, automatic file manager for logging.
# maxBytes            -> The weight limit. Triggers file swap when reached.
# backupCount         -> The history tracker limit. Tells how many files to keep.
# Memory Overflow     -> App crash caused by log text completely filling the disk.

# =====================================================================
# 🏢 ENTERPRISE PRODUCTION FOOTPRINT CONCEPTS
# =====================================================================
# 📊 THE STORAGE FORMULA:
#   - Total Max Space = maxBytes * (backupCount + 1)
#   - A 50KB cap with a backupCount of 3 limits total logs to 200KB max.
#   - Safe limits guarantee predictable cloud costs for clients.
#
# 🛡️ THE PRODUCTION CHECKLIST:
#   - Always block duplicate handlers using: if not logger.hasHandlers():
#   - Avoid backupCount=0 unless you want your history erased on rotation.
#   - Never push generated text data to code repositories. Keep `*.log` in `.gitignore`.
#   - Read limit sizes dynamically from `.env` instead of hardcoding values.

# =====================================================================
# 🧙‍♂️ THE AUTOMATION DEV MAGIC SPELL
# =====================================================================
# "Set it, cap it, forget it—predictable boundaries prevent production crashes."
