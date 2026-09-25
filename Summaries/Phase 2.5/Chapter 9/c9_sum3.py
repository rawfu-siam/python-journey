'''
Chapter9, topic - Bandit analyzer — running AST (Abstract Syntax Tree) scans 
                  to catch codebase injection flaws and loose dependencies
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# Bandit     -> An automated security static analyzer for Python code.
# AST Scan   -> Abstract Syntax Tree; reads structural meanings of code, 
#               not just flat text strings, ensuring precise analysis.
# Injection  -> A flaw where unsafe inputs trick the shell into running 
#               harmful system commands (e.g., executing raw strings).
# Loose Deps -> Outdated or insecure packages imported into the codebase.
#
# =====================================================================
# 📊 SEVERITY & CONFIDENCE SCALES
# =====================================================================
# Severity   -> Risk level of the flaw: High 🔴 | Medium 🟡 | Low 🟢
# Confidence -> Bandit's certainty level: High 🎯 | Medium/Low ⚖️
#
# =====================================================================
# 🛡️ THE ELITE SECURITY PLUGIN MATRICES
# =====================================================================
# ❌ B101    -> Assert statement used (Tragic! Disappears in production 
#               when run under optimized '-O' runtime flags).
# 🔑 B105    -> Hardcoded password/API key found inside a raw string variable.
# 💉 B605    -> Unsafe shell execution detected (e.g., raw os.system loops).
# 🕸️ B301    -> Insecure data unpacking using vulnerable modules like 'pickle'.
#
# =====================================================================
# 🚀 THE LAZY PRO ENTERPRISE GUARDRAILS
# =====================================================================
# # nosec    -> Inline comment bypass. Slapped on true false-positives only.
#               Pro tip: Always use specific IDs like '# nosec B101'.
# Exclusions -> Flag custom code paths only to skip virtual folders:
#               `bandit -r src/ --exclude .venv`
# Dev Hack   -> Never test manually! Bind Bandit to your local Pre-Commit 
#               hooks and execute AST checks inside GitHub Actions CI/CD.
#
# =====================================================================
# 🪄 THE AGENCY CATCHPHRASE MAGIC SPELL
# =====================================================================
# "Never trust user input, never spawn a raw shell, and let the AST 
# guard your pipeline!"
