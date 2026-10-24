'''
Chapter7, topic - streaming AI responses to frontend
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & STREAMING OVERVIEW
# =====================================================================
# Streaming    -> Sending AI text word-by-word to the browser in real-time.
# Async Gen    -> A Python function that pauses and yields small data pieces.
# StreamingRes -> FastAPI tool that keeps browser connections open for data.

# =====================================================================
# 🌊 THE 3-PART STREAMING PIPELINE
# =====================================================================
# 1. Async Generator -> Uses async def and yield to pass tiny text chunks.
# 2. FastAPI Server  -> Uses StreamingResponse with a text/plain or SSE format.
# 3. Browser Reader  -> JavaScript fetch API using a TextDecoder to print live.

# =====================================================================
# 🛡️ PRODUCTION GUARDRAILS & SENIOR SECRETS
# =====================================================================
# - Enable LLM stream: Always set streaming=True in your OpenAI model config.
# - Use async routes: Always use async def to prevent server blocking.
# - Handle closures: Stop generating if the user closes their browser tab.
# - Use SSE standards: Upgrade to Server-Sent Events for robust production.