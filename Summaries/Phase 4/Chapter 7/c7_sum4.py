'''
Chapter7, topic - user authentication for AI apps — JWT
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & JWT OVERVIEW
# =====================================================================
# JWT        -> JSON Web Token, a secure digital pass issued after login.
# TokenUrl   -> The endpoint path where users trade passwords for a wristband.
# Depends    -> FastAPI security helper to verify tokens on protected routes.
# Bearer     -> Authentication scheme where token is presented by the client.

# =====================================================================
# 🎫 THE 4-PART AUTHENTICATION PIPELINE
# =====================================================================
# 1. Login Route   -> Validates credentials and returns a signed JWT pass.
# 2. Payload Data  -> Contains user identity ('sub') and expiration time ('exp').
# 3. Dependency    -> FastAPI helper checking tokens on routes like https://api.agency.com/secure-ai.
# 4. Error Guard   -> Blocks unauthorized users with a 401 response if invalid.

# =====================================================================
# 🛡️ PRODUCTION GUARDRAILS & SENIOR SECRETS
# =====================================================================
# - Hide secrets: Load SECRET_KEY from environment variables, never hardcode.
# - Set short life: Always include expiration times (exp) to limit token theft window.
# - Use secure cookies: Store tokens in HttpOnly cookies to block XSS attacks.
# - Add refresh tokens: Pair short access tokens with secure database refresh tokens.
# - Validate scope: Ensure users only access resources they are authorized to see.