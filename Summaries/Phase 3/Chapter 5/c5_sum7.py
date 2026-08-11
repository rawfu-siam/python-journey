'''
Chapter5, topic - working with dates and times — datetime
'''
# =====================================================================
# 🧠 CORE AUTOMATION DEFINITIONS
# =====================================================================
# date      -> Calendar tool only (Year, Month, Day). No time tracks.
# time      -> Clock tool only (Hour, Minute, Second, Microsecond).
# datetime  -> Ultimate combo engine. Holds both calendar and clock.
# timedelta -> Duration stopwatch. Used to add/subtract spans of time.

# =====================================================================
# ⚙️ THE STRING TRANSLATION RADAR
# =====================================================================
# 📥 strptime() -> [P]arse text. Turns raw string data into Python object.
#                  Example: datetime.strptime("2026-08-11", "%Y-%m-%d")
#
# 📤 strftime() -> [F]ormat object. Turns Python object into clean text string.
#                  Example: right_now.strftime("%Y-%m-%d %H:%M")

# =====================================================================
# 🛡️ THE ENTERPRISE ENGINE GUARDRAILS
# =====================================================================
# 🌍 Global Baseline -> Never calculate in local time. Run servers on UTC.
#                       Use `datetime.now(timezone.utc)` for calculations.
#
# 🤝 Border Sync     -> Use `zoneinfo.ZoneInfo` to safely shift zones.
#                       Never mix timezone-aware objects with naive ones.
#
# 🔗 Data Standards  -> Use `.isoformat()` (ISO 8601) when passing data to
#                       external APIs, webhooks, databases, or n8n nodes.
