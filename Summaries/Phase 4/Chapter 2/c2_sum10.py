'''
Chapter2, topic - vector stores — ChromaDB, FAISS
'''
# =====================================================================
# 🧠 CORE VECTOR STORE DEFINITIONS
# =====================================================================
# Vector Store -> An AI database storing data meaning via lists of numbers.
# Embedding   -> A text snippet translated into mathematical coordinates.
# Chunking    -> Chopping big files into small blocks with semantic overlap.
# Distance    -> Math checks (like Cosine) to find matching document concepts.

# =====================================================================
# 🪵 CHROMADB VS. ⚡ FAISS CHEAT SHEET
# =====================================================================
# 🪵 CHROMADB:
#   - Best for fast, all-in-one RAG apps and swift local prototyping.
#   - Stores raw text strings and vector arrays together in one file.
#   - Has native metadata rules built right into the query engine.
#
# ⚡ FAISS (Facebook AI Similarity Search):
#   - Best for super low-latency checks across millions of files.
#   - Stores raw numbers in memory matrix lanes to maximize speed.
#   - Requires custom dictionary arrays to map values back to text.

# =====================================================================
# 🛡️ SENIOR DEV PRODUCTION GUARDRAILS & TIPS
# =====================================================================
# 🪓 Overlap Buffer -> Keep a 10-20% text overlap so sentences don't break.
# 🔒 Sandbox Rule   -> Give each separate client their own database collection.
# 🧩 Singleton base -> Load your database engine client once at application init.
# 🕵️ Hybrid Search   -> Mix keyword search with vector math for absolute safety.
