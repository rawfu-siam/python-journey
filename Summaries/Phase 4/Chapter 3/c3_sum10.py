'''
Chapter3, topic - LangSmith — debugging and monitoring agents
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & LANGSMITH AUDITING MECHANICS
# =====================================================================
# LangSmith -> A cloud dashboard that acts like an X-ray engine for AI.
# Trace      -> A holistic flight log capturing a complete pipeline execution.
# Run/Span   -> A specific parent-child sub-step task nested inside a trace.
# Metadata   -> Dynamic data tags (Client ID, Run ID) added to filter trace feeds.

# =====================================================================
# 🛠️ ENV SYSTEM ACTIVATION MATRIX
# =====================================================================
# `LANGCHAIN_TRACING_V2=true` -> Tells Python to automatically stream telemetry.
# `LANGCHAIN_PROJECT="..."`    -> Routes traces into separate room environments.
# `LANGCHAIN_API_KEY="..."`    -> Secure credential key that authenticates logs.

# =====================================================================
# 🏢 AGENCY PRODUCTION GUARDRAILS
# =====================================================================
# 🔒 Zero Hardcoding -> Isolate keys inside a hidden `.env` profile setup.
# ✂️ Sampling Control -> Mute logs on millions of cheap scraper loops to save costs.
# 👥 Client Portals  -> Grant read-only access to custom workspaces for transparency.
# 🧪 Failure Tuning  -> Clip failing prompt histories into test suites for optimization.
