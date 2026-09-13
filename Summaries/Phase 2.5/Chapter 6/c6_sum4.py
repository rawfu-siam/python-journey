'''
Chapter6, topic - Mocking external components — unittest.mock and patch
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# Mocking  -> Creating a safe, harmless "stunt double" of a code component.
# Patching -> Unplugging a real component and plugging in a fake Mock.
# Why it matters in an Agency -> Saves API costs, accelerates test suites,
#                               and prevents destructive production accidents.
#
# THE MAGIC SPELL: "Mock where it's looked up, not where it's defined."

# =====================================================================
# 🧩 CORE MECHANICS (unittest.mock)
# =====================================================================
# 🤖 Mock Object:
#   - A shape-shifting robot clone that captures and records interaction history.
#   - Tracks execution states: `.called`, `.call_count`, and exact input args.
#
# 🩹 @patch Decorator / with patch() Context Manager:
#   - Dynamically hijacks a namespace string path for the duration of a test.
#   - Automatically restores original system wiring once execution finishes.
#
# 💰 return_value:
#   - Forces a mock to instantly return a clean, static, successful data shape.
#
# 💥 side_effect:
#   - Triggers dynamic logic, variations, or injects crashes (e.g., ConnectionError).

# =====================================================================
# ⚠️ COMMON MISTAKES & ADVANCED TRICKS
# =====================================================================
# ❌ The Wrong House Trap: Patching the origin path instead of the usage path.
#   - Fix: Target where the script imports and uses the target module.
# 🕵️ Typo Risks: Strings are not auto-completed; always double-check paths manually.
# 🚀 The Pro Shortcut (autospec=True):
#   - Dynamically copies the exact method and argument structure of real code.
#   - Explodes instantly if your app passes non-existent arguments to the mock.
