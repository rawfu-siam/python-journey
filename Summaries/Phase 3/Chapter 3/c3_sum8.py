'''
Chapter3, topic - ethical scraping — robots.txt
'''
# =====================================================================
# 🧠 ETHICAL SCRAPING & ROBOTS.TXT 
# =====================================================================
# Ethical Scraping -> Writing polite scripts that respect website limits.
# robots.txt       -> A public rules file found at a website's root folder.
# Location Rule    -> Must always live exactly at: `://domain.com`
#
# =====================================================================
# 📋 CORE ROBOTS.TXT SYNTAX FIELDS
# =====================================================================
# User-agent: *       -> Code block targeting ALL web scraper robots.
# Disallow: /admin/   -> Stay out! Do NOT scrape or access this directory path.
# Allow: /public/     -> Green light! Safe to scrape this specific path.
# Crawl-delay: 5      -> Speed limit! Wait 5 seconds between loading pages.
#
# =====================================================================
# ⚙️ PRODUCTION CODE ARCHITECTURE RULES
# =====================================================================
# 1. DYNAMIC URL PARSING:
#    - Never hardcode the robots.txt file web path string.
#    - Use `urllib.parse.urlparse` to extract `scheme` and `netloc`.
#    - This allows your script to work safely across any dynamic target URL.
#
# 2. RUNTIME MEMORY EFFICIENCY (CACHING):
#    - Read and download the robots.txt file ONCE at script initialization.
#    - Cache the rules structure object in memory during execution loops.
#    - Do NOT call `.read()` inside a loop for every single webpage link.
#
# 3. GATEKEEPER DESIGN PATTERN:
#    - Build a defensive function wrapping your HTTP requests (`requests.get`).
#    - Pass target links through `.can_fetch("*", target_url)` first.
#    - Instantly drop forbidden URLs before they hit the live network line.
#
# =====================================================================
# 🐨 AUSTRALIAN AGENCY COMPLIANCE BEST PRACTICES
# =====================================================================
# - Crashing local business servers causes severe operational liability issues.
# - Always add a fallback randomized delay if `Crawl-delay` is missing.
# - Customize the HTTP `User-Agent` string header professionally.
# - Avoid the default `python-requests` signature to prevent firewall blocks.
