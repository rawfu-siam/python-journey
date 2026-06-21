'''
Chapter4, topic - endswith(), startswith(), count(), replace(), find()
'''
'''
Task 1 (Medium): Create a clean script file named c4_pt6.py inside your 
Chapter 4 directory. Create a string variable representing an invoice
tracking reference code: invoice_ref = "INV-9084_PAID". Use .endswith() 
to check if the file ends with the text string "PAID". Print out the 
direct True/False boolean answer.
'''
invoice_ref = "INV-9084_PAID"
print(invoice_ref.endswith("PAID"))
'''
Task 2 (Hard): Create a variable named war_strategy holding the text: 
"hours of code, hours of math, hours of theory". Run a print statement 
that uses .count() to dynamically find exactly how many times the word 
"hours" appears in your strategy string. Below it, use .find() to
print out the index location room number where the word "math" begins.
'''
war_strategy = "hours of code, hours of math, hours of theory"
print(war_strategy.count("hours"))
print(war_strategy.find("math"))
'''
Task 3 (Professional Business Problem): Build an internal automated 
data routing script layout. Create a string text variable representing 
a server asset description pathway line: server_asset = "root_user_Japan_CSE". 
Use the correct .replace() method to swap out the word "Japan" for 
the string word "Bangladesh". Print the final outcome inside a 
clean f-string tracking block.
'''
server_asset = "root_user_Japan_CSE"
correction = server_asset.replace("Japan", "Bangladesh")
print(f"server asset after correction: {correction}")
