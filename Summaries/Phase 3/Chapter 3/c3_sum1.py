'''
Chapter3, topic - BeautifulSoup4 — parsing HTML
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# BeautifulSoup4 -> A Python library that turns raw, messy HTML text 
#                  into an organized, searchable element tree.
# Parsing        -> The act of reading, breaking down, and extracting 
#                  structured data from unorganized web code strings.
# HTML Tags      -> Code blocks (<p>, <h1>, <div>) defining content type.
# Attributes     -> Hidden key-value traits like "id" (unique passport) 
#                  and "class" (group/style uniform) inside a tag.
# Inner Text     -> The clean human text sitting safely inside the tags.

# =====================================================================
# 🛠️ THE CORE BS4 PARSING COMMANDS
# =====================================================================
# soup = BeautifulSoup(html, 'html.parser')
#   - Initializes the tool and reads raw text layout.
#
# soup.tag_name
#   - Short cut to grab the absolute FIRST occurrence of that tag.
#
# soup.find("tag", class_="name") / soup.find(id="unique-id")
#   - Targets ONE specific element matching the class or ID criteria.
#   - Returns None if no matching element is found on the page.
#   - CRITICAL: Remember the trailing underscore on class_!
#
# soup.find_all("tag", class_="name")
#   - Searches the entire tree and collects ALL matches into a list.
#   - You must loop through this list to extract individual data points.
#
# tag.text
#   - Strips away all HTML brackets, leaving only clean text data.
#
# tag['attribute_name']
#   - Treats the tag like a dictionary to pull hidden items like href links.

# =====================================================================
# ⚠️ THE DEFENSIVE JUNIOR DEV PLAYBOOK
# =====================================================================
# 1. Protect against 'NoneType' crashes:
#    Always verify an element exists before calling .text on it.
#    Example: if element: print(element.text)
#
# 2. Think in Containers:
#    Isolate the parent layout card first using find_all(), then loop 
#    inside that specific container card to pull matching titles/prices.
#
# 3. Look Human:
#    Pass custom User-Agent strings in your headers to avoid getting 
#    instantly geo-blocked or flagged by strict Australian websites.
