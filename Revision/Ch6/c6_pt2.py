'''
Chapter6, topic - Nested conditionals
'''
'''
Task 1 (Medium): Smart Home Security 🏠Create two variables: 
is_door_locked (Boolean) and motion_detected (Boolean). Write 
a nested structure. First check: Is the door locked? If it is 
locked, check the second gate: Is motion detected? If yes, 
print "🚨 ALARM BLARING! Call the police!". If no motion is 
detected, print "🔒 All safe inside.". If the door wasn't 
locked at the start, print "🔓 Door is wide open anyway."
'''
is_door_locked = True
motion_detected = True
if is_door_locked:
    if motion_detected:
        print("ALARM BLARING! Call the police!")
    else:
        print("All safe inside.")
else:
    print("Door is wide open anyway.")
'''
Task 2 (Intermediate): Bank ATM Cash Simulator 🏦Create three 
variables: entered_pin (Integer), correct_pin (Integer, make it 1234), 
and withdrawal_amount (Integer). Your bank account balance is $500.
First, check if entered_pin matches correct_pin.If it matches, check 
if withdrawal_amount is less than or equal to your balance ($500). 
If yes, print "💵 Dispensing cash!". If not enough money, print "❌ 
Insufficient balance."If the PIN was wrong at the very start, print 
"❌ WRONG PIN: Card locked."
'''
entered_pin = 1234
correct_pin = 1234
withdrawal_amount = 400
if entered_pin == correct_pin:
    if withdrawal_amount <= 500:
        print("Dispensing cash!")
    else:
        print("Insufficient balance.")
else:
    print("WRONG PIN: Card locked.")
'''
Task 3 (Professional Challenge): AI Automation Client Onboarding 📊
Create three variables: has_signed_contract (Boolean), project_type 
(String, can be "AI Automation" or "Web Scraper"), and client_budget 
(Integer).Write a nested conditional workflow that mimics an onboarding 
pipeline. If they haven't signed a contract, print "❌ Do nothing. 
Wait for signature.". If they have signed, check their project type. 
If it's "AI Automation", check if their budget is $3000 or more to print "
🚀 Setup premium n8n workspace.", otherwise print "📉 Route to basic 
template system.". Handle other cases safely!
'''
has_signed_contract = True
project_type = "AI Automation"
client_budget = 3000
if not has_signed_contract:
    print("Do nothing")
elif has_signed_contract:
    if project_type == "AI Automation":
        if client_budget >= 3000:
            print("Setup premium n8n workspace.")
        else:
            print("Route to basic template system.")
