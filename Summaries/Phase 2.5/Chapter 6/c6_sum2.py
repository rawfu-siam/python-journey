'''
Chapter6, topic - Writing assertive test cases — test_* naming conventions
'''
# =====================================================================
# 🧠 TESTING FUNDAMENTALS & DEFINITIONS
# =====================================================================
# Test Case  -> A small function written to verify another function works.
# Assert     -> The 'assert' keyword confidently verifies a logic condition.
# Pytest     -> The framework that scans, runs, and monitors your tests.
# Exception  -> If an assert is False, Python raises an AssertionError.

# =====================================================================
# 📐 THE AAA STRUCTURE & NAMING CONVENTIONS
# =====================================================================
# 📁 FILE RULE:
#   - Your files MUST start with 'test_' (e.g., `test_scraper_utils.py`).
#
# ⚙️ FUNCTION RULE:
#   - Every test function MUST start with 'test_' (e.g., `test_clean_email()`).
#
# 🏗️ THE AAA PATTERN:
#   - Arrange : Set up your variables, mock inputs, and conditions.
#   - Act     : Fire the real target function and store its raw output.
#   - Assert  : Forcefully evaluate actual results vs. expected criteria.

# =====================================================================
# 🦥 LAZINESS IS A VIRTUE: ENTERPRISE MINDSET
# =====================================================================
# ⚡ Shortcut  -> Use `@pytest.mark.parametrize` to run loops inside 1 test.
# 🛡️ Principle -> Untested code is broken code in a live environment.
# 🪝 Strategy  -> Hook `pytest` to local git pre-commit to block buggy pushes.
# 📝 Formatting -> Always pass a descriptive failure message after a comma!
