'''
Chapter6, topic - nested loop 
'''
'''
Task 1 (Medium): Dual-Store Inventory Synchronizer 🏬Create two lists: 
stores = ["Dhaka_Hub", "Chittagong_Hub"] and products = ["Keyboard", "Mouse"]. 
Write a nested loop system that links them together. For each store, loop 
through and print out: "📦 Dispatching 50 units of [product_name] to [store_name].".
'''
stores = ["Dhaka_Hub", "Chittagong_Hub"]
products = ["Keyboard", "Mouse"]
for store in stores:
    for product in products:
        print(f"📦 Dispatching 50 units of {product} to {store}.")
'''
Task 2 (Intermediate): Multi-Agent Password Hack Simulator 🔐Create a list of 
strings called usernames = ["admin_siam", "dev_user"] and a list of integers 
called pin_codes = [1111, 2222, 3333]. Write a nested loop layout that tests 
every single pin against every user name. Print: "🔄 Testing User: [user] | 
Trying PIN: [pin]...".
'''
usernames = ["admin_siam", "dev_user"]
pin_codes = [1111, 2222, 3333]
for username in usernames:
    for pin in pin_codes:
        print(f"🔄 Testing User: {username} | Trying PIN: {pin}...")
'''
Task 3 (Professional Challenge): Corporate Database Token Auditor 📊
Create a list of dictionaries exactly like this: agency_accounts = [
{"name": "Siam", "tokens": [450, 500]},{"name": "Alice", "tokens": [1200, 300]},
{"name": "Zayn", "tokens":[35, 750]}Write an optimization script using nested loops 
to scan through this dataset.The outer loop should target the account 
dictionary names.The inner loop should run through the integers inside 
the "tokens" list array.If an individual token value drops below 50, 
trigger a warning alert: "🚨 WARNING: Low token count found for [user_name]!
Value: [token_value]".Otherwise, calculate and print: "🟢 Token batch verified 
for [user_name]: [token_value]".]
'''
agency_accounts = [
    {"name": "Siam",  "tokens": [450, 500] },
    {"name": "Alice", "tokens": [1200, 300]},
    {"name": "Zayn",  "tokens": [35, 750]  }]
for account in agency_accounts:
    user_name = account["name"]
    for token in account["tokens"]:
        if token < 50:
            print(f"🚨 WARNING: Low token count found for {user_name} !Value: {token}")
        else:
            print(f"🟢 Token batch verified for {user_name} : {token}")
