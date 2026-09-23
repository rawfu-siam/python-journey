'''
Chapter8, topic - docker-compose for multi-container apps
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & ARCHITECTURE
# =====================================================================
# Dockerfile     -> The recipe to build ONE isolated application box.
# Docker-Compose -> The manager that launches & links MULTIPLE boxes.
# YAML (.yml)    -> The configuration syntax using strict spacing/indents.
#
# =====================================================================
# 🏢 THE 4 CORE PILLARS OF COMPOSE
# =====================================================================
# 🏗️ Services : The containers themselves (e.g., FastAPI app, Postgres DB).
# 🔌 Networks : Private virtual networks allowing containers to talk.
# 💾 Volumes  : Persistent disk drives keeping data safe if apps crash.
# 🔑 Environment: Zero-trust variables injected securely from a .env file.
#
# =====================================================================
# 🪄 THE ELITE SENIOR DEV PLAYBOOK RULES
# =====================================================================
# 🛰️ DNS Hack   : Container names become their domain names automatically!
#                 Example: Connecting to "mongodb://database_service:27017"
# ⏳ Boot Trap  : "depends_on" only starts containers; it doesn't wait for 
#                 internal application health checks or readiness.
# 🚪 Port Rule  : Host Port (Left) is your computer; Container Port (Right)
#                 is internal. Syntax -> "HOST_PORT:CONTAINER_PORT".
#
# =====================================================================
# 🛠️ INDUSTRIAL TERMINAL CHEAT SHEET
# =====================================================================
# docker-compose up      -> Launches entire ecosystem in the foreground.
# docker-compose up -d   -> Launches ecosystem in background (Detached).
# docker-compose down    -> Stops everything and wipes the temporary paths.
# docker-compose ps      -> Lists status profiles for all active services.
# docker-compose logs -f -> Streams live outputs from all running workers.
