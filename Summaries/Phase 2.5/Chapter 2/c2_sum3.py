'''
Chapter2, topic - Log formatters — timestamps, log levels, file names, line numbers
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# Log Formatter -> A structural rulebook defining layout templates for logs.
# basicConfig()  -> The one-shot initialization tool to lock layout rules.
# Placeholder   -> Dynamic `%()` string injection codes swapped at runtime.
#
# =====================================================================
# 🛠️ THE 5 PILLARS OF ENTERPRISE LOG FORMATTING
# =====================================================================
# %(asctime)s   -> Automates precise date and millisecond tracking.
# %(levelname)s -> Affixes severity badges (INFO, WARNING, ERROR).
# %(filename)s  -> Identifies the source code file communicating.
# %(lineno)d    -> Pinpoints exact code lines. Ends with 'd' for Digits.
# %(message)s   -> Delivers custom human text or error exceptions.
#
# =====================================================================
# ⚠️ CRITICAL AMATEUR TRAPS TO AVOID
# =====================================================================
# 1. Type Typos: Using '%(lineno)s' crashes scripts. It MUST be '%(lineno)d'.
# 2. Naked Logs: Stripping time/levels turns loggers into useless print().
# 3. Multi-Calls: Initializing basicConfig twice is silently ignored.
#
# =====================================================================
# 💼 PRO AUTOMATION DEV STRATEGIES (AU/SG AGENCY STANDARDS)
# =====================================================================
# 1. Laziness Rule: Build an isolated 'logger.py' utility once; import it daily.
# 2. Time Unity  : Force 'time.gmtime' converter to keep all logs in UTC format.
# 3. Extra Payload: Use the 'extra={}' dict parameter for clean data injection.
# 4. Privacy Wall : Strip PII (passwords, tokens) before logs touch formatters.
#
# =====================================================================
# 🪄 THE MAGIC SPELL
# =====================================================================
# "Format once at the root, log everywhere with absolute context."
# =====================================================================
