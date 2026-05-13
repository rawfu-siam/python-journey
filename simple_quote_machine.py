# ============================================
# PROJECT : Simple Quote Printer Machine
# AUTHOR  : Rawfu Siam
# DATE    : May 13, 2026
# TOPICS  : print(), sep=, end=, import, random
# ============================================

import random

# --- All quotes stored as one list ---
quotes = [
    ("The secret of getting ahead is getting started.",               "Mark Twain"        ),    
    ("Code is like humor. When you have to explain it, it's bad.",    "Cory House"        ),
    ("First, solve the problem. Then, write the code.",               "John Johnson"      ),
    ("The best time to plant a tree was 20 years ago.",               "Chinese Proverb"   ),
    ("It always seems impossible until it is done.",                  "Nelson Mandela"    ),
    ("Push yourself because no one else will do it for you.",         "Unknown"           ),
    ("Dream big. Start small. Act now.",                              "Robin Sharma"      ),
    ("Consistency is the key to achieving and maintaining momentum.", "Darren Hardy"      ),
]

# --- Pick one random quote ---
quote, author = random.choice(quotes)

# --- Print the result ---
print()
print("━" * 45)
print("   💬 QUOTE OF THE DAY")
print("━" * 45)
print()
print(" ", quote)        # quote text
print()
print(" ", "—", author, sep=" ")  # author name
print()
print("━" * 45)
print("   github.com/rawfu-siam")
print("━" * 45)
print()