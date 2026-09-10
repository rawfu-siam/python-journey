'''
Chapter6, topic - pytest framework installation and configuration
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & BASIC UNDERSTANDING
# =====================================================================
# pytest        -> A smart automated Python framework that checks code for bugs.
# Installation  -> Bringing the pytest library into a virtual environment via pip.
# Configuration -> Setting up global rulebooks using a dedicated configuration file.
# Assert        -> The built-in Python judge keyword used to verify if statements are True.

# =====================================================================
# 🎯 THE AGENCY-GRADE RULES & AUTOMATION DISCOVERY
# =====================================================================
# 🔍 File Naming Rule     : Test files must start with `test_` or end with `_test.py`.
# ⚙️ Function Naming Rule : Test functions must start exactly with `test_`.
# 📂 Workspace Layout     : Keep all validation scripts isolated inside a `tests/` directory.
# 🧪 Test Isolation       : Each test should be independent; avoid mixing shared global states.

# =====================================================================
# ⚙️ THE CONTROL TOWER SETUP (`pytest.ini`)
# =====================================================================
# Place a file named exactly `pytest.ini` in the project root directory:
#
# [pytest]
# addopts = -v --tb=short
# testpaths = tests
#
# * `addopts = -v`   -> Activates Verbose mode for detailed terminal notes.
# * `--tb=short`     -> Trims massive stack traces down to small, readable bug alerts.
# * `testpaths = tests` -> Expressly points pytest to search inside the `tests/` folder.

# =====================================================================
# 🎬 THE BACKSTAGE PASS: PROFESSIONAL TERMINAL SHORTCUTS
# =====================================================================
# ⚡ `pytest -x`   -> Stop at First Blood: Halts the test suite instantly on the first error.
# 🎯 `pytest --lf` -> Last Failed Sniper: Skips passing tests; runs only previously failed ones.
# 🧙‍♂️ Magic Spell   -> "If it isn't tested automatically, it is broken implicitly."
