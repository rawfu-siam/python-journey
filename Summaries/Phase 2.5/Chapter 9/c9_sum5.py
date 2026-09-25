'''
Chapter9, topic - Tenacity integration — wrapping flaky network requests
                  or scrapers in self-healing exponential backoff decorators
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & TERMINOLOGY
# =====================================================================
# Tenacity    -> A self-healing Python library used to retry failing tasks.
# Decorator   -> A magic wrapper (@retry) that adds powers to functions.
# Flaky Call  -> A function that randomly breaks due to external issues.
# Backoff     -> Smartly increasing sleep times to prevent server spam.

# =====================================================================
# 🛠️ STRATEGY & CONFIGURATION CHEAT SHEET
# =====================================================================
# 🔄 STOP CONDITIONS:
#   - stop_after_attempt(n) -> Gives up completely after 'n' tries.
#   - stop_after_delay(s)   -> Gives up if 's' total seconds pass by.
#
# ⏳ WAIT STRATEGIES:
#   - wait_fixed(s)        -> Sleeps an exact, flat number of seconds.
#   - wait_exponential()   -> Doubles the delay time after every failure.
#   - wait_random_expon()  -> Doubles delay + adds "Jitter" (random gap).
#
# 🎯 TARGETED ISOLATION:
#   - retry_if_exception_type(Err) -> Only retry specific network faults.
#   - before_sleep=my_func         -> Fires a custom log before sleeping.

# =====================================================================
# 💼 ENTERPRISE BLUEPRINT EXAMPLES
# =====================================================================
#
# 👉 DECORATOR APPROACH (Clean & Standard):
#
# @retry(
#     retry=retry_if_exception_type(TimeoutError),
#     stop=stop_after_attempt(3),
#     wait=wait_exponential(multiplier=1, min=2, max=8),
#     before_sleep=my_logger_hook
# )
# def fetch_data():
#     # Volatile API call goes here
#     pass
#
# =====================================================================
# 👉 INLINE RUNTIME APPROACH (The Pro Context Trick):
#
# for attempt in Retrying(stop=stop_after_attempt(3), wait=wait_fixed(1)):
#     with attempt:
#         # Sandboxed block of legacy code executed dynamically
#         pass
#
# =====================================================================
# 🧙‍♂️ THE MAGIC SPELL SUMMARY:
# "Decorate your boundaries, back off exponentially, and fail with a loud log."
