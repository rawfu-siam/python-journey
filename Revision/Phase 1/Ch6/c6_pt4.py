'''
Chapter6, topic - in keyword
'''
'''
Task 1 (Medium): AI Automation Keyword Tracker 📊Create a variable called 
client_proposal_text holding any string paragraph. Write an if-else block 
using the in keyword to scan if the string contains the phrase "AI Automation". 
If it does, print "🤖 Route to AI agent engineers". If not, print "💻 
Route to basic software tier".
'''
client_proposal_text = "We want an AI Automation software for our business"
if "AI Automation" in client_proposal_text:
    print("🤖 Route to AI agent engineers")
else:
    print("💻 Route to basic software tier")
'''
Task 2 (Intermediate): Access Control Security Blacklist 🛑Create a list called 
banned_ip_addresses filled with 3 mock IP string coordinates. Create a variable 
called incoming_ip. Write a system that scans the list. If the incoming IP exists 
inside your banned list, print "🚨 ACCESS BLOCKED: Malicious client attempt registered.". 
Otherwise, print "🟢 Traffic Allowed."
'''
banned_ip_addresses = [9999, 0000]
incoming_ip = 0000
if incoming_ip in banned_ip_addresses:
    print("🚨 ACCESS BLOCKED: Malicious client attempt registered.")
else:
    print("🟢 Traffic Allowed.")
'''
Task 3 (Professional Challenge): Webhook Structural Validator 🎯Create a dictionary 
profile called lead_data containing keys like "name" and "company". Write a script that 
checks if the key "budget" exists inside the dictionary layout.If it is present, use an 
inner conditional expression one-liner to check if the budget value is greater than 3000 
to assign a category variable to "High Priority", else "Standard".If the key "budget" 
is missing entirely, inject the key into the dictionary layout with a default value of 
0 and print "⚠️ No budget provided, default initialized".
'''
lead_data = {"name":"Alice", "company": "Axaro"}
required_data = ["name", "company", "budget"]
if "budget" in lead_data:
    category = "High Priority" if lead_data["budget"] > 3000 else "Standard"
else:
    lead_data["budget"] = 0
    print("⚠️ No budget provided, default initialized")
print(lead_data)