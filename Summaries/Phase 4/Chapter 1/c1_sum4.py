'''
Chapter1, topic - temperature, max_tokens, top_p parameters
'''
# =====================================================================
# 🧠 CORE PARAMETER DEFINITIONS 
# =====================================================================
# temperature -> Controls AI randomness (0.0 = strict robot, 2.0 = wild poet).
# max_tokens  -> Sets a hard length ceiling on the output text (1 token ≈ 4 chars).
# top_p       -> Cumulative probability filter (nucleus sampling) for word pools.

# =====================================================================
# 🏢 REAL-WORLD BUSINESS CONFIGURATIONS
# =====================================================================
# 📊 DATA EXTRACTION & CODES (Strict Tasks):
#   - Set `temperature=0.0` or ultra-low values.
#   - Forces the AI to stick purely to facts and provided context.
#   - Keeps JSON data structures safe and perfectly intact.
#
# 🎨 MARKETING COPY & BRAINSTORMING (Creative Tasks):
#   - Set `temperature=0.0` to default (1.0) and use `top_p=0.90` or higher.
#   - Widens the choice pool to surface interesting and unique vocabulary.
#   - Discards completely irrelevant or broken vocabulary options.

# =====================================================================
# ⚠️ SENIOR ARCHITECT PRODUCTION GUARDRAILS
# =====================================================================
# 🚫 Rule 1: Never adjust BOTH temperature and top_p at the same time.
# 🚫 Rule 2: Never starve JSON tasks—always provide a buffer for closing tags.
# 🛑 Rule 3: max_tokens only cuts output costs. Input costs must be sliced early.
# 🛠️ Rule 4: Check `finish_reason == "length"` to catch truncated scripts.

# =====================================================================
# 🪄 THE AUTOMATION HACKERS MAGIC SPELL
# =====================================================================
# "Freeze the temperature for strict facts;
#  open the window of Top_P for marketing acts!"
# =====================================================================
