'''
Chapter5, topic - JSON handling
'''
'''
Task 1 (Easy): Agency Metrics Packager. Create a script that converts a 
structural python data layout into a universal string payload. Setup: 
Import the json module. Logic: Declare a dictionary named node_status 
containing three keys: "node_id" (int), "is_online" (bool), and "region" 
(str). Use json.dumps() to convert this dictionary into a flat JSON text 
string variable named packed_string and print it. Verification Parameter: 
Run your script directly and verify that your terminal outputs a single 
plain text line containing your data keys wrapped in universal lowercase 
JSON formats (e.g., true instead of True).
'''
import json
node_status = { 'node_id': 123, 'is_online': True, 'region': 'Tokyo'}
packed_string = json.dumps(node_status)
print(packed_string)
'''
Task 2 (Medium): Inbound Webhook Parser. Build an incoming text interpreter 
gateway function. Logic: Write a function named parse_webhook_data that 
accepts a single string argument named raw_json. The function must use 
json.loads() to convert that string back into a Python dictionary, extract 
the value stored inside a key named "event_id", and return that value as 
an integer (-> int). Verification Parameter: Initialize a string variable 
test_payload = '{"event_id": 8845, "status": "pending"}'. Run your script 
and verify that passing test_payload into parse_webhook_data and printing 
the result outputs exactly the isolated number value 8845.
'''
def parse_webhook_data(raw_json) -> int:
    py_dict = json.loads(raw_json)
    return py_dict["event_id"]
test_payload = '{"event_id": 8845, "status": "pending"}'
print(parse_webhook_data(test_payload))
'''
Task 3 (Above Average): Nested AI Payload Destructuring. Design a multi-layered 
extraction worker module that parses deep parameters cleanly. Logic: Write a 
function named extract_agent_model that accepts a JSON string argument named 
api_response. The string structure will mimic a nested layout: 
{"ai_config": {"model_name": "gpt-4o", "temperature": 0.5}}. Your function 
must decode the text, access the nested inner dictionary, and return the 
string value attached to the "model_name" key.Verification Parameter: Create 
a mock verification string reading: mock_json = '{"ai_config": {"model_name": 
"gpt-4o", "temperature": 0.5}}'. Execute your function using this parameter 
and verify that running a print command on the returned output displays 
exactly the isolated string value "gpt-4o".
'''
def extract_agent_model(api_response):
    decoded = json.loads(api_response)
    config = decoded["ai_config"]
    return config["model_name"]
mock_json = '{"ai_config": {"model_name": "gpt-4o", "temperature": 0.5}}'
print(extract_agent_model(mock_json))
