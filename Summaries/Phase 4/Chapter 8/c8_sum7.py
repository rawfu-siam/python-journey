'''
Chapter8, topic - Streaming states — monitoring token chunks and node transitions live
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & CONCEPTS
# =====================================================================
# Streaming States   -> Watching AI execution and data updates in real time.
# Token Chunks       -> Words or pieces of text appearing one by one.
# Node Transitions   -> Tracking which agent step is currently executing.
# Generator Function -> Yielding data pieces dynamically without waiting.

# =====================================================================
# 🏗️ ARCHITECTURE PATTERNS & SETUP
# =====================================================================
# .stream()          -> Replaces .invoke() to return a live execution stream.
# stream_mode        -> Parameter choosing between updates, values, or custom.
# Frontend SSE       -> Server-Sent Events pushing Python streams to web UI.
# Endpoint Routing   -> Streaming routes hosted at `https://api.myagency.com/stream`.

# =====================================================================
# 🚀 AGENCY BEST PRACTICES & PRODUCTION TIPS
# =====================================================================
# Avoid Invoke       -> Never use blocking invoke methods for user-facing UIs.
# Progress Bars      -> Use update streams to show active agent steps on dashboards.
# Token Streaming    -> Use LLM-level chunks for realistic chat typing effects.
# Error Handling     -> Ensure stream generators catch exceptions mid-flight.