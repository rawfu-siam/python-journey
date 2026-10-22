'''
Chapter5, topic - ChromaDB — local vector database
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# ChromaDB   -> A local vector database that understands text meaning.
# Vector     -> A list of numbers representing semantic context/ideas.
# Embedding  -> The mathematical conversion of strings into vectors.
# Collection -> A distinct storage table or bucket grouping related data.

# =====================================================================
# 🛠️ PRODUCTION ARCHITECTURE & OPERATION STEPS
# =====================================================================
# 💾 PERSISTENCE:
#   - Avoid pure in-memory clients which wipe data on runtime death.
#   - Always isolate path logic via .env paths using `PersistentClient`.
#
# ⚡ DATA OPERATIONS:
#   - `.get_or_create_collection()` prevents runtime recreation errors.
#   - Prefer `.upsert()` over `.add()` to modify existing entries cleanly.
#   - Always feed structured IDs and parallel `metadatas` arrays.
#
# 🛡️ SECURITY & RETRIEVAL:
#   - Pass a unique key inside `where={}` dicts for multi-tenant isolation.
#   - `n_results` sets the exact ceiling on returned context elements.

# =====================================================================
# 🚀 CORE PRODUCTION WORKFLOW OVERVIEW
# =====================================================================
# import chromadb
# client = chromadb.PersistentClient(path="./production_vault")
# collection = client.get_or_create_collection(name="kb_system")
# collection.upsert(ids=["id_1"], documents=["text"], metadatas=[{"k": "v"}])
# res = collection.query(query_texts=["query"], n_results=1, where={"k": "v"})
