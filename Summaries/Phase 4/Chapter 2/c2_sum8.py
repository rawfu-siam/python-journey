'''
Chapter2, topic - text splitters — chunking strategies
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# Text Splitter -> Tool that cuts a massive file into small text pieces.
# Chunk          -> The individual, small slice of text cut by the splitter.
# Chunk Size     -> Maximum characters/tokens allowed inside one single slice.
# Chunk Overlap  -> Duplicate text padding shared between adjacent chunks.
#                   Acts as a contextual bridge so sentences aren't lost.

# =====================================================================
# 🪓 CHUNKING STRATEGIES FACE-OFF
# =====================================================================
# 🎯 CharacterTextSplitter:
#   - Rigidly splits text based on raw character count metrics.
#   - High risk of cutting words or key phrases completely in half.
#
# 🧠 RecursiveCharacterTextSplitter:
#   - Professional agency go-to for standard text files and PDFs.
#   - Tries splitting sequentially by paragraphs, sentences, then words.
#   - Keeps clean, complete human thoughts and logical ideas intact.

# =====================================================================
# 🛡️ PRODUCTION MISTAKES & SENIOR AGENCY SECRETS
# =====================================================================
# ❌ Beginner Flaw -> Setting overlap to 0, destroying context at cuts.
# ❌ Beginner Flaw -> Hardcoding character counts for specialized files.
#
# ⚡ Senior Secret -> Maintain overlap at 10% to 20% of your total size.
# ⚡ Senior Secret -> Split by Tokens (via Tiktoken) to manage API billing.
# ⚡ Senior Secret -> Carry file path/page metadata cleanly on every chunk.
