'''
Chapter1, topic - list comprehension
'''
'''
Task 1 (Easy) — The Micro-Agency Pricing ScaleGoal: Your agency wants to scale 
up a baseline list of subscription prices by adding $15 to each package tier.
Input list: base_prices = [20, 50, 99, 150] Action: Use list comprehension to 
create a list called inflated_prices with 15 added to each entry.
'''
base_prices = [20, 50, 99, 150]
inflated_prices = [price + 15 for price in base_prices]
print(inflated_prices)
'''
Task 2 (Medium) — The Email Domain ScrubberGoal: Filter a raw list of lead 
communication logs to isolate internal system developer emails that belong 
specifically to your domain agency.com. Input list: inbound_emails = 
["user1@gmail.com", "siam@agency.com", "client@yahoo.com", "dev@agency.com"]
Action: Use list comprehension with an if conditional rule to extract only 
emails that end with "@agency.com".
'''
inbound_emails = ["user1@gmail.com", "siam@agency.com", "client@yahoo.com", "dev@agency.com"]
my_domain = [email for email in inbound_emails if email.endswith("@agency.com")]
print(my_domain)
'''
Task 3 (Bit Harder) — The High-Value Client ID ProcessorGoal: Isolate and 
premium-tag high-value enterprise accounts from an incoming list of client 
budgets.Input list: client_budgets = [1200, 6000, 450, 9000, 3100] Action: 
Use list comprehension with an if conditional filter to find all budgets 
greater than 3000. For those premium budgets, turn them into formatted 
strings that read: "VIP-$[Value]". (e.g. your final list should look like 
['VIP-$6000', ... ]).
'''
client_budgets = [1200, 6000, 450, 9000, 3100]
vip_client_budgets = [f"VIP-${budget}" for budget in client_budgets if budget>3000]
print(vip_client_budgets)
