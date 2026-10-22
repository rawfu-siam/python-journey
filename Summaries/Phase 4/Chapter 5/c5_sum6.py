'''
Chapter5, topic - Weaviate basics
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# Weaviate   -> Enterprise-scale vector database built for huge datasets.
# Class      -> A structured schema blueprint (like an SQL data table).
# Properties -> Typed data fields (columns) assigned inside a Class.
# Vectorizer -> Built-in AI module converting incoming text to vectors.

# =====================================================================
# 🛠️ MODERN V4 SYNTAX RULES & PROTOCOLS
# =====================================================================
# 🔌 CONNECTION MANAGEMENT:
#   - Use `weaviate.connect_to_local()` for local docker testing environments.
#   - Always wrap calls inside try/finally blocks to fire `client.close()`.
#
# 📊 SCHEMA & COLLECTION HANDLING:
#   - Access tables exclusively via the `client.collections` namespace.
#   - `.create()` establishes schemas; `.exists()` prevents overwrite errors.
#   - Manual vector matrices can be directly mapped using `vector=[]`.
#
# 🎯 ENTERPRISE RETRIEVAL:
#   - Use `.query.near_vector()` to scan coordinates for semantic similarity.
#   - Extract distance scores from objects using return_metadata parameters.

# =====================================================================
# 🚀 QUICK-START CODE ARCHITECTURE REFERENCE
# =====================================================================
# import weaviate
# client = weaviate.connect_to_local()
# try:
#     coll = client.collections.get("Article")
#     coll.insert(properties={"title": "Test"}, vector=[0.1, 0.9])
#     res = coll.query.near_vector(near_vector=[0.1, 0.9], limit=1)
# finally:
#     client.close()
