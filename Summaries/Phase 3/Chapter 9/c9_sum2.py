'''
Chapter9, topic - folder structure for professional Python projects
'''
# =====================================================================
# 🧠 PROFESSIONAL FOLDER STRUCTURE & ARCHITECTURE BLUEPRINT
# =====================================================================
# Goal: Organize code logically so any dev can instantly navigate it.
# Standard: The "src/" container layout is the global agency gold standard.
#
# Project Directory Concept Visualizer:
# my_agency_project/
#  ├── .gitignore          -> Secret agent shielding .env from GitHub.
#  ├── .env.example        -> Public template showing required API keys.
#  ├── pyproject.toml      -> Modern blueprint containing project packages.
#  ├── README.md           -> Onboarding guide for clients and recruiters.
#  └── src/                -> The clean container where ALL running code lives.
#       ├── __init__.py    -> Empty file making folder importable as a package.
#       ├── config.py      -> Safe config center reading keys securely.
#       └── main.py        -> Captain of the ship. The main script entrypoint.

# =====================================================================
# 🎯 WHY IT MATTERS FOR US AI AUTOMATION AGENCIES
# =====================================================================
# 🤝 Scalability: Allows multiple devs to build features without conflicts.
# 🛡️ Maintenance: Isolates bugs to single files; prevents accidental deletes.
# 🤖 CI/CD Ready: Cloud servers can easily find tests and execution paths.

# =====================================================================
# ⚠️ SENIOR DEV SANITY RULES (COMMON MISTAKES TO AVOID)
# =====================================================================
# 1. NEVER commit a live '.env' file. Initialize '.gitignore' on day one!
# 2. Never use flat roots. Keep loose root files to an absolute minimum.
# 3. Avoid hardcoded machine paths. Always use portable dynamic paths.
# 4. Separate code from output. Drop scraped data into a clear 'data/' folder.
