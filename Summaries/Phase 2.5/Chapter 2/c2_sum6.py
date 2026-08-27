'''
Chapter2, topic - Creating a reusable logger.py utility module
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# Logger   -> The central tracking engine that monitors running scripts.
# Handler  -> The route controller sending text to Console or Files.
# Formatter-> The layout designer shaping timestamps & line numbers.
#
# 🧙 THE GOLDEN RULE OF ENTERPRISE AUTOMATION:
# "If it isn't logged with a timestamp, it never happened in production."
# =====================================================================

# =====================================================================
# 🚦 THE 5 SEVERITY LOG LEVELS (RANKED LOW TO HIGH)
# =====================================================================
# 1. DEBUG    🐛 -> Micro-details for debugging (Variables, paths).
# 2. INFO     ℹ️  -> Confirmation milestones (Script started, step done).
# 3. WARNING  ⚠️ -> Unexpected events, script can still continue safely.
# 4. ERROR    ❌ -> Feature crash (Web scraper failed, API timeout).
# 5. CRITICAL 🚨 -> Complete system death (Out of hard-drive space).
# =====================================================================

# =====================================================================
# 🛡️ THE ENTERPRISE REUSABLE LOGGER ARCHITECTURE (`logger.py`)
# =====================================================================
# • Dual Handlers       -> Prints INFO to screen, writes DEBUG to file.
# • Duplication Guard   -> Uses `hasHandlers()` check to block double logs.
# • Memory Safeguard    -> `RotatingFileHandler` splits files at size thresholds.
# • Automated Tracking  -> Passing `__name__` maps origin files instantly.
# • Crash Tracebacks    -> `logger.exception()` captures entire error trees.
# • Cloud-Readiness     -> Centralized `sys.stdout` streaming for cloud nodes.
