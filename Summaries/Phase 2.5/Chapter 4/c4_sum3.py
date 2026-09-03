'''
Chapter4, topic - Auto-generated documentation engines — Swagger UI (/docs)
                  and ReDoc (/redoc)
'''
# =====================================================================
# 🧠 FASTAPI AUTO-DOCUMENTATION HUB 
# =====================================================================
# 🧪 SWAGGER UI (`/docs`):
#   - Interactive sandbox layout for live manual engineering tests.
#   - Features a "Try it out" button to execute backend python routes.
#   - Ideal for rapid debugging, testing scripts, and system spot-checks.
#
# 📚 REDOC (`/redoc`):
#   - Clean, publication-grade three-pane technical document textbook.
#   - Built for developer handoff, codebase scaling, and structured reading.
#   - Read-only navigation interface with sidebar indexing structures.

# =====================================================================
# 🛠️ HOW THE ENGINE READS YOUR CODE
# =====================================================================
# 1. Title/Version -> Passed directly as main arguments inside FastAPI().
# 2. Description  -> Pulls from app initialization arguments or module-level strings.
# 3. Route Info   -> Extracted directly from function triple-quote docstrings (""").
# 4. Input Schema -> Built instantly from type-hints or referenced Pydantic models.
# 5. Organizers   -> Managed via `tags=["Category Name"]` decorators to group tools.

# =====================================================================
# 🚀 PRO-LEVEL EMBEDDED SHORTCUTS
# =====================================================================
# - `openapi.json`           -> The raw underlying schema map at `/openapi.json`.
# - `include_in_schema=False` -> Pass to a route decorator to hide it from docs.
# - `Field(example="...")`    -> Enforces predefined sample variables in UI forms.
# - `response_model=Model`    -> Forces Swagger/ReDoc to display clean output schemas.

# =====================================================================
# 🪄 THE AUTOMATION GOLDEN RULE
# =====================================================================
# "Your code is your documentation; if it looks beautiful on `/docs`, 
# it will run flawlessly in production."
# =====================================================================
