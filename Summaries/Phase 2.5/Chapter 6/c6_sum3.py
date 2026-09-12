'''
Chapter6, topic - Testing FastAPI endpoints using TestClient
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# TestClient  -> A virtual browser simulator provided by FastAPI.
#               It lets you hit endpoints without launching a real server.
# Assert      -> Python's built-in referee keyword used to cross-examine
#               returned statuses or JSON outputs against expectations.
# Pytest      -> The automated test runner that sweeps files looking for
#               prefixed functions to execute validation checks.
#
# =====================================================================
# 🚀 THE FASTAPI TESTCLIENT DANCE FLOW
# =====================================================================
# Step 1: Write an endpoint inside your app file (e.g., app/main.py).
# Step 2: Create an isolated test file prefixed with 'test_' (e.g., test_main.py).
# Step 3: Initialize the mock engine: `client = TestClient(app)`.
# Step 4: Fire simulation requests: `response = client.get("/route")`.
# Step 5: Assert execution status: `assert response.status_code == 200`.
# Step 6: Validate output structures: `assert response.json() == {"data": "ok"}`.
#
# =====================================================================
# ⚠️ AGENCY GUARDRAILS & COMMON PITFALLS
# =====================================================================
# 🔍 File Naming Rules  -> Scripts MUST be named `test_*.py` or `*_test.py`.
# 🔍 Function Naming   -> Test functions MUST start with the prefix `test_`.
# 🚫 No Uvicorn Spawn   -> Never run a manual local server while running tests.
# 🚫 Type Matching      -> `response.json()` returns a Dictionary, not a String!
# 🔒 Database Isolation -> Never point TestClient simulations at production data;
#                         always intercept requests using temporary test databases.
#
# =====================================================================
# 🪄 THE ONE-LINE PRO MAGIC SPELL
# =====================================================================
# "Mock the request, freeze the server, assert the JSON."
# =====================================================================
