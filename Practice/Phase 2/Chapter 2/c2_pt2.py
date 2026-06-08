'''
Chapter2, topic - inheritance and types
'''
'''
Task 1 (Easy) — The Specialized Developer DeploymentGoal: Build a parent class 
named Employee that contains an __init__ constructor setting an instance variable 
name. Add a method inside it named work() that returns "System Task Processing...".
Action: Build a child class named AIEngineer that inherits from Employee. Create 
an instance of AIEngineer named "Bob", and print out his name along with the 
output of his inherited .work() method.
'''
class Employee:
    def __init__(self, name):
        self.name = name
    def work(self):
        return "System Task Processing..."
class AIEngineer(Employee):
    pass
engineer1 = AIEngineer("Bob")
print(engineer1.name)
print(engineer1.work())
'''
Task 2 (Medium) — The Cloud Matrix Asset Inventory (Multilevel)Goal: Build a 3-tier 
multilevel chain inheritance class matrix: Grandparent Class: Asset -> 
contains a class variable attribute category = "Digital".Parent Class: 
CloudInstance (inherits from Asset) -> contains a class variable 
attribute provider = "AWS".Child Class: ProductionContainer (inherits from 
CloudInstance) -> contains a custom method .get_specs() that 
returns a string displaying both inherited attributes. Action: Initialize a 
ProductionContainer object and call the .get_specs() method.
'''
class Asset:
    category = "Digital"
class CloudInstance(Asset):
    provider = "AWS"
class ProductionContainer(CloudInstance):
    def get_specs(self):
        return f"Category: {self.category} | Provider: {self.provider}"
container1 = ProductionContainer()
print(container1.get_specs())
'''
Task 3 (Bit Harder) — The Automated Omnichannel Broadcaster (Multiple Inheritance)
Goal: Construct an agency data engine using multiple inheritance: Parent Class A: 
SMSService -> contains a method named send_text(phone) that returns 
"SMS Piped to [phone]".Parent Class B: WhatsAppService -> contains 
a method named send_whatsapp(phone) that returns "WhatsApp Piped to [phone]".
Child Class: OmniChannelRouter (inherits from BOTH parents) -> contains a custom 
method named broadcast_to_client(phone_number) that calls both inherited methods
and prints their combined delivery confirmation outputs.
'''
class SMSService:
    def send_text(self, phone):
        return f"SMS Piped to {phone}"
class WhatsAppService:
    def send_whatsapp(self,phone):
        return f"WhatsApp Piped to {phone}"
class OmniChannelRouter(SMSService,WhatsAppService):
    def  broadcast_to_client(self,phone_number):
        sms_result = self.send_text(phone_number)
        whatsapp_result = self.send_whatsapp(phone_number)

        print(sms_result)
        print(whatsapp_result)

channel1 = OmniChannelRouter()
channel1.broadcast_to_client(889374483)
