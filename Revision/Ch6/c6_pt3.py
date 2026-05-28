'''
Chapter6, topic - conditional expression / ternary operator / one liner
'''
'''
Task 1 (Medium): Automated Server Status Alert Create a variable 
called server_load_percentage. Write a single-line conditional 
expression that saves "🚨 CRITICAL OVERLOAD" to a variable named 
system_alert if the load is greater than 85, otherwise save 
"🟢 Server Healthy". Print out system_alert.
'''
server_load_percentage = 75
system_alert="CRITICAL OVERLOAD" if server_load_percentage>85 else "Server Healthy"
print(system_alert)
'''
Task 2 (Intermediate): AI Model Selector Tool 🤖Create a variable called 
input_word_count. Write a one-liner expression that assigns "gpt-4o-heavy" 
to a variable named target_model if the word count is greater than 2000 words. 
Otherwise, it should assign "gpt-4o-mini". Print out the selected model
'''
input_word_count = 2100
target_model = "gpt-4o-heavy" if input_word_count>2000 else "gpt-4o-mini"
print(target_model)
'''
Task 3 (Professional Challenge): Agency Invoicing Discount 📊Create two 
variables: invoice_amount (Integer) and is_loyal_client (Boolean).Write a 
single-line conditional expression that calculates a 10% discount on the 
total invoice value if is_loyal_client is True. Otherwise, the discount 
is 0.Hint: You can calculate a 10% discount value directly using math 
expressions inside your one-liner, like invoice_amount * 0.10. Print 
out the final calculated discount string.
'''
invoice_amount = 99
is_loyal_client = True
discount = invoice_amount*0.10 if is_loyal_client else invoice_amount*0
print(discount)
