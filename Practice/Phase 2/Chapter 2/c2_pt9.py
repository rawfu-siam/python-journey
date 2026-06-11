'''
Chapter2, topic - operator overloading
'''
'''
Task 1 (Easy) — The Simple Cloud Storage Merger Goal: Create a CloudDrive class 
where __init__ sets a storage size integer in self.gigabytes. Overload the __add__ 
operator so that adding two drives together returns a new CloudDrive containing 
their total storage combined. Action: Instantiate a drive with 15 GB and another 
with 25 GB. Add them together and print the resulting gigabytes to verify 
it equals 40.
'''
class CloudDrive:
    def __init__(self, gigabytes):
        self.gigabytes = gigabytes
    def __add__(self, other):
        total = self.gigabytes + other.gigabytes
        return CloudDrive(total)
drive1 = CloudDrive(15)
drive2 = CloudDrive(25)
total_drive = drive1 + drive2
print(total_drive.gigabytes)
'''
Task 2 (Medium) — The AI Agent Resource Pooler 🤖Goal: Create an AIAgent class 
where __init__ takes an agent name string and a task_count integer tracking their 
active automation backlog. Overload the less-than operator (__lt__(self, other)) 
to compare two agents. It must return True if the left agent has fewer active 
tasks than the right agent. Action: Create Agent 1 with 3 tasks, and Agent 2 with 
7 tasks. Run if agent1 < agent2: and print a confirmation message: "Agent 1 is 
free to take new client assignments!".
'''
class AIAgent:
    def __init__(self, name, task_count):
        self.name = name
        self.task_count = task_count
    def __lt__(self, other):
        return self.task_count < other.task_count
agent1 = AIAgent("Bot1", 3)
agent2 = AIAgent("Bot2", 7)
if agent1 < agent2:
    print("Agent 1 is free to take new client assignments!")
'''
Task 3 (Bit Harder) — The Smart Cart Item Deductor 🛒Goal: Create an InventoryBatch 
class tracking store components. __init__ maps item_name and quantity. Overload 
the subtraction operator (__sub__). If the item names do not match exactly, 
print an error: "Item mismatch error!" and return self. If they match, calculate 
the new reduced quantity. If it drops below 0, clamp it back to 0. Return a new 
InventoryBatch object with the remaining stock.Action: Instantiate a batch of 
"Microchips" with a quantity of 100. Subtract a batch of "Microchips" with a 
quantity of 40. Verify the outcome shows 60 units remaining.
'''
class InventoryBatch:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity
    def __sub__(self, other):
        if not self.item_name == other.item_name:
            print("Item mismatch error!")
            return self
        else:
            reduced_quantity = self.quantity - other.quantity
            if reduced_quantity < 0:
                reduced_quantity = 0
            
            return InventoryBatch(self.item_name, reduced_quantity)
batch1 = InventoryBatch("Microchips", 100)
batch2 = InventoryBatch("Microchips", 40)
remaining = batch1 - batch2
print(remaining.quantity)
