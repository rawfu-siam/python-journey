'''
Chapter6, topic - dependency injection basics
'''
# =====================================================================
# 📚 CORE CORE DEFINITIONS
# ---------------------------------------------------------------------
# Dependency -> Any tool, configuration, or connection a function needs.
# Injection  -> The act of FastAPI supplying that tool automatically.
# Depends()  -> The bridge helper that hooks the supplier to the route.

# 🏢 REAL-WORLD BUSINESS VALUE
# ---------------------------------------------------------------------
# 🧼 Clean Code: Write setup logic ONCE, use it across 100+ endpoints.
# 💰 Cost Control: Stop unauthorized API requests BEFORE hitting GPT models.
# 🧪 Mock Testing: Easily swap live tools with dummy tools during test runs.

# ⚙️ EXTRAS & AGENCY BEST PRACTICES
# ---------------------------------------------------------------------
# ⛓️ Chaining: Dependencies can look up other dependencies seamlessly.
# ⚡ Caching: FastAPI caches identical request calls to optimize performance.
# 🚨 Global Guard: Protect massive API groups using router-level dependencies.
# ⚠️ No Parenthesis: Never call the function inside Depends -> Depends(func).
# ♻️ Resource Cleanup: Use "yield" to open tools and safely close them later.
# =====================================================================
