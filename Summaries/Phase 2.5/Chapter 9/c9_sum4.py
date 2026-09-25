'''
Chapter9, topic - Automated Pre-Commit hooks — constructing a local 
                  .pre-commit-config.yaml matrix to block broken or unvetted git commits
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# Pre-Commit Hook  -> An automatic safety guard script running right before 
#                     a 'git commit' execution saves your code.
# YAML Config File -> Named `.pre-commit-config.yaml`. The local matrix or 
#                     rulebook listing tools to check code.
# The Local Hook   -> Resides inside `.git/hooks/pre-commit` after you run 
#                     the initialization engine tool.
#
# =====================================================================
# 🛡️ THE THREE CRITICAL PIECES
# =====================================================================
# 1. The Manager   -> Installed via terminal: `pip install pre-commit`
# 2. The Activator -> Hooked into Git via: `pre-commit install`
# 3. The Execution -> Happens automatically upon running `git commit`
#
# =====================================================================
# 🎬 THE SENIOR DEVELOPER PRO CHEATS
# =====================================================================
# `pre-commit run --all-files` -> Scans the entire codebase instantly 
#                                 without needing a mock commit.
# `pre-commit autoupdate`      -> Automatically bumps all rule hook 
#                                 versions to their latest releases.
# `--no-verify`                -> Appended to git commit to bypass hooks 
#                                 during production emergencies ONLY.
#
# =====================================================================
# 🧠 AGENCY MINDSET GOLDEN RULE
# =====================================================================
# "If it isn't automated locally, it will definitely crash globally."