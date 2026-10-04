'''
Chapter1, topic - structured output — JSON mode
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# JSON Mode -> An API parameter locking OpenAI into raw data delivery.
# Switch    -> Enforced by setting: response_format={"type": "json_object"}
# Golden Rule-> You MUST explicitly include the word "JSON" in the prompt!
# Parsing   -> AI outputs a string. Convert it via: json.loads(response_text)

# =====================================================================
# ⚡ PRODUCTION SCHEMA TEMPLATE EXAMPLE
# =====================================================================
# Below is a standard structural layout passed to automation pipelines:
#
# {
#   "lead_data": {
#     "contact_name": "Alex Mercer",
#     "company": "Nexus Automation Labs",
#     "detected_budget_usd": 12500,
#     "is_qualified": true
#   },
#   "system_meta": {
#     "confidence_score": 0.99,
#     "routing_destination": "sales_pipeline"
#   }
# }

# =====================================================================
# 🛡️ AGENCY-GRADE JUNIOR DEV BEST PRACTICES
# =====================================================================
# 1. DEFENSIVE PARSING: Never expect the AI to be 100% stable. 
#    Always wrap json.loads() in a try/except JSONDecodeError block.
# 2. KEY STANDARDIZATION: Keep JSON object keys in clean snake_case.
# 3. COST OPTIMIZATION: Keep key names short to minimize token overhead.
# 4. STEPPING UP: Transition from raw JSON Mode to Pydantic parsing 
#    using client.beta.chat.completions.parse() for auto-validated schemas.
