'''
Chapter5, topic - RAG architecture — deep understanding
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# RAG        -> Retrieval-Augmented Generation (An open-book exam for AI).
# Chunking   -> Chopping huge target documents into small, manageable text pieces.
# Embedding  -> Converting raw text strings into arrays of meaning-based numbers.
# Vector DB  -> A high-speed digital library storing items by conceptual similarity.
# Context    -> The exact relevant chunks injected directly into the LLM system prompt.

# =====================================================================
# 🔄 THE TWO CORE PIPELINE STAGES
# =====================================================================
# 📥 1. THE INGESTION PIPELINE:
#   - Document Loader parses raw files (.pdf, .txt, .json) into data text streams.
#   - Text Splitter segments text using safe token/character rolling window limits.
#   - Embedding Engine calculates mathematical values for every isolated text chunk.
#   - Database Client pushes vectors + metadata objects into persistent indexes.
#
# 📤 2. THE RETRIEVAL & GENERATION PIPELINE:
#   - Incoming user queries are dynamically vectorized by the runner script.
#   - Semantic Vector Search compares query vectors against the library collection.
#   - System Builder glues the nearest text fragments inside strict prompt blocks.
#   - Deterministic LLM execution parses inputs to synthesize precise responses.

# =====================================================================
# 🛡️ THE PRODUCTION ENGINE GUARDRAILS
# =====================================================================
# 🌡️ Temperature Zero -> Crucial setting (`temperature=0.0`) to kill hallucinations.
# 🔄 Rolling Overlaps -> Preventing split sentences by carrying context between chunks.
# 🏷️ Metadata Tags    -> Running fast pre-filters (`{"category": "legal"}`) before vector math.
# 🛑 Triage Checkpoints-> Returning human fallbacks immediately if vector distance scores are poor.
