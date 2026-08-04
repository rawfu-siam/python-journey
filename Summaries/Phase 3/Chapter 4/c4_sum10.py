'''
Chapter4, topic - MongoDB basics — PyMongo
'''
# =====================================================================
# 🧠 MONGODB & PYMONGO CORE DEFINITIONS
# =====================================================================
# NoSQL DB -> A flexible database storing data as folders instead of tables.
# PyMongo  -> The translator library connecting Python scripts to MongoDB.
# Client   -> The network engine/truck establishing the active DB connection.
# Database -> The separate room or vault inside the main warehouse.
# Collection -> The filing cabinet storing groups of files (SQL Table equivalent).
# Document -> Individual data sheets shaped exactly like a Python Dict {}.

# =====================================================================
# ⚡ THE AGILITY VALUE (WHY BUSINESSES LOVE IT)
# =====================================================================
# - Dynamic Schemas: Documents in the same collection can have different keys.
# - High Speed: Perfect for messy Web Scraping and rapid AI Agent outputs.
# - Growth Friendly: Business scaling never halts for rigid SQL migrations.

# =====================================================================
# 🛠️ THE PYMONGO CORE COMMAND CHEAT-SHEET
# =====================================================================
# client = MongoClient("mongodb://localhost:27017/") -> Fire up the truck.
# db = client["agency_db"]                             -> Open the vault.
# collection = db["clients"]                          -> Pull open the cabinet.
#
# collection.insert_one(dict)                         -> File 1 single folder.
# collection.insert_many(list_of_dicts)               -> File a batch of folders.
# collection.find_one({"key": "val"})                 -> Pull 1 matching document.
# collection.find({"price": {"$gt": 1000}})           -> Pull a cursor stream of matches.
# collection.update_one(filter, {"$set": new_data})   -> Safely change a document field.

# =====================================================================
# ⚠️ SENIOR DEV CODE SAFETY DEFUSAL GUIDE
# =====================================================================
# 1. ALWAYS iterate find() results using a for-loop (it returns a cursor).
# 2. ALWAYS use the "$set" operator in updates to prevent wiping document keys.
# 3. ALWAYS cast string IDs via ObjectId("str") when searching by the system _id.
# 4. ALWAYS isolate server connection strings in a hidden secure `.env` file.
# 5. ALWAYS use 'upsert=True' in updates to safely combine create/edit logics.
