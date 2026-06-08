'''
Chapter1, topic - global keyword
'''
'''
Task 1 (Easy) — The Agency Deal RegisterGoal: Create a global variable called 
total_deals set to 0. Write a function called win_new_deal() that uses the 
global keyword to increase total_deals by 1 every time it is called.Test Call: 
Call it twice and print total_deals. It should output 2.
'''
total_deals = 0
def win_new_deal():
    global total_deals 
    total_deals += 1
win_new_deal()
win_new_deal()
print(total_deals)
'''
Task 2 (Medium) — The Client Lead GatekeeperGoal: Create a global variable called 
system_mode set to "STANDARD". Write a function called upgrade_system_tier() that 
changes that exact global variable to "ENTERPRISE".Action: Print the mode before 
and after calling your function to verify the permanent change.
'''
system_mode = "STANDARD"
def upgrade_system_tier():
    global system_mode
    system_mode = "ENTERPRISE"
print(system_mode)
upgrade_system_tier()
print(system_mode)
'''
Task 3 (Bit Harder) — The Automated BDT Arbitrage SafeGoal: Create a global variable 
called bdt_vault_balance initialized to 50000. Write a function called 
inject_usd_earnings(usd_amount).The function must convert the usd_amount to BDT 
using our standard arbitrage rate (1 USD = 117 BDT).It must use the global keyword 
to add that converted BDT total directly to the bdt_vault_balance.Test Call: 
Call inject_usd_earnings(200) and print out the final global bdt_vault_balance. 
It should output 73400.
'''
bdt_vault_balance = 50000
def inject_usd_earnings(usd_amount):
    global bdt_vault_balance
    bdt_vault_balance += (usd_amount*117)
inject_usd_earnings(200)
print(bdt_vault_balance)
