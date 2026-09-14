'''
Chapter6, topic - Firing single-command integration tests (pytest -v)
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & TERMINOLOGY
# =====================================================================
# Unit Test        -> Testing a single line or isolated function (e.g., math helper).
# Integration Test -> Testing how multiple components work together as a team.
# pytest           -> Python's industry-standard automated test engine runner framework.
# -v Flag          -> "Verbose" mode. Tells pytest to output detailed, chatty results.

# =====================================================================
# 📂 THE DETECTIVE NAMING RULES (STRICT CRITERIA)
# =====================================================================
# 1. File Names     -> Must start with `test_` or end with `_test.py`.
# 2. Function Names -> Must start explicitly with `test_` (e.g., def test_api()).
# ⚠️ Failure to follow these prefixes means pytest will completely ignore your file.

# =====================================================================
# 🛡️ THE ENTERPRISE AUTOMATION GUARDRAILS
# =====================================================================
# TestClient -> Provided by FastAPI to mimic web interactions at zero network cost.
# assert     -> The programmatic judge. Determines if conditions are True or False.
# mock.patch -> Intercepts expensive live web calls (like OpenAI) for free testing.

# =====================================================================
# 🎬 THE SENIOR DEV CHEAT SHEET (TERMINAL TRICKS)
# =====================================================================
# `pytest -v`           -> Fires the entire test directory with full verbose logging.
# `pytest -v -k "auth"` -> Runs ONLY the specific test cases matching the word "auth".
# 🧙‍♂️ Golden Rule        -> "If it isn't verified by an assert, it is broken live."
