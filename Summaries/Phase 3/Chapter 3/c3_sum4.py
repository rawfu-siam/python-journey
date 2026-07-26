'''
Chapter3, topic - Selenium — scraping JavaScript-rendered pages
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# Selenium   -> A powerful automation framework that controls a real browser.
# JavaScript -> Language used by modern sites to load data dynamically.
# WebDriver  -> The robotic translator engine connecting Python to Chrome.
# Headless   -> Running the browser invisibly in memory without a GUI screen.

# =====================================================================
# 🎯 CORE LOGIC-BUILDING RULES
# =====================================================================
# 1. Never use time.sleep() -> It is slow, unpredictable, and inefficient.
# 2. Use Explicit Waits     -> Pauses script until the element exists/is visible.
# 3. Always driver.quit()   -> Closes the browser sessions to save system RAM.
# 4. Use robust locators     -> Prioritize By.ID or clean CSS over fragile layouts.

# =====================================================================
# 🏢 AGENCY-GRADE CONFIGURATION TEMPLATE
# =====================================================================
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# 
# options = Options()
# options.add_argument("--headless=new")  # Invisible mode for cloud servers
# options.add_argument("--user-agent=RealisticUserAgentStringHere")
# 
# driver = webdriver.Chrome(options=options)
# driver.get("https://your-target-website.com")
# ... processing steps ...
# driver.quit()
