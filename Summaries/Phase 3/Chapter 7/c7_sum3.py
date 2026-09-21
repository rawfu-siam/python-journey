'''
Chapter7, topic - n8n workflows — triggers, nodes, connections
'''
# =====================================================================
# 🧠 N8N WORKFLOW FUNDAMENTALS — DEFINITIONS
# =====================================================================
# Trigger     -> The Spark plug. Defines WHEN a workflow wakes up.
#                - Webhook: Listens at a specific URL for instant hits.
#                - Schedule: Fires on a cron-timer (e.g., Every Monday).
#                - Polling: Queries an application periodically for changes.
#
# Node        -> The Worker. Defines WHAT task gets executed.
#                - Pre-built blocks handle API structures automatically.
#                - Logic/Filter blocks route traffic down custom paths.
#                - Code blocks allow raw Python injections for complex math.
#
# Connection  -> The Highway. Defines HOW data travels down the line.
#                - Transports data as clean JSON lists of dictionaries.
#                - Guarantees sequential, step-by-step logic execution.

# =====================================================================
# 🛠️ EXPRESSIONS & DATA MANIPULATION
# =====================================================================
# - Variables are parsed dynamically using double curly brackets: {{ ... }}
# - Example: `{{ $json.body.customer_name }}` extracts incoming data.
# - Explicit targeting skips middleware and points directly to old steps:
#   `{{ $node["Webhook Trigger"].json.body.email }}`

# =====================================================================
# ⚠️ PRODUCTION DEFENSE CONTRACT (SENIOR DEV CRITICAL RULES)
# =====================================================================
# 1. Environment Guardrails:
#    - Build/debug loops exclusively using the `Test Webhook URL`.
#    - Move your live traffic to the `Production Webhook URL` ONLY when Active.
#
# 2. Resilient Infrastructure:
#    - Enable 'Retry on Failure' on heavy external API integrations.
#    - Rename and color-code blocks to tell an intuitive visual story.
#
# 3. Server Memory Health:
#    - Enable execution pruning to dump successful logs after 48 hours.
#    - Prevents enterprise pipeline memory crashes.

# =====================================================================
# 🪄 THE AUTOMATION GOLDEN SPELL
# =====================================================================
# "Fix the data shape at the node, and the connection highway runs on autopilot."
# =====================================================================
