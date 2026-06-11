'''
Chapter2, topic - getters and setters
'''
'''
Task 1 (Easy) — The Security Badge Scanner 📛Goal: Create a SecurityBadge 
class where __init__ takes an ID number and passes it to set_badge_id().
Logic: Create a getter get_badge_id() and a setter set_badge_id(). The 
setter must check if the length of the ID string is less than 4 characters. 
If it is, print: "Invalid Badge Number". If it passes, save it inside 
self._badge_id. Action: Create a badge with "12". Verify it prints an error. 
Create one with "9987" and fetch it via your getter.
'''
class SecurityBadge:
    def __init__(self, id_number):
        self.set_badge_id(id_number)
    def get_badge_id(self):
        return self._badge_id
    def set_badge_id(self, new_id):
        if len(new_id) < 4:
            print("Invalid Badge Number")
            self._badge_id = None
        else:
            self._badge_id = new_id
id1 = SecurityBadge("12")

id2 = SecurityBadge("9987")
print(id2.get_badge_id())
'''
Task 2 (Medium) — The Server Temperature Monitor Goal: Create a ServerNode 
class where _temperature is set to 40 by default.Logic: Create a getter 
get_temperature() that returns the integer. Create a setter set_temperature(). 
If the incoming temperature value is greater than 80, print: "🛑 CRITICAL 
WARNING: Server Overheating! Shutting down fans." and do not save the value. 
Otherwise, update it.Action: Instantiate a server node. Use your setter to 
set it to 50, then try setting it to 95. Print the current temperature to 
ensure 95 was rejected.
'''
class ServerNode:
    def __init__(self):
        self._temperature = 40
    def get_temperature(self):
        return self._temperature
    def set_temperature(self, value):
        if value > 80:
            print("🛑 CRITICAL WARNING: Server Overheating! Shutting down fans.")
        else:
            self._temperature = value
temp1 = ServerNode()
temp1.set_temperature(50)
temp1.set_temperature(95)
print(temp1.get_temperature())
'''
Task 3 (Bit Harder) — The B2B Client Balance Lock 💼Goal: Create an AgencyInvoice 
class where __init__ assigns a business name and passes a financial total to 
set_bdt_balance().Logic: Create a getter get_bdt_balance(). Create a setter 
set_bdt_balance(). The setter must reject the value with an error message if 
someone tries to increase the debt balance by passing a value less than the 
current balance (meaning they are trying to magically erase their invoice history).
Action: Instantiate an invoice for "AlphaTech" with 50000 BDT. Run your setter to 
change it to 30000. Verify the reduction is blocked. Run the setter to change it 
to 65000 and verify it updates successfully.
'''
class AgencyInvoice:
    def __init__(self, name, total):
        self.name = name
        self._bdt_balance = 0
        self.set_bdt_balance(total)
    def get_bdt_balance(self):
        return self._bdt_balance
    def set_bdt_balance(self, value):
        if value < self._bdt_balance:
            print("Error! Cannot reduce balance.")
        else:
            self._bdt_balance = value
invoice1 = AgencyInvoice("AlphaTech", 50000)
invoice1.set_bdt_balance(30000)
print(f"Balance after trying 30000: {invoice1.get_bdt_balance()}")
invoice1.set_bdt_balance(65000)
print(f"Balance after trying 65000: {invoice1.get_bdt_balance()}")
