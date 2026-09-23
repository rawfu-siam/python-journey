'''
Chapter8, topic - docker build, run, ps, stop, rm
'''
# =====================================================================
# 🧠 DOCKER CORE CONCEPTS & DEFINITIONS
# =====================================================================
# Dockerfile -> The raw text instruction booklet outlining app construction.
# Image      -> The read-only, compiled master blueprint package (The Recipe).
# Container  -> The live, isolated running instance inside memory (The Soup).
#
# =====================================================================
# 🛠️ THE 5 MAGICAL AUTOMATION COMMANDS
# =====================================================================
# 1. docker build -t <name> .
#    - Compiles a Dockerfile into a reusable, read-only system Image.
#    - The '-t' flag assigns a clean, human-readable name tag.
#    - The '.' specifies the current folder directory as the context block.
#
# 2. docker run -d --name <custom_name> <image_name>
#    - Spins an Image blueprint into a living, fully active Container.
#    - The '-d' flag detaches the execution into the quiet background.
#    - The '--name' assigns a fixed nickname to prevent system name chaos.
#
# 3. docker ps -a
#    - Acts as a system tracker displaying active and inactive containers.
#    - Plain 'docker ps' only displays containers actively running.
#    - Adding the '-a' flag reveals dead, crashed, or exited containers.
#
# 4. docker stop <container_identifier>
#    - Dispatches a polite SIGTERM shutdown signal to a running container.
#    - Allows Python automation tasks to save states and close gracefully.
#
# 5. docker rm <container_identifier>
#    - Acts as the digital janitor to purge stopped container structures.
#    - Will throw an error if executed against an actively running container.
#
# =====================================================================
# ⚠️ CRITICAL PRODUCTION MISTAKES TO AVOID
# =====================================================================
# - Forgetting the trailing dot (.) on builds, crashing the path compiler.
# - Reusing active custom names before running 'docker rm' on old ghosts.
# - Attempting to run 'docker rm' on active processes before a 'docker stop'.
#
# =====================================================================
# 🎬 THE BACKSTAGE PASS: PRO DEV SHORTCUTS
# =====================================================================
# - docker container prune -f -> Instantly wipes all dead containers at once.
# - The '--rm' run flag      -> Auto-deletes a container the second it finishes.
# - The Short ID Trick        -> Supply only the first 3-4 digits of a container ID.
#
# =====================================================================
# 🇺🇸 USA AI AGENCY BEST PRACTICES
# =====================================================================
# - Always utilize slim base layers (e.g., python:3.11-slim) to minimize costs.
# - Enforce custom descriptive naming strategies for absolute search tracking.
# - Design architectures using distributed, small, clean microservice containers.
