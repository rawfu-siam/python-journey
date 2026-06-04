'''
Chapter11, topic - __init__ and self
'''
'''
Task 1: The Digital Wallet Setup (Easy-Medium) Create a class named DigitalWallet.
Use an __init__ method that requires one input parameter when the object is created: 
owner_name.Inside __init__, set self.owner_name = owner_name and initialize a 
default balance variable: self.balance = 0.Write a method named display_balance(self) 
that prints: "Wallet Owner: [name] | Current Funds: $[balance]".Create an instance 
for yourself, call the display method, and verify your output matches your 
initialization data.
'''
class DigitalWallet:
    def __init__(self,owner_name):
        self.owner_name = owner_name 
        self.balance = 0
    
    def display_balance(self):
        print(f"Wallet Owner: {self.owner_name} | Current Funds: ${self.balance}")
owner1 = DigitalWallet("Alex")
owner1.display_balance()
'''
 Task 2: The Retainer Upgrade Module (Medium)Create a class named AgencyContract.
 Write an __init__ method that accepts two parameters: company and monthly_retainer. 
 Map them using self..Write a method named apply_bonus(self, bonus_amount) that 
 adds that incoming parameter value directly to your existing self.monthly_retainer 
 amount.Instantiate an object with a base fee of 3000. Run your bonus method with 
 a value of 1500, then print the updated contract balance attribute directly.
'''
class AgencyContract:
    def __init__(self,company,monthly_retainer):
        self.company = company
        self.monthly_retainer = monthly_retainer
    def apply_bonus(self, bonus_amount):
        self.monthly_retainer += bonus_amount
        print(f"Updatede contract balance for {self.company} is ${self.monthly_retainer}")

company1 = AgencyContract("TB Limited", 3000)
company1.apply_bonus(1500)
'''
Task 3: The API Request Limit Watchdog (Upper Medium)Create a class named ApiWatchdog.
Inside __init__, accept an api_name string. Also, hardcode a default attribute variable 
named self.requests_remaining = 3.Write a method named fire_call(self). Each time this 
method runs, check if self.requests_remaining is greater than 0. If it is, deduct 1 
from it and print: "[API CALL] Connection to [api_name] successful."If it is equal 
to 0, print instead: "[CRITICAL] Blocked! [api_name] limit reached. Status 429."Create 
an instance named openai_watchdog = ApiWatchdog("OpenAI GPT-4o"). Fire the call method 
4 consecutive times to force your logic engine to activate the rate-limit safety warning 
message.
'''        
class ApiWatchdog:
    def __init__(self, api_name):
        self.api_name = api_name
        self.requests_remaining = 3
    def fire_call(self):
        if self.requests_remaining > 0:
            self.requests_remaining -= 1
            print(f"[API CALL] Connection to {self.api_name} successful.")
        elif self.requests_remaining == 0:
            print(f"[CRITICAL] Blocked! {self.api_name} limit reached. Status 429.")

openai_watchdog = ApiWatchdog("OpenAI GPT-4o")
openai_watchdog.fire_call()
openai_watchdog.fire_call()
openai_watchdog.fire_call()
openai_watchdog.fire_call()
