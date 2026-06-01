'''
Chapter10, topic - oop
'''
'''
Task 1 (Easy): Create a class named Laptop. Give it two attributes: 
brand = "Generic" and ram = 8. Create a method inside called show_specs(self) 
that prints out: "This laptop is a [brand] with [ram]GB RAM." Create an 
actual object from it, change the brand to match your current PC, and run 
the method.
'''
class Laptop:
    brand = "Generic"
    ram = 8
    def show_specs(self):
        print(f"This laptop is a {self.brand} with {self.ram}GB RAM.")
laptop1 = Laptop()
laptop1.brand = "Lenovo"
laptop1.show_specs()
'''
Task 2 (Medium): Create a class named BankAccount. Give it two attributes: 
account_holder = "Unknown" and balance = 0. Create a method called 
deposit(self, amount) that adds that amount directly to self.balance and 
prints the new total. Create an object, name it after yourself, deposit $250, 
and watch your code update the asset data!
'''
class BankAccount:
    account_holder = "Unknown"
    balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
siam = BankAccount()
siam.deposit(250)
'''
Task 3 (Upper-Medium Business Logic): Create a class named LeadAgent to model 
an AI marketing tool. Give it attributes for agent_name and leads_found (start 
it at 0). Write a method called scrape_web(self). Every time this method is 
called, it should increase leads_found by 5 and print out how many total leads 
this specific agent has captured so far. Call the method three times in a row!
'''
class LeadAgent:
    agent_name = "lucas"
    leads_found = 0
    def scrape_web(self):
        self.leads_found += 5
        print(self.leads_found)
agent1 = LeadAgent()
agent1.scrape_web()
agent1.scrape_web()
agent1.scrape_web()
