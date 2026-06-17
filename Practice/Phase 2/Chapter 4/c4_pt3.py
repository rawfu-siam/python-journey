'''
Chapter4, topic - typing module
'''
'''
Task 1 (Easy) — The Simple String Score Stream Goal: Create a function 
named print_scores that takes a parameter named names_list. Use the 
typing module to explicitly hint that names_list must be a list 
containing nothing but text strings (List[str]). The function should 
use a loop to print "Player Name: [name]" for each item, and use 
arrow notation to show it returns None.Action: Test it by passing a 
list containing your favorite names, like ["Mozi", "Martin", "Tammy"].
'''
from typing import List
def print_scores(names_list: List[str]) -> None:
    for name in names_list:
        print(f"Player Name: [{name}]")
teamA = ["Mozi", "Martin", "Tammy"]
print_scores(teamA)
'''
Task 2 (Medium) — The Agency Server Price Configurator Goal: Create a 
function named summarize_server_costs that takes a parameter named 
cost_map. Use the typing module to explicitly hint that cost_map must 
be a dictionary where the keys are strings and the values are integers 
(Dict[str, int]). The function must return an integer (int) calculation 
representing the total sum of all costs combined (sum(cost_map.values())).
Action: Create a typed dictionary containing database rows like 
{"OpenAI_API": 400, "Server_Hosting": 150}. Pass it into your function 
and print the final returned sum to verify it equals 550.
'''
from typing import Dict
def summarize_server_costs(cost_map: Dict[str, int]) -> int:
    total_sum = sum(cost_map.values())
    return total_sum
database1 = {"OpenAI_API": 400, "Server_Hosting": 150}
print(summarize_server_costs(database1))
'''
Task 3 (Bit Harder) — The Webhook Mixed Profile Inspector Goal: Create 
a function named inspect_user_payload that takes a parameter named 
user_packet. Use the typing module to declare that user_packet is a 
dictionary with string keys, but its values can be absolutely any 
mixed data type whatsoever (Dict[str, Any]). The function must return 
a string (str) value.Inside, look for a key named "status". If the 
status value matches "VIP", return "Priority Route Cleared".Otherwise, 
return "Standard Route Assigned". Action: Test your inspector function 
twice: first pass a payload dictionary containing {"name": "Martin", 
"status": "VIP"} and second pass a payload containing 
{"name": "Anon", "status": "guest"}. Print both returns to confirm 
the conditional router evaluates the mixed profiles accurately.
'''
from typing import Any, Dict
def inspect_user_payload(user_packet: Dict[str, Any]) -> str:
    if user_packet["status"] == "VIP":
        return "Priority Route Cleared"
    else:
        return "Standard Route Assigned"
payload1 = {"name": "Martin", "status": "VIP"}
payload2 = {"name": "Anon", "status": "guest"}
print(inspect_user_payload(payload1))
print(inspect_user_payload(payload2))
