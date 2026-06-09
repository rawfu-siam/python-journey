'''
Chapter2, topic - polymorphism
'''
'''
Task 1 (Easy) — The Automated Clean Screen ToolsGoal: Build two 
separate classes: Monitor and Smartphone.Give both classes a method 
named turn_on(). Monitor.turn_on() should return "Monitor screen 
glowing blue."Smartphone.turn_on() should return "Phone lockscreen 
loading display."Action: Instantiate an object of each, drop them 
into a python list, loop through them, and print their .turn_on() 
outputs.
'''
class Monitor:
    def turn_on(self):
        return "Monitor screen glowing blue."
class Smartphone:
    def turn_on(self):
        return "Phone lockscreen loading display."
device1 = Monitor()
device2 = Smartphone()
for dev in [device1, device2]:
    print(dev.turn_on())
'''
Task 2 (Medium) — The Multi-Platform Agency Notifier FleetGoal: Build an 
override polymorphic matrix using inheritance: Parent Class: BaseNotifier ->
method .send(msg) returns f"Base Alert: {msg}".Child Class: SlackBot-> 
overrides .send(msg) to return f"[SLACK] Broadcasting: {msg}".Child Class: 
DiscordBot -> overrides .send(msg) to return f"[DISCORD] 
Pinging: {msg}".Action: Create a list containing instances of all 3 classes. 
Loop through the list, execute .send("Server Connection Lost!") on each, 
and print the outputs.
'''
class BaseNotifier:
    def send(self, msg):
        return f"Base Alert: {msg}"
class SlackBot(BaseNotifier):
    def send(self, msg):
        return f"[SLACK] Broadcasting: {msg}"
class DiscordBot(BaseNotifier):
    def send(self, msg):
        return f"[DISCORD] Pinging: {msg}"
all_bot = [BaseNotifier(), SlackBot(), DiscordBot()]
for bot in all_bot:
    print(bot.send("Server Connection Lost!"))
'''
Task 3 (Bit Harder) — The Corporate Currency Conversion Ledger GatewayGoal: 
Build an enterprise accounting module utilizing a universal receiver 
function:Class A: USDBalance -> method .display_value(cash) returns 
f"${cash}".Class B: BDTBalance -> method .display_value(cash) returns 
f"৳{cash * 117}" (converts cash input on the fly).Standalone Function: 
Write a separate function called print_vault_status(balance_object, 
total_cash). Inside it, print balance_object.display_value(total_cash).
Action: Execute your standalone function twice: once passing a USDBalance 
object with 1000, and once passing a BDTBalance object with 1000.
'''
class USDBalance:
    def display_value(self, cash):
        return f"${cash}"
class BDTBalance:
    def display_value(self, cash):
        return f"৳{cash * 117}"
def print_vault_status(balance_object, total_cash):
    print(balance_object.display_value(total_cash))
print_vault_status(USDBalance(), 1000)
print_vault_status(BDTBalance(), 1000)
