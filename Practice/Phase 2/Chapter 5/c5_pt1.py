'''
Chapter5, topic - JSON handling
'''
'''
Task 1 (Easy) — The Chatbot User Profile Loader Goal: Create a function 
named load_user_profile that takes a parameter named raw_json_string. 
The function must convert that text string into a Python dictionary. 
It must return an f-string message stating: "User Account: [name] | 
Location: [city]".Action: Test it by passing a raw string containing 
double quotes: '{"name": "Tammy", "city": "Dhaka"}'. Print the 
returned welcome message text.
'''
import json
def load_user_profile(raw_json_string):
    json_dict = json.loads(raw_json_string)
    return f"User Account: [{json_dict['name']}] | Location: [{json_dict['city']}]"
raw_string1 = '{"name": "Tammy", "city": "Dhaka"}'
print(load_user_profile(raw_string1))
'''
Task 2 (Medium) — The Server Configuration Exporter Goal: Create a function 
named export_system_config that takes a dictionary parameter called 
config_dict. Inside, use json.dumps() with an indentation parameter value 
of 2 to convert the map into a formatted string. Return this formatted 
JSON text string. Action: Create a sample settings dictionary containing 
pairs like {"nodes": 5, "debug_mode": False}. Pass it into your function, 
print the final output string, and verify that the output formatting 
displays the parameters beautifully aligned.
'''
def export_system_config(config_dict):
    json_str = json.dumps(config_dict, indent=2)
    return json_str
sample_dict = {"nodes": 5, "debug_mode": False}
print(export_system_config(sample_dict))
'''
Task 3 (Bit Harder) — The Webhook Ledger Account Validator Goal: Create a 
function named process_crm_webhook that takes a raw JSON string package 
representing a single customer transaction row.Inside, decode the text 
into a working python dictionary safely.Check for a key named 
"contract_value". If the value is less than 5000, add an extra key-value 
pair to the dictionary named "account_tier": "Standard". If it is 5000 
or higher, add "account_tier": "Premium". Finally, convert this updated 
dictionary back into a pretty text string format using json.dumps(indent=4) 
and return it.Action: Test your pipeline function twice: first pass an 
input string '{"name": "Mozi", "contract_value": 2500}', and second pass 
'{"name": "AlphaTech", "contract_value": 12000}'. Print both returning 
text logs to watch the tier tag updates happen dynamically.
'''
def process_crm_webhook(raw_string_package):
    transaction = json.loads(raw_string_package)
    if transaction["contract_value"] < 5000:
        transaction["account_tier"] = "Standard"
    elif transaction["contract_value"] >= 5000:
        transaction["account_tier"] = "Premium"
    return json.dumps(transaction, indent=4)
web_hook1 = '{"name": "Mozi", "contract_value": 2500}'
web_hook2 = '{"name": "AlphaTech", "contract_value": 12000}'
print(process_crm_webhook(web_hook1))
print(process_crm_webhook(web_hook2))
