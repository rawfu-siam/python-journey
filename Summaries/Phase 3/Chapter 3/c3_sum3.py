'''
Chapter3, topic - CSS selectors and HTML navigation
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & PRINCIPLES
# =====================================================================
# HTML Navigation -> Moving along the family tree (Parents, Children, Siblings).
#                   Best used when items lack clear, unique class names.
# CSS Selectors   -> Universal targeting strings acting like search lasers.
#                   Best used to jump directly to labels across any depth.
#
# Rule of Dot/Hash -> Use a dot (.) for classes:    soup.select(".item")
#                  -> Use a hash (#) for IDs:       soup.select_one("#main")

# =====================================================================
# 🥊 SELECTOR FACE-OFF: FIND VS. SELECT
# =====================================================================
# THE OLD WAY (find / find_all):
#   - Clunky Python-specific arguments: soup.find("p", class_="title")
#   - Harder to nest multi-level paths cleanly in a single method call.
#
# THE PRO WAY (select / select_one) -> ALWAYS DEFAULT TO THIS:
#   - Standard CSS syntax used by browsers: soup.select_one("p.title")
#   - Ultra-flexible paths. Space means inside: soup.select(".card h2")

# =====================================================================
# 🛡️ PRODUCTION GUARDRAILS (AGENCY-GRADE)
# =====================================================================
# 1. Clear List Traversal: Never call .text on a list variable. 
#    Always loop through the list returned by soup.select().
#
# 2. Defensive Safeguards: Verify an element exists before calling .text
#    to keep a slight website change from crashing your background worker.
#
# 3. User-Agent Spoofing: Disguise your scraper as a real browser header
#    to protect against instant IP blocks and firewall bans.
#
# 4. Human-like Rate Limits: Always drop a random time.sleep() delay 
#    inside scraping loops to gather enterprise data ethically.
