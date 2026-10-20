'''
Chapter2, topic - embeddings — OpenAI, HuggingFace
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# Embedding -> A model transforming text into structured lists of numbers.
# Vector    -> The numerical coordinate list representing text meaning.
# Dimension -> The size of the vector array (e.g., 1536 unique dimensions).
# Match     -> Using geometric math (Cosine Similarity) to find close concepts.

# =====================================================================
# 🏢 CLOUD VS. OFFLINE LOCAL FACE-OFF
# =====================================================================
# 🌐 OpenAI Embeddings (Cloud):
#   - Accessed via network API calls; requires a secure .env secret key.
#   - Exceptionally high multi-language accuracy but incurs token costs.
#
# 🤗 HuggingFace Embeddings (Local):
#   - Runs completely offline, drawing power directly from host hardware.
#   - Zero runtime platform API fees and keeps data perfectly secure.

# =====================================================================
# 🛡️ PRODUCTION MISTAKES & SENIOR AGENCY SECRETS
# =====================================================================
# ❌ Beginner Flaw -> Mixing two different models inside a single pipeline.
# ❌ Beginner Flaw -> Storing array lists in raw SQL text fields at scale.
#
# ⚡ Senior Secret -> Use one unified model for text database and user queries.
# ⚡ Senior Secret -> Offload similarity search computations to a Vector DB.
# ⚡ Senior Secret -> Merge semantic search with keyword search (Hybrid Search).
