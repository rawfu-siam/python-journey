'''
Chapter11, topic - oop - class
'''
'''
Task 1 (Easy): Define a clean class named AutomatedTask. Give it a 
default attribute task_name = "System Check" and is_done = False. 
Write a method called complete_task(self) that sets is_done to True 
and prints: "[task_name] is now completed!". Instantiation an object, 
change its name, and call the method!
'''
class AutomatedTask:
    task_name = "System Check"
    is_done = False
    def complete_task(self):
        self.is_done = True
        print(f"{self.task_name} is now completed!")
task1 = AutomatedTask()
task1.task_name = "System Update"
task1.complete_task()
'''
Task 2 (Medium): Create a class named CRMContact. Give it default template 
attributes for client_name and deal_value = 0. Write an internal system 
function method called upgrade_deal(self, bonus) that increases deal_value 
by that bonus amount. Instantiate two different clients, give them different 
values, upgrade only one of them, and print both their profiles!
'''
class CRMContact:
    client_name = "Default name"
    deal_value = 0

    def upgrade_deal(self, bonus):
        self.deal_value += bonus
        print(f"The value of the deal for client - {self.client_name} is ${self.deal_value}.")
client1 = CRMContact()
client1.client_name = "Alice"
client1.deal_value = 500

client2 = CRMContact()
client2.client_name = "Bob"
client2.deal_value = 400

client1.upgrade_deal(100)
client2.upgrade_deal(0)
'''
Task 3 (Upper-Medium Business Logic): Create a class named AgencyPipeline. Set 
attributes for agency_name = "Nova Agency" and revenue = 1000. Write a method 
called close_deal(self, contract_price). This method should take the contract 
price, add it directly to self.revenue, calculate a 10% tax deduction allocation 
string internally, and print out the new net budget standing. Call it twice with 
different numbers!
'''
class AgencyPipeline:
    agency_name = "Nova Agency"
    revenue = 1000

    def close_deal(self, contract_price):
        self.revenue += contract_price
        print(f"The net budget for {self.agency_name} is ${self.revenue + (self.revenue * 0.1)}")

agency1 = AgencyPipeline()
agency1.close_deal(750)
agency1.close_deal(650)