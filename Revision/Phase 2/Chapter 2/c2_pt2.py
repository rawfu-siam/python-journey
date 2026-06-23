'''
Chapter2, topic - inheritance and types
'''
'''
Task 1 (Easy): Create a parent class called Tool. Give it a method inside 
called power_on(self) that prints "System online.". Create a child class 
called Scanner that inherits from Tool, and give it a unique custom method 
called scan_barcode(self) that prints "Reading data...". Build a scanner 
object and run both methods!
'''
class Tool:
    def power_on(self):
        print("System online.")
class Scanner(Tool):
    def scan_barcode(self):
        print("Reading data...")
scanner1 = Scanner()
scanner1.power_on()
scanner1.scan_barcode()
'''
Task 2 (Medium): Create a grand family tree structure using Multilevel Inheritance.
Grandparent Class: User (has attribute access_level = "Guest") Parent Class: 
Manager (inherits from User, overrides or adds access_level = "Staff")Child 
Class: Admin (inherits from Manager, overrides or adds access_level = "Superuser")
Create an Admin object instance and print out its final access_level attribute 
variable value to prove it inherited the youngest generation's settings!
'''
class User:
    access_level = "Guest"
class Manager(User):
    access_level = "Staff"
class Admin(Manager):
    access_level = "Superuser"
adminA = Admin()
print(adminA.access_level)
'''
Task 3 (Above Average): Let's build an agency automation fusion tool using 
Multiple Inheritance. Create a class called Logger with a method log_event(self) 
that prints "[LOG]: Task entry updated". Create a second independent class 
called NotionAPI with a method sync_database(self) that prints "[NOTION]: 
Canvas rows synced". Finally, create a child class called AutomationWorker 
that inherits from both Logger and NotionAPI. Give it an internal runner 
execution tool method called execute_task(self) that triggers both parent 
behaviors sequentially!
'''
class Logger:
    def log_event(self):
        print("[LOG]: Task entry updated")
class NotionAPI:
    def sync_database(self):
        print("[NOTION]: Canvas rows synced")
class AutomationWorker(Logger, NotionAPI):
    def execute_task(self):
        self.log_event()
        self.sync_database()
workerA = AutomationWorker()
workerA.execute_task()
