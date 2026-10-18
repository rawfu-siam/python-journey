'''
Chapter4, topic - CrewAI flows — event-driven agent pipelines
'''
# =====================================================================
# 🧠 CREWAI FLOWS CORE ARCHITECTURE — REPOSITORY REFERENCE
# =====================================================================
# Flow Class   -> The master pipeline controller hosting state & actions.
# State        -> A centralized Pydantic clipboard shared by all steps.
# @start()     -> The primary green-light entry point trigger decorator.
# @listen()    -> Event-driven ears waiting for a target step to finish.
# @router()    -> A decision checkpoint that returns string route signals.

# =====================================================================
# 🏢 ENTERPRISE PIPELINE DESIGN CHEAT SHEET
# =====================================================================
# 🧼 LEAN METHOD STRATEGY:
#   - Keep flow logic thin; shift heavy actions to separate modules.
#   - Call external utility functions inside @listen frames.
#
# 📋 ZERO-TRUST DATA FLOW:
#   - Always enforce precise Pydantic typings across variables.
#   - Use clear defaults to avoid blank state instantiation crashes.
#
# 📊 PRODUCTION DEPLOYMENT STANDARD:
#   - Swap all basic print() statements out for enterprise logging.
#   - Call flow.plot() to auto-generate graphical architecture maps.
#
# 🪄 THE PIPELINE CATCHPHRASE:
#   - "Events trigger the tracks, but the State carries the payload."
# =====================================================================
