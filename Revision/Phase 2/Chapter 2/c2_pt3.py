'''
Chapter2, topic - super() method
'''
'''
Task 1 (Easy): Create a parent class called Account with an __init__(self, username) 
constructor that saves the name string to self.username. Create a child class 
called PremiumAccount that inherits from Account. Its constructor should accept 
username and a tier_level string. Use super() to pass the username up correctly. 
Build an instance object and print both variables!
'''
class Account:
    def __init__(self, username):
        self.username = username
class PremiumAccount(Account):
    def __init__(self, username, tier_level):
        super().__init__(username)
        self.tier_level = tier_level
acc1 = PremiumAccount("Max", 5)
print(acc1.username)
print(acc1.tier_level)
'''
Task 2 (Medium): Create an automation base worker class called DataPipe. Give it a 
plain method inside called process(self) that prints "[PIPE]: Scrubbing raw formatting 
layout...". Create a child class called AIPipe that overrides that exact process(self) 
method. Use super() to ensure the parent's scrubbing message prints first, and then 
follow it with a brand new custom print statement saying: "[AI]: Feeding cleaned 
text rows into LLM engine!".
'''
class DataPipe:
    def process(self):
        print("[PIPE]: Scrubbing raw formatting layout...")
class AIPipe(DataPipe):
    def process(self):
        super().process()
        print("[AI]: Feeding cleaned text rows into LLM engine!")
test_pipe = AIPipe()
test_pipe.process()
'''
Task 3 (Above Average): Let's build an agency invoicing system tracking state 
inheritance. Create a parent class called BaseInvoice with an __init__(self, 
client_name, amount) constructor that initializes those variables. Create a child 
class called TaxedInvoice that inherits from it and accepts client_name, amount, 
and a tax_rate float. Use super() to initialize the parent's data. Then, add a 
method inside the child called get_final_total(self) that multiplies the inherited 
amount attribute variable by the child's tax_rate and returns the final calculated 
result number!
'''
class BaseInvoice:
    def __init__(self, client_name, amount):
        self.client_name = client_name
        self.amount = amount
class TaxedInvoice(BaseInvoice):
    def __init__(self, client_name, amount, tax_rate:float):
        super().__init__(client_name, amount)
        self.tax_rate = tax_rate
    def get_final_total(self):
        final_result = self.amount * self.tax_rate
        return final_result
invoiceA = TaxedInvoice("AI_Automations_LLC", 5000, 1.15)
print(invoiceA.get_final_total())
