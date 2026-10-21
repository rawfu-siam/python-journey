'''
Chapter3, topic - web search tool — Tavily, SerpAPI
'''
# =====================================================================
# 🧠 CORE DEFINITIONS: WEB SEARCH TOOLS
# =====================================================================
# Web Search Tools -> Software bridges that give LLMs real-time web access.
# SerpAPI          -> Scrapes raw search engine SERP data (links, snippets).
# Tavily           -> AI-native search engine; extracts and cleans raw text.

# =====================================================================
# 🛠️ CHANNELS & PARA PARAMETERS 
# =====================================================================
# max_results      -> Guardrail parameter restricting search context size.
# max_iterations   -> Agent loop cap preventing infinite cost bleeding.
# .env isolation   -> Zero-trust hygiene pattern hiding API tokens.

# =====================================================================
# 🏢 AGENCY WORKSPACE DISPATCH: TAVILY VS. SERPAPI
# =====================================================================
# 📝 USE TAVILY WHEN:
#   - Building content agencies, research assistants, or summary pipelines.
#   - Your LLM needs clean, unstructured text without menu/ad noise.
#
# 📊 USE SERPAPI WHEN:
#   - Building market intelligence, SEO tracking, or lead generation bots.
#   - Your script needs to analyze ranking order positions or map reviews.

# =====================================================================
# 🛡️ PRODUCTION CHECKLIST FOR JUNIOR DEVS
# =====================================================================
# 1. Keep max_results low (2-3) to save token cost and speed up response.
# 2. Never hardcode keys; use os.environ.get() paired with python-dotenv.
# 3. Restrict agent loops using max_iterations parameters inside wrappers.
# 4. Integrate Tenacity retry decorators to survive temporary API downtime.
