'''
Chapter2, topic - @classmethod
'''
'''
Task 1 (Easy) — The Simple Space Broker FactoryGoal: Build a class 
named ServerNode with an __init__ constructor setting node_id. 
Add a @classmethod named from_raw_id(cls, raw_text) that takes a 
string, runs .strip() to clean empty spaces, and returns a fully 
built ServerNode instance object. Action: Execute 
ServerNode.from_raw_id("  NODE-99  ") and verify that printing 
the node_id outputs the clean, space-free text string.
'''
class ServerNode:
    def __init__(self, node_id):
        self.node_id = node_id
    @classmethod
    def from_raw_id(cls, raw_text):
        clean_text = raw_text.strip()
        return cls(clean_text)
new_node = ServerNode.from_raw_id("  NODE-99  ")
print(new_node.node_id)
'''
Task 2 (Medium) — The Automated App Tier SwitcherGoal: Create a class 
named AgencyPortal containing a Class Attribute string current_tier = 
"FREE".Add a @classmethod named upgrade_global_tier(cls) that 
automatically flips that shared class tier variable value string 
permanently to "PREMIUM".Action: Print the class attribute, fire 
your class method tool directly, and print the attribute score 
again to confirm the global system state mutation.
'''
class AgencyPortal:
    current_tier = "FREE"
    @classmethod
    def upgrade_global_tier(cls):
        cls.current_tier = "PREMIUM"
print(AgencyPortal.current_tier)
AgencyPortal.upgrade_global_tier()
print(AgencyPortal.current_tier)
'''
Task 3 (Bit Harder) — The Webhook Slash Payload Ingester EngineGoal: 
Construct an alternative constructor method that decodes webhook 
transaction line strings:Class Name: InvoiceRecord → __init__ constructor 
maps two instance variables: client_name and bdt_amount.Class Method: 
Build a @classmethod named from_slash_payload(cls, payload_string). 
This method must split an incoming payload text string string via 
slashes (/), clean any whitespace, format the name to capital letters 
(.upper()), and return a fully constructed, ready-to-run object instance.
Test Data Input Stream: "elon musk / 351000" Action: Ingest that test 
data line through your class method alternative constructor and display 
its internal variables on your terminal screen line.
'''
class InvoiceRecord:
    def __init__(self, client_name, bdt_amount):
        self.client_name = client_name
        self.bdt_amount = bdt_amount
    @classmethod
    def from_slash_payload(cls, payload_string):
        splitted = payload_string.split("/")
        client_name = splitted[0].strip().upper()
        bdt_amount = int(splitted[1])
        return cls(client_name, bdt_amount)
test_input = "elon musk / 351000"
invoice1 = InvoiceRecord.from_slash_payload(test_input)
print(invoice1.client_name)
print(invoice1.bdt_amount)
