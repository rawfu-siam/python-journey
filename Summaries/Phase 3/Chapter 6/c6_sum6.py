'''
Chapter6, topic - response models and status codes
'''
# =====================================================================
# 🛡️ 1. CORE DEFINITIONS
# =====================================================================
# Response Model -> A Pydantic data filter blueprint linked to an endpoint.
#                   It automatically strips out private/sensitive fields 
#                   (e.g., passwords, internal budgets) before transmission.
#
# Status Code    -> A universal 3-digit number attached to a server response.
#                   It acts as a machine-readable flag telling frontends and
#                   no-code tools (n8n/Make) exactly how the request went.

# =====================================================================
# 🚥 2. THE GLOBAL STATUS CODE RULEBOOK
# =====================================================================
# 🟢 2xx FAMILY: SUCCESS CODES
#   - 200 OK      -> The request worked flawlessly. Here is your data.
#   - 201 Created -> Data was successfully committed/written to the DB.
#
# 🟡 4xx FAMILY: CLIENT-SIDE ERROR CODES (User mistakes)
#   - 400 Bad Request  -> The incoming payload data is broken or malformed.
#   - 401 Unauthorized -> Invalid or missing API tokens/authentication keys.
#   - 404 Not Found    -> The requested item/ID does not exist anywhere.
#
# 🔴 5xx FAMILY: SERVER-SIDE ERROR CODES (Code explosions)
#   - 500 Internal Error -> Your Python script crashed or hit an unhandled traceback.

# =====================================================================
# 💻 3. PRODUCTION IMPLEMENTATION PATTERNS
# =====================================================================
# To use these patterns in production, remember to:
#   1. Define an outbound schema inheriting from pydantic.BaseModel
#   2. Bind it via the decorator using: @app.route(response_model=Schema)
#   3. Explicitly pass success statuses using: status_code=status.HTTP_201_CREATED
#   4. Use 'raise HTTPException()' to halt bad requests early (Fail-Fast pattern)
#   5. Use 'response_model_exclude_unset=True' to strip out null/unused fields

# =====================================================================
# 🧪 4. SENIOR DEV CODE REVIEW CHECKLIST
# =====================================================================
# ✔️ NEVER return raw text error messages inside a sunny 200 OK status.
# ✔️ NEVER hardcode raw integer numbers (use 'from fastapi import status').
# ✔️ ALWAYS ensure returned dictionaries contain fields required by schemas.
# ✔️ ALWAYS build response models FIRST to map your API's public contract.
# =====================================================================
