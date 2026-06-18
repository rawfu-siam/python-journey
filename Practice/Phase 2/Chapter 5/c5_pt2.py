'''
Chapter5, topic - regex (regular expressions)
'''
'''
Task 1 (Easy) — The Zip Code Sweeper Goal: Create a function named 
extract_zip_codes that takes a text string parameter named address_text. 
Use re.findall() to search for and return a list of all instances where 
exactly 5 numbers in a row appear (representing regional zip codes).
Action: Test it by passing the sentence "Shipping nodes are located at 
hubs 10021, 94103, and 55102.". Verify it pulls the numbers into a 
clean list array
'''
import re
def extract_zip_codes(address_text):
    pattern = r"\d{5}"
    zip_code = re.findall(pattern, address_text)
    return zip_code
the_sentence = "Shipping nodes are located at hubs 10021, 94103, and 55102."
test1 = extract_zip_codes(the_sentence)
print(test1)
'''
Task 2 (Medium) — The Agent Protocol Key Tracker Goal: Create a function 
named track_agent_keys that takes a string parameter named log_data. The 
function must look for system security keys that always start with the 
capital literal text "AGENT_" followed by exactly 3 digits 
(e.g., "AGENT_702"). Return the list of matches. Action: Test it by 
passing the log string: "System failure reported by AGENT_102 and 
cleared by AGENT_405.". Print the outcome.
'''
def track_agent_keys(log_data):
    pattern = r"AGENT_\d{3}"
    agent_keys = re.findall(pattern, log_data)
    return agent_keys
log_string = "System failure reported by AGENT_102 and cleared by AGENT_405."
print(track_agent_keys(log_string))
'''
Task 3 (Bit Harder) — The Clean Cash Extractor Goal: Create a function 
named gather_clean_prices that takes a string parameter named receipt_text. 
The function must use Regex to extract monetary values formatted with a 
decimal point and cents, specifically starting with a literal $ sign 
followed by any amount of numbers, a literal period ., and exactly 2 
digits for cents (e.g., r"\$\d+\.\d{2}").Action: Test your pipeline 
function by passing the invoice block text: "Server subscription renewed 
for $45.99, data storage added for $120.50, tax was $0.00.". Print the 
resulting list to ensure cent balances are completely preserved.
'''
def gather_clean_prices(receipt_text):
    pattern = r"\$\d+\.\d{2}"
    amounts = re.findall(pattern, receipt_text)
    return amounts
invoice = "Server subscription renewed for $45.99, data storage added for $120.50, tax was $0.00."
print(gather_clean_prices(invoice))
