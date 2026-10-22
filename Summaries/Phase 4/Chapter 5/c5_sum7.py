'''
Chapter5, topic - hybrid search — keyword + semantic
'''
# =====================================================================
# 🧠 HYBRID SEARCH CORE DEFINITIONS
# =====================================================================
# Hybrid Search -> Blends exact keyword matching with conceptual meaning.
# Sparse Vector -> The word matrix used for literal matches (e.g., BM25).
# Dense Vector  -> The numeric embeddings used for semantic intent search.
# Alpha (α)     -> The weight dial slider (0.0 = Pure Keyword, 1.0 = Pure Semantic).
# RRF           -> Reciprocal Rank Fusion algorithm that merges both result lists.

# =====================================================================
# 🏢 THE RETRIEVAL FACE-OFF
# =====================================================================
# 🔍 KEYWORD RETRIEVAL (SPARSE):
#   - Finds exact codes, SKU numbers, product versions, and unique tags.
#   - Blind to context: Searching "car" completely misses the word "automobile".
#
# 🧠 SEMANTIC RETRIEVAL (DENSE):
#   - Finds concepts, feelings, synonyms, and conversational intent.
#   - Blind to exact precision: Can easily mistake code "ERR-404" for "ERR-405".

# =====================================================================
# 🛡️ AGENCY PRODUCTION GUARDRAILS & TRICKS
# =====================================================================
# 1. Alphanumeric Regex Bypass:
#    If the query looks like a serial code, override alpha to favor keywords.
# 2. Score Normalization:
#    Always scale raw distance metrics to a standard 0.0 - 1.0 window before merging.
# 3. Dynamic Weight Tuning:
#    Use a fast classifier to set high alpha for chat and low alpha for lookups.
# 4. Text Clean Checking:
#    Strip trailing punctuations to protect literal token matching engines.
