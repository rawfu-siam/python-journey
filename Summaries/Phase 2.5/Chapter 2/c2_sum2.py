'''
Chapter2, topic - Log levels — DEBUG, INFO, WARNING, ERROR, CRITICAL
'''
# =====================================================================
# 🧠 CORE LOG LEVELS & HIDDEN NUMERIC VALUES
# =====================================================================
# DEBUG    (10) -> Microscopic details. Used only by devs during testing.
# INFO     (20) -> Normal operations. Tracks happy business milestones.
# WARNING  (30) -> Unexpected hiccups. Something went wrong, bot recovered.
# ERROR    (40) -> Localized failure. An item broke, loop skips and goes on.
# CRITICAL (50) -> Total blackout. Complete script crash, human needed.

# =====================================================================
# 🏢 AGENCY PRODUCTION RULES & FILTERING LIFEHACKS
# =====================================================================
# 🎛️ THE FILTER RULE:
#   - Setting a threshold blocks any logs with values lower than that number.
#   - level=logging.WARNING will show WARNING, ERROR, and CRITICAL.
#   - It will completely hide and ignore DEBUG and INFO logs.
#
# 🤫 THE QUIET PRODUCTION RULE:
#   - In Sydney/Singapore agencies, keep live production servers quiet.
#   - Set live pipelines to WARNING or ERROR to save on cloud storage costs.
#   - Toggle to DEBUG via environment variables ONLY during bug triage.
#
# 🚨 EXCEPTION HANDLING MASTERY:
#   - Never hardcode "ERROR" strings inside logging.info().
#   - Inside except blocks, always use logging.exception().
#   - This automatically appends the exact Python traceback diagram.
#
# 🪄 THE AUTOMATION MANIFESTO:
#   - "Log for the machine in production; filter for the human in triage."
# =====================================================================
