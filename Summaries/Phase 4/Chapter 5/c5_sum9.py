'''
Chapter5, topic - advanced retrieval strategies
'''
# =====================================================================
# 🧠 ADVANCED RETRIEVAL STRATEGIES — ENGINE ARCHITECTURE
# =====================================================================
# Basic RAG  -> Standard vector search using simple keyword/phrase match.
# Expansion  -> Using a fast LLM to rewrite messy questions into multiple terms.
# Parent-Doc -> Searching small text snippets but retrieving large context blocks.
# Reranking  -> A secondary AI judge scoring exactly how well text answers a query.

# =====================================================================
# 🛠️ ADVANCED RETRIEVAL PIPELINE STEP-BY-STEP
# =====================================================================
# STEP 1: Query Transformation (The Interpreter)
#   - Raw user input is often vague, short, or filled with slang.
#   - Pass the query to a fast model (`gpt-4o-mini`) to generate variations.
#   - Maps "desk money" to `["hardware stipend", "office budget", "allowance"]`.
#
# STEP 2: Multi-Vector Retrieval & Aggregation
#   - Query the Vector DB using all generated query variations.
#   - Combine all returned text fragments into a single processing list.
#   - Deduplicate documents using unique metadata keys or content hashes.
#
# STEP 3: Context Enrichment (Parent-Child Tracking)
#   - If a child chunk is matched, swap it for its parent chunk programmatically.
#   - Ensures the LLM gets comprehensive background data rather than raw snippets.
#
# STEP 4: Cross-Encoder Reranking (The Final Judge)
#   - Run the aggregated text blocks through a specialized model (`FlashRank`).
#   - Re-score and sort the array, placing the absolute best match at index 0.
#   - Filter out any document hit that falls below a safety threshold (e.g. < 0.30).

# =====================================================================
# 🚀 PRODUCTION GUARDRAILS & PERFORMANCE
# =====================================================================
#   - Never block your primary application thread with heavy, local models.
#   - Enforce maximum token budgets on parent context to prevent huge bills.
#   - Gracefully fallback to a human handoff if rerank scores are too low.
