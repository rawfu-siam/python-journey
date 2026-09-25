'''
Chapter9, topic - project versioning — semantic versioning
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# Project Versioning   -> Giving code a standard label to track changes.
# Semantic Versioning  -> A strict 3-number system indicating code safety.
# The SemVer Contract  -> Tells developers if updates will run safely or crash.
#
# Format Structure     -> MAJOR.MINOR.PATCH  (Example: 2.5.1)

# =====================================================================
# 🛠️ THE THREE NUMBER BLOCKS BREAKDOWN
# =====================================================================
# 🚨 1. MAJOR Version (First Digit: 2.x.x)
#   - Increment when: Making breaking modifications or changing schemas.
#   - Compatibility: Backward-incompatible (Old systems will crash).
#   - Action rule   : Increments the digit and resets MINOR and PATCH to 0.
#
# 🚀 2. MINOR Version (Second Digit: x.5.x)
#   - Increment when: Safely introducing clean, new features or utilities.
#   - Compatibility: Backward-compatible (Old code runs perfectly fine).
#   - Action rule   : Increments the digit and resets the PATCH version to 0.
#
# 🩹 3. PATCH Version (Third Digit: x.x.1)
#   - Increment when: Shipping hotfixes, refactoring style, or fixing typos.
#   - Compatibility: Backward-compatible (Zero functional impact on users).
#   - Action rule   : Increments the third digit smoothly without resets.

# =====================================================================
# 🧪 SENIOR DEV AGENCY GUARDRAILS
# =====================================================================
# 🐣 Unstable Beta Stage -> Keep project at 0.y.z until ready for production.
# 🔟 Double-Digit Rule   -> Numbers are not decimals! 1.10.2 is valid after 1.9.9.
# 🏷️ Git Tagging Anchor  -> Lock releases into terminal logs using: `git tag v1.0.0`
# 🪄 The Magic Catchphrase -> "Fix a scratch with a PATCH, grow features with a 
#                             MINOR, but clear the board for a MAJOR."
