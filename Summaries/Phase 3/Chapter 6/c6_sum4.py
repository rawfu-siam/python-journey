'''
Chapter6, topic - path parameters and query parameters
'''
# =====================================================================
# 🧠 FASTAPI PARAMETERS RULEBOOK
# =====================================================================
# Path Parameter  -> Mandatory variable baked directly inside the URL path.
#                    Used to identify a unique target resource.
# Query Parameter -> Optional modifier attached to the end of a URL after '?'.
#                    Used to sort, filter, or paginate data collections.
#
# =====================================================================
# 🛣️ SYNTAX BREAKDOWN & RULES
# =====================================================================
# 🎛️ PATH PARAMETER RULES:
#   - Declared using curly braces in route: `@app.get("/items/{item_id}")`
#   - Variable names must match function arguments exactly.
#   - Example: `http://127.0.0/items/500` -> Fetches unique item #500.
#
# 🔎 QUERY PARAMETER RULES:
#   - NEVER written inside the `@app` path decorator string.
#   - Declared strictly inside the function argument parameters.
#   - Example: `http://127.0.0?limit=5` -> Filters view to 5 items.
#
# =====================================================================
# 🇦🇺🇸🇬 AGENCY PRO-TIPS FOR PRODUCTION ENVIRONMENT
# =====================================================================
# 🛡️ Sane Defaults: Always set default limits to prevent system overloads.
# 🔒 Zero-Trust: Never put private tokens or secrets inside visible URLs.
# 🧪 Guardrails: Enforce explicit type hints (`int`, `str`) for auto-validation.
