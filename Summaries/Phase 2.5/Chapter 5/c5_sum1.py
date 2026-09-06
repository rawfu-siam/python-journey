'''
Chapter5, topic - Pydantic BaseModel setup for data parsing
'''
# =====================================================================
# 🧠 PYDANTIC BASEMODEL SETUP FOR DATA PARSING
# =====================================================================
# Pydantic   -> A strict digital bouncer/filter for Python data validation & parsing.
# BaseModel  -> The core class inherited to turn normal classes into validation contracts.
# Coercion   -> The automatic cleaning/casting of mismatched data types (e.g., "12" -> 12).
# ValidationError -> The exception thrown when data completely violates schema rules.

# =====================================================================
# 🧩 CORE MECHANICS
# =====================================================================
# 1. Import   -> from pydantic import BaseModel
# 2. Schema   -> class MyModel(BaseModel): field: type
# 3. Parse    -> obj = MyModel(**dictionary_data)
# 4. JSON     -> obj = MyModel.model_validate_json(raw_string)
# 5. Dump     -> clean_dict = obj.model_dump()

# =====================================================================
# ⚠️ COMMON MISTAKES & PRO TIPS
# =====================================================================
# - Always wrap remote API/webhook parsing in try/except ValidationError blocks.
# - Always unpack incoming dictionaries using the double-asterisk operator (**).
# - Use Field(description="...") to give AI models context on what data to extract.
# - Centralize your schemas into a dedicated models.py or schemas/ folder.
