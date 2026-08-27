'''
Chapter3, topic - python-dotenv library — loading keys via load_dotenv()
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# python-dotenv -> External library that hides secret keys inside a text file.
# .env file     -> Hidden config file named exactly '.env' using KEY="value".
# load_dotenv() -> Magic spell injecting keys from .env into background memory.
# os.environ    -> Python's system memory dictionary holding active variables.
# os.environ.get-> Safe extraction claw pulling values into active code variables.

# =====================================================================
# 🎯 REAL-WORLD AGENCY COMPLIANCE & SAFETY WORKFLOWS
# =====================================================================
# 🛑 The Git Rule     -> Add '.env' to '.gitignore' so secrets never leak [Chapter 3].
# 📋 The Team Template -> Share a clean '.env.example' showing required key names [Chapter 3].
# 🧨 Fail-Early Policy -> Check keys on line 1; crash loudly if keys are missing [Chapter 3].
# 🔧 Fallback Handling -> Use os.environ.get("PORT", "80") only for non-secret defaults [Chapter 3].

# =====================================================================
# 🛠️ QUICK SYNTAX REFERENCE CHEAT SHEET
# =====================================================================
# Installation command : pip install python-dotenv
# Core Python Import   : from dotenv import load_dotenv
# Terminal Shortcut    : python -m dotenv run python script.py [Chapter 7]
# Perfect .env Entry   : CRITICAL_API_KEY="sk-12345" (No spaces around '=') [Chapter 6]
