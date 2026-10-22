'''
Chapter5, topic - Pinecone — cloud vector database
'''
# =====================================================================
# 🧠 CORE PINECONE DEFINITIONS
# =====================================================================
# Pinecone  -> A cloud-native vector database optimized for semantic search.
# Index     -> The main data vault configured with a specific dimension size.
# Vector ID -> A unique string key assigned to locate a specific vector.
# Metadata  -> Text details or category tags attached directly to a vector.
# Namespace -> An isolated zone separating distinct customer environments.

# =====================================================================
# 🛠️ CORE OPERATIONAL PIPELINES
# =====================================================================
# ⬆️ Upserting Data:
#   - Pushes vectors and metadata dicts into an index.
#   - Always specify a namespace to keep client sandboxes cleanly separated.
#
# 🔍 Querying Data:
#   - Compares a query vector against the index to find nearest neighbors.
#   - CRITICAL: Must pass include_metadata=True to receive raw text strings.
#   - Filters can narrow matches down by metadata properties (e.g., {"category": "tech"}).

# =====================================================================
# 🛡️ SENIOR DEV PRODUCTION GUARDRAILS
# =====================================================================
# 🏎️ Serverless First    -> Choose Serverless indexes to save client cloud costs when idle.
# ⚖️ Metric Alignment    -> Match index metrics (like Cosine) directly with model output rules.
# 📦 External Storage   -> Keep giant raw text payloads in SQL/NoSQL databases, not Pinecone.
# ⚡ Batch Operations    -> Group vectors in sets of 100 before calling upsert pipelines.
