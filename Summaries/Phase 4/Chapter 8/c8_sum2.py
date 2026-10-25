'''
Chapter8, topic - State Graphs — nodes, edges, and conditional edges
'''
# =====================================================================
# 🧠 CORE DEFINITIONS: STATE GRAPHS
# =====================================================================
# State Graph      -> A structured flowchart map for guiding data flow 
#                     and logic through worker nodes and decision pathways.
# State            -> The shared central memory bag (TypedDict) holding all 
#                     pipeline data as it travels between nodes.
# Node             -> A standard Python worker function performing one 
#                     specific task (e.g., checking inventory, calling an LLM).
# Edge             -> A direct, fixed pathway connecting two nodes sequentially.
# Conditional Edge -> A smart traffic-light function inspecting state 
#                          to dynamically route data (enabling forks and loops).

# =====================================================================
# 🏢 AGENCY PRODUCTION TIPS & GUARDRAILS
# =====================================================================
# - Always ensure every node function explicitly returns the updated state dictionary.
# - Match conditional routing return strings precisely with route dictionary keys.
# - Keep state dictionaries lean and focused only on shared workflow variables.
# - Avoid dead ends by properly connecting all terminal nodes to the END marker.