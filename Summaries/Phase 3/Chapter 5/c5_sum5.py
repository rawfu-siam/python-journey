'''
Chapter5, topic - scheduling tasks — schedule library
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# Task Scheduling -> Setting an automated digital alarm clock for code.
# Schedule Library-> A simple tool to trigger functions using plain English.
# Heartbeat Loop  -> The background engine keeping the script's clock alive.
#
# =====================================================================
# 🎯 REAL-WORLD AGENCY NEED
# =====================================================================
# * Removes Manual Overhead -> Code runs autonomously 24/7 without human intervention.
# * Core Automation Tasks   -> Nightly scrapers, automated social posts, and daily reporting.
# * System Health Checks    -> Monitored server checks that alert teams instantly if code fails.
#
# =====================================================================
# ⚠️ COMMON BEGINNER TRAPS
# =====================================================================
# * Parentheses Mistake     -> Using job() inside .do() fires the task instantly and breaks it.
# * Missing Time Sleep      -> Omitting time.sleep(1) spikes the server CPU usage straight to 100%.
# * Volatile Memory Storage -> Alarms live in RAM; a server reboot wipes out all upcoming schedules.
#
# =====================================================================
# 🧪 SENIOR DEVELOPER GUARDRAILS
# =====================================================================
# * Decoupled Architecture  -> Keep core business actions isolated from scheduling timers.
# * Timezone Synchronization -> Cloud servers use UTC time; match target client time zones manually.
# * Job Self-Cancellation   -> Returning schedule.CancelJob cleanly removes a task from execution queues.
