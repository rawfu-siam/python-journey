'''
Chapter2, topic - what is an API — REST vs GraphQL
'''
# =====================================================================
# 🧠 CORE DEFINITIONS
# =====================================================================
# API      -> A digital bridge letting two apps talk and share data.
# Endpoint -> A specific web URL path where code goes to fetch/send data.
# Schema   -> The server's rulebook defining allowed data shapes & types.

# =====================================================================
# 🏢 REST VS. GRAPHQL FACE-OFF
# =====================================================================
# 📬 REST:
#   - Uses MULTIPLE specific URL paths (e.g., `/users`, `/posts`).
#   - Uses standard HTTP verbs (`GET` to read, `POST` to create) [Chapter 2].
#   - Server decides the package. Causes Over-fetching (gets useless data).
#
# 🛍️ GRAPHQL:
#   - Uses ONE single URL path for everything (e.g., `/graphql`).
#   - Requests are sent inside an HTTP `POST` data payload [Chapter 2].
#   - Client query specifies exactly what fields it wants. Saves server costs.
