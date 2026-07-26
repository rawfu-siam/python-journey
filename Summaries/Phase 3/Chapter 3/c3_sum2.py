'''
Chapter3, topic - requests + BeautifulSoup workflow
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & WORKFLOW BLUEPRINT
# =====================================================================
# Workflow    -> A 2-step team pipeline used to collect web data automatically.
# requests    -> The Fetcher. Contacts the web server and pulls raw HTML.
# bs4 (Soup)  -> The Organizer. Turns messy HTML strings into a searchable tree.
#
# PIPELINE ARCHITECTURE STEPS:
# 1. Target URL Definition -> Specify where your automation script goes.
# 2. Network Ping          -> Fire requests.get(url) with a browser User-Agent.
# 3. Status Validation     -> Verify response.status_code == 200 before parsing.
# 4. Soup Initialization   -> Feed response.text into BeautifulSoup(txt, parser).
# 5. Target Extraction     -> Search via selectors and peel out clean text data.

# =====================================================================
# 🛠️ ELEMENT SEARCH METHOD COMPARISON
# =====================================================================
# 🔍 .find() METHOD:
#   - Purpose: Scopes the first single occurrence of a specific HTML tag.
#   - Returns: A single Element object if found, or None if missing.
#   - Usage: Best for unique items like page headings or metadata blocks.
#
# 📊 .find_all() METHOD:
#   - Purpose: Scrapes every single matching occurrence across the entire DOM.
#   - Returns: A standard Python list containing multiple Element objects.
#   - Usage: Best for multi-target grids like product tables or job lists.

# =====================================================================
# 🛡️ ENTERPRISE DEFUSE CODES & LANDMINES
# =====================================================================
# 💣 Landmine: AttributeError: 'NoneType' object has no attribute 'text'
#   - Cause: Trying to extract text from a tag that does not exist on the page.
#   - Fix: Always isolate the tag first, check if tag exists, then extract .text.
#
# 💣 Landmine: Immediate Bot Detection Blocking (403 Forbidden)
#   - Cause: Sending scripts out with Python's default identifier strings.
#   - Fix: Pass a custom browser user-agent inside headers={...} dictionary.
#
# 💣 Landmine: Network Latency Overhead on Multi-page Scraping Loop
#   - Cause: Creating a new handshake socket connection on every single page loop.
#   - Fix: Initialize requests.Session() to persist the active socket pipe.
