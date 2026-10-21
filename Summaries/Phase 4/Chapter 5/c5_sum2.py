'''
Chapter5, topic - chunking strategies — size, overlap, semantic
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & STRATEGIES
# =====================================================================
# Fixed-Size -> Rigidly splitting text at exact character or token counts.
# Overlap    -> Copying trailing text to the next chunk for context safety.
# Semantic   -> Splitting text dynamically only when the meaning shifts.
# Parent-Child-> Searching tiny child chunks but sending giant parent text blocks.
# Tokenizer  -> Math parser converting strings to exact AI readable fragments.

# =====================================================================
# 📊 STRATEGY COMPARISON MATRIX
# =====================================================================
# 📐 FIXED-SIZE SEPARATION:
#   - Pros: Lightning fast, minimal processing overhead, highly predictable.
#   - Cons: Blindly tears sentences apart, dropping factual data values.
#
# 🔄 OVERLAPPING SLIDING WINDOWS:
#   - Pros: Creates a safety web; glues broken boundaries back together.
#   - Cons: Increases total vector storage footprints due to duplicate text.
#
# 🧠 DYNAMIC SEMANTIC TRACKING:
#   - Pros: Maximum accuracy; groups thoughts perfectly by their context.
#   - Cons: Requires heavy processing power to calculate sentence vectors.

# =====================================================================
# 🛡️ THE SENIOR ENGINE WORKFLOW
# =====================================================================
# 📏 Token vs Char -> Always chunk using `tiktoken` metrics instead of `len()`.
# 🪟 Overlap Rule  -> Maintain a strict 10% to 20% footprint buffer size.
# 🔗 Parent Link   -> Index small child nodes but query their broad parent sources.
# 🏷️ Layout Safety -> Keep headers (`#`) intact to prevent document schema loss.
