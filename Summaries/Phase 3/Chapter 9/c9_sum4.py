'''
Chapter9, topic - unit testing — pytest basics
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & NAMING RULES
# =====================================================================
# Unit Testing -> Writing small helper scripts to verify single functions.
# pytest       -> A production-grade framework to auto-run test suites.
# assert       -> The core keyword. Evaluates True (Pass 🟢) or False (Fail 🔴).
# 
# 📋 STRICT FILENAME LAWS:
#   - Files MUST look like -> test_app.py   OR   app_test.py
#   - Functions MUST look like -> def test_my_logic():
#   - Directories -> Neatly grouped inside a root /tests/ folder.

# =====================================================================
# 🏗️ THE AAA PATTERN (THE SENIOR DEVELOPER WAY)
# =====================================================================
# Every professional unit test follows three clean execution steps:
#
# 1. ARRANGE -> Set up the static variables, inputs, and mock states.
# 2. ACT     -> Execute the actual targeted function being tested.
# 3. ASSERT  -> Evaluate results using crisp comparison operators.
#
# Example Pattern:
# def test_addition():
#     # Arrange
#     num1, num2 = 10, 20
#     
#     # Act
#     total = add_numbers(num1, num2)
#     
#     # Assert
#     assert total == 30

# =====================================================================
# 🎬 THE SPEED-RUNNING TERMINAL CHEATSHEET
# =====================================================================
# Run all tests standard:        -> pytest
# Run with names verbose:        -> pytest -v
# Exit instantly on first FAIL:  -> pytest -x
# Run ONLY last failed cases:   -> pytest --lf
# Target specific file only:     -> pytest tests/test_payment.py

# =====================================================================
# ⚠️ AGENCY GUARDRAILS & COMMON PITFALLS
# =====================================================================
# ❌ NEVER use raw print() inside a test case to review outcomes manually.
# ❌ NEVER make live internet API calls inside local pure unit tests.
# 🧠 ALWAYS confirm your virtual env (venv) is active before running pytest.
