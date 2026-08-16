'''
Chapter6, topic - creating routes — GET, POST, PUT, DELETE
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# Route/Endpoint -> A specific URL path location that listens for data.
# HTTP Verb      -> A standardized operation command (GET, POST, etc.).
# CRUD           -> Create, Read, Update, Delete (The core of all app data).
# Decorator      -> The @app syntax linking a web path to a Python function.

# =====================================================================
# 🔤 THE 4 INTERNET ACTION VERBS
# =====================================================================
# 📖 GET    -> Reads or retrieves information. Safe to run in regular browser.
# 🆕 POST   -> Pushes new data to create a record. Not safe to repeat blindly.
# 🔄 PUT    -> Modifies/overwrites existing records at a specified pointer.
# 🗑️ DELETE -> Purges or completely destroys records from the backend system.

# =====================================================================
# 🛠️ PRODUCTION INTERVIEW STANDARDS (AU/SG STYLE)
# =====================================================================
# 1. Clean URLs -> Focus paths on plural nouns instead of descriptive actions:
#    - GOOD: @app.get("/leads")   |  BAD: @app.get("/get-all-agency-leads")
# 2. Testing    -> Never test POST/PUT/DELETE from browser URL bar. Use `/docs`.
# 3. Handling   -> Keep route functions light; pass data to separate scripts.
