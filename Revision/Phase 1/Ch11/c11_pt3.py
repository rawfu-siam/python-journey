'''
Chapter11, topic - objects, attributes and methods
'''
'''
Task 1: The SaaS Subscription Tracker (Easy-Medium)Create a class named SaaSPlan.
Give it two default attributes: plan_name = "Basic" and price = 29. Write a method 
named upgrade_plan(self) that changes the plan_name to "Premium" and changes the 
price to 99.Instantiate the object, call the upgrade method, and print the 
new details.
'''
class SaaSPlan:
    plan_name = "Basic"
    price = 2

    def upgrade_plan(self):
        self.plan_name = "Premium"
        self.price = 99
        print(f"The price of {self.plan_name} pack is ${self.price}.")

plan1 = SaaSPlan()
plan1.upgrade_plan()
'''
Task 2: The E-commerce Checkout Counter (Medium)Create a class named InvoiceTotal.
Give it an attribute subtotal = 0.Write a method named add_item(self, item_price) 
that takes an input number and adds it directly to the subtotal state variable.
Write a method named apply_tax(self) that multiplies the subtotal by 1.05 (5% tax 
rate adjustment).Create an instance, add three separate product amounts, run the 
tax calculation method, and print the exact final amount.
'''
class InvoiceTotal:
    subtotal = 0

    def add_item(self, item_price):
        self.subtotal = self.subtotal + item_price
            
    def apply_tax(self):
        self.apply_tax = self.subtotal * 1.05
        print(f"Final amount to pay: ${self.apply_tax}")

shopping1 = InvoiceTotal()
shopping1.add_item(60)
shopping1.add_item(130)
shopping1.add_item(90)
shopping1.apply_tax()
'''
Task 3: The AI Agent Token Budget Monitor (Upper Medium)Create a class named 
AIAgentContainer.Give it an attribute token_budget = 5000.Write a method named 
execute_prompt(self, words_in_prompt). Inside this method, calculate tokens 
consumed by multiplying words_in_prompt by 2.Deduct the result from the token_budget 
attribute state.If the token_budget falls below 0, print a warning: "CRITICAL: 
API Token limits exhausted. Run execution halted."Simulate running multiple 
consecutive prompts until the system triggers the safety warning flag.
'''
class AIAgentContainer:
    token_budget = 5000

    def execute_prompt(self, words_in_prompt):
        self.token_consumed = words_in_prompt * 2
        self.token_budget = self.token_budget - self.token_consumed
        if self.token_budget <= 0:
            print("CRITICAL: API Token limits exhausted. Run execution halted.")
        else:
            print(f"Remaining token: {self.token_budget}")
agent1 = AIAgentContainer()
agent1.execute_prompt(255)
agent1.execute_prompt(500)
agent1.execute_prompt(1250)
agent1.execute_prompt(660)
