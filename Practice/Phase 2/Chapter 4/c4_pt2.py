'''
Chapter4, topic - advanced type hints
'''
'''
Task 1 (Easy) — The Flexible Invoicing Balance Gate Goal: Create a function 
named format_balance_due that takes a parameter named balance. Use advanced 
pipe notation (|) to declare that balance can be an integer (int) OR a 
decimal float number (float). The function must return an f-string stating 
"Current Outstanding Balance: $[value]", formatting the number with two 
decimal places (:.2f).Action: Test your function twice: first pass the 
integer 5000 and second pass the decimal float 1250.75. Print both to 
verify the output formatting rules.
'''
def format_balance_due(balance: int | float) -> str:
    return f"Current Outstanding Balance: ${balance:.2f}"
print(format_balance_due(5000))
print(format_balance_due(1250.75))
'''
Task 2 (Medium) — The Hidden Customer Nickname Checker Goal: Create a 
function named get_profile_tag that takes a mandatory string parameter 
named real_name and an Optional string parameter named nickname (hinted 
as Optional[str] = None).If nickname is None, return the string: "User: 
[real_name]".If a nickname is passed, return the string: "User: 
[real_name] (aka [nickname])".Action: Run the function for "Martin" 
with no nickname, and run it for "Tammy" with the nickname "DevQueen". 
Print both to verify the branching logic handles None securely.
'''
from typing import Optional
def get_profile_tag(real_name: str, nickname: Optional[str] = None) -> str:
    if nickname is None:
        return f"User: [{real_name}]"
    else:
        return f"User: [{real_name} (aka [{nickname}])]"
profile1 = get_profile_tag("Martin")
profile2 = get_profile_tag("Tammy", "DevQueen")
print(profile1)
print(profile2)
'''
Task 3 (Bit Harder) — Strict Financial Vault Audit Goal: Create a function 
named audit_vault_transactions that takes a parameter named amounts_list. 
Use nested type hints to explicitly state that amounts_list must be a list 
containing nothing but whole integers (list[int]). The function must use 
arrow notation to show it returns a Union structure that can be an integer 
(int) OR a string (str).Inside, calculate the sum of the list using sum
(amounts_list).If the total sum is greater than 100000, return the text 
string: "ALERT: Maximum Vault Limit Exceeded!".Otherwise, return the 
calculated integer sum directly.Action: Test it twice. First pass a 
list of safe values [5000, 20000, 15000]. Second pass a massive list 
[60000, 50000, 30000]. Print the results to watch the return data type 
swap dynamically.
'''
def audit_vault_transactions(amounts_list: list[int]) -> int | str:
    total_amount = sum(amounts_list)
    if total_amount > 100000:
        return "ALERT: Maximum Vault Limit Exceeded!"
    else:
        return total_amount
list1 = [5000, 20000, 15000]
list2 = [60000, 50000, 30000]
print(audit_vault_transactions(list1))
print(audit_vault_transactions(list2))
