'''
Chapter5, topic - Graceful handling of ValidationError exceptions
'''
# =====================================================================
# 🧠 GRACEFUL HANDLING OF PYDANTIC VALIDATIONERRORS 
# =====================================================================
# ValidationError -> Pydantic's alert when incoming data breaks the schema rules.
# Graceful Handling -> Catching the error so your app doesn't crash at midnight.
#
# =====================================================================
# 🛡️ THE CORE SAFETY NET PATTERN
# =====================================================================
#   - 📋 Schema   -> Define rules using Pydantic's `BaseModel`.
#   - ⚡ Try      -> Wrap raw data initialization in a `try:` block.
#   - 🛡️ Except   -> Catch the exact `except ValidationError as e:` block.
#   - 📝 Inspect  -> Read field errors safely via `e.errors()` or `e.json()`.
#
# =====================================================================
# ⚠️ CLASSIC BEGINNER MISTAKES TO AVOID
# =====================================================================
#   - Catching general `Exception` instead of specific `ValidationError`.
#   - Swallowing error messages completely without logging details (`e.errors()`).
#   - Confusing standard Python `ValueError` with Pydantic's `ValidationError`.
#
# =====================================================================
# 🏢 US AGENCY PRO TIPS
# =====================================================================
#   - Validate data at the absolute edge (front door) of your application.
#   - Skip bad rows silently in large batch loops, but send Slack alerts 
#     for high-value business failures (payments, crucial leads).
#   - Use framework defaults (like FastAPI's 422 responses) to cheat legally.
