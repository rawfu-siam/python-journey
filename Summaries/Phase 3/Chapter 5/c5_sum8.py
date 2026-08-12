'''
Chapter5, topic - logging — proper log files for production
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# Logging   -> A built-in system to record code activity into a permanent diary.
# print()   -> Ephemeral data output. Shouts into a vacuum; lost when terminal closes.
# File Log  -> Persistent diagnostic evidence stored securely on the host machine.
#
# =====================================================================
# 📶 THE URGENCY METRIC (LOG LEVELS)
# =====================================================================
# 🐛 DEBUG    -> Minute technical clues. Used strictly by engineers for parsing bugs.
# ℹ️ INFO     -> General milestone markers verifying operations run within margins.
# ⚠️ WARNING  -> Minor anomalies caught; execution continues without degradation.
# ❌ ERROR    -> Failure event isolation. Features break, but master script lives.
# 🚨 CRITICAL -> Total infrastructure collapse. Pipeline terminates immediately.
#
# =====================================================================
# 🏗️ ENTERPRISE ARCHITECTURE INTEGRITY
# =====================================================================
# 🖥️ StreamHandler      -> Directs log traffic to live terminal console.
# 💾 FileHandler        -> Appends structured text directly to disk files.
# 🔄 RotatingHandler   -> Limits log file byte-sizes; archives old splits to save storage.
# 🎨 Formatter          -> Dynamically injects Timestamps, Filenames, and Row Indexes.
#
# =====================================================================
# ⚠️ JUNIOR DEFENSE CHECKPOINTS & PITFALLS
# =====================================================================
# 1. Never use filemode="w" in production config; it deletes logs on crashes. Use "a".
# 2. Never expose consumer passwords, tokens, or secret API strings in raw logs.
# 3. Always invoke exc_info=True inside exception handlers to preserve trackbacks.
# 4. Decouple pipeline logic from logger configurations by using a "logger_config.py".
