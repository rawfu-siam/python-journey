'''
Chapter8, topic - Dockerfile — writing your first container
'''
# =====================================================================
# 🧠 DOCKER CORE DEFINITIONS
# =====================================================================
# Dockerfile -> A plain text recipe file with instructions to build an image.
# Image      -> A frozen, unchangeable blueprint snapshot of your application.
# Container  -> A live, isolated mini-computer running the image instance.
#
# =====================================================================
# 🏗️ THE 5 PRIMARY BLUEPRINT COMMANDS
# =====================================================================
# FROM    -> Establishes the foundation OS and language layer (e.g., Python).
# WORKDIR -> Sets up the home project folder directory inside the container.
# RUN     -> Executes software installers at build time (e.g., pip install).
# COPY    -> Moves files from your local host machine into the container.
# CMD     -> The absolute final ignition switch that starts your automation.
#
# =====================================================================
# 🛡️ ENTERPRISE PRODUCTION GUARDRAILS
# =====================================================================
# 1. Caching Optimizations:
#    - ALWAYS copy 'requirements.txt' and 'RUN pip install' BEFORE 'COPY . .'.
#    - This avoids rebuilding unchanged code libraries, saving hours of dev time.
#
# 2. Zero-Trust Security Hygiene:
#    - Maintain a strict '.dockerignore' matrix file.
#    - NEVER bake virtual folders ('env/') or private API keys ('.env') inside.
#    - Implement a non-root 'USER' to restrict unauthorized server access.
#
# 3. Low-Latency Reliability:
#    - Set 'ENV PYTHONUNBUFFERED=1' so application print logs stream instantly.
#    - Always pin exact language image versions to prevent future breaks.
# =====================================================================
