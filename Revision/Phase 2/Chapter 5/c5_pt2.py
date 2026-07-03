'''
Chapter5, topic - regex (regular expressions)
'''
r'''
Task 1 (Easy): System Error Code Extractor. Extract a target integer identifier code 
out of a diagnostic server string response. Setup: Import the re module. Logic: Given 
the text line string server_log = "CRITICAL FAILURE: Error code 505 encountered.", 
write a script using re.search() with the pattern r"\d+" to find the code number. 
Use .group() to extract the clean text string value and print it. Verification 
Parameter: Run your script directly and verify that your workspace terminal displays 
exactly the isolated string value "505".
'''
import re
server_log = "CRITICAL FAILURE: Error code 505 encountered."
pattern = r"\d+"
code_number = re.search(pattern, server_log)
print(code_number.group())
r'''
Task 2 (Medium): Automation Webhook Hashtag Scraper. Build a clean text extraction module 
for user tags. Logic: Write a function named extract_hashtags that takes a single text 
string argument named post_text. The function must use re.findall() to find all 
occurrences of a hashtag pattern consisting of an actual # symbol followed immediately 
by one or more letters or digits (\w+). The function must return all matches as a 
clean list (-> list). Verification Parameter: Initialize a test string: 
test_message = "Building an agency using #python and #n8n automation!". Verify that 
passing test_message into extract_hashtags and printing the output returns exactly the 
list: ['#python', '#n8n'].
'''
import re
def extract_hashtags(post_text) -> list:
    pattern = r"#\w+"
    return re.findall(pattern, post_text)
test_message = "Building an agency using #python and #n8n automation!"
print(extract_hashtags(test_message))
'''
Task 3 (Above Average): Structured Serial Validator. Design a data pipeline filter function 
that extracts standard corporate license blocks from logs. Logic: Write a function named 
scrape_serial_codes that takes a single string argument named document_text. The function 
must look through the text and use re.findall() to extract all serial patterns configured 
strictly as: Two letters, an actual dash symbol, followed by exactly three digits 
(e.g., AZ-101). Return the results as a list. Verification Parameter: Create a validation 
text string: mock_doc = "Ship items labeled UT-854 and UT-991, but ignore item XY-99 and 
template UT-1234". Pass this into your function and verify that printing the output 
displays exactly the captured list matrix: ['UT-854', 'UT-991'].
'''
import re
def scrape_serial_codes(document_text):
    pattern = r"\b[a-zA-Z]{2}-\d{3}\b"
    return re.findall(pattern, document_text)
mock_doc = "Ship items labeled UT-854 and UT-991, but ignore item XY-99 and template UT-1234"
print(scrape_serial_codes(mock_doc))
