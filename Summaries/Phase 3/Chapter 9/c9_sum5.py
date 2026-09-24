'''
Chapter9, topic - writing a requirements.txt and setup.py
'''
# =====================================================================
# 🧠 CORE CONFIGURATION DEFINITIONS
# =====================================================================
# requirements.txt -> A flat text shopping list of third-party packages.
# setup.py         -> A Python build script making your tool installable.
# install_requires -> The setup.py parameter listing absolute dependencies.
#
# =====================================================================
# 🛒 REQUIREMENTS.TXT VS. SETUP.PY FACE-OFF
# =====================================================================
# 📄 REQUIREMENTS.TXT:
#   - Context: Used for deploying apps, web services, and scripts.
#   - Engine: Executed using `pip install -r requirements.txt`.
#   - Best Practice: Use exact bounds (`==`) to freeze production logic.
#
# 🐍 SETUP.PY:
#   - Context: Used for libraries, internal modules, and frameworks.
#   - Engine: Executed using `pip install .` or bundled for distribution.
#   - Best Practice: Read your `README.md` file dynamically using pathlib.
#
# =====================================================================
# ⚠️ AGENCY GUARDRAILS & LAUNCH TRAPS
# =====================================================================
#   - Global Pollution: Never run freeze commands without an active venv.
#   - Loose Versions: Avoid `>=` in production; updates break code.
#   - Git Leaks: Ensure build/ and *.egg-info/ are trapped inside .gitignore.
#   - Enterprise Tip: Use `uv` package engine to run lightning installs.
