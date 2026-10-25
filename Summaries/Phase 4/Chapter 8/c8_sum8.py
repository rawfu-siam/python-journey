'''
Chapter8, topic - Sub-graphs — nestable graph architectures for complex workflows
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & CONCEPTS
# =====================================================================
# Sub-graphs       -> Smaller, independent mini-workflows nested inside a parent graph.
# Child Sub-graph  -> A focused agent team handling one specific sub-task.
# Parent Graph     -> The master workflow coordinating overall execution.
# Nesting          -> Adding an entire compiled sub-graph as a node.

# =====================================================================
# 🏗️ ARCHITECTURE PATTERNS & SETUP
# =====================================================================
# StateSchema      -> Independent dictionaries for parent and child data.
# add_node()       -> Method used to plug a compiled sub-graph into a parent.
# Data Flow        -> Passing specific inputs down and returning results up.
# Modular Files    -> Storing reusable sub-graphs in dedicated code folders.

# =====================================================================
# 🚀 AGENCY BEST PRACTICES & PRODUCTION TIPS
# =====================================================================
# Separate States  -> Avoid forcing identical keys across parent and child.
# Reusable Modules -> Import shared sub-graphs across multiple client apps.
# Clean Codebases  -> Keep files small instead of writing monolithic scripts.
# GitHub Storage   -> Push modular sub-graph packages to https://github.com/myagency.