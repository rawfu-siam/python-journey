'''
Chapter2, topic - polymorphism
'''
'''
Task 1 (Easy): Create two unrelated classes: Laptop and Server. Give both 
of them a method named boot_up(self).Inside Laptop, it prints "Displaying 
lock screen window.". Inside Server, it prints "Mounting secure cloud 
database arrays.". Verification Parameter: Put both objects into a list 
array loop and call their .boot_up() method sequentially to trace the 
two distinct print statements.
'''
class Laptop:
    def boot_up(self):
        print("Displaying lock screen window.")
class Server:
    def boot_up(self):
        print("Mounting secure cloud database arrays.")
devices = [Laptop(), Server()]
for device in devices:
    device.boot_up()
'''
Task 2 (Medium): Create a base parent class called Notification. Give it a 
method send(self, user) that prints "Sending base alert to user". Create a 
child class called SMSNotification that overrides that exact method to 
print "📱 SMS Alert dispatched to [user]!". Verification Parameter: Test it 
by initializing an SMSNotification object instance and calling .send("Robin"). 
Confirm that the parent's message is blocked and only the custom phone 
alert prints.
'''
class Notification:
    def send(self, user):
        print(f"Sending base alert to {user}")
class SMSNotification(Notification):
    def send(self, user):
        print(f"📱 SMS Alert dispatched to {user}!")
noti = SMSNotification()
noti.send("Robin")
'''
Task 3 (Above Average): Let's build an automated file processor. Create a 
class called CSVFile with an __init__(self, filename) constructor and a 
method get_row_count(self) that returns the integer 150. Create a second 
independent class called JSONFile with an __init__(self, filename) 
constructor and a method get_row_count(self) that returns the integer 42. 
Write an independent polymorphic master function called log_file_size(file_obj). 
This function should look at the object, run .get_row_count(), and print: 
"File: [filename] contains [count] data records." Verification Parameter: 
Initialize CSVFile("leads.csv") and JSONFile("config.json"). Pass each one 
through your master log_file_size() function sequentially and verify the terminal 
formats the numbers and file names accurately.
'''
class CSVFile:
    def __init__(self, filename):
        self.filename = filename
    def get_row_count(self):
        return 150
class JSONFile:
    def __init__(self, filename):
        self.filename = filename
    def get_row_count(self):
        return 42
def log_file_size(file_obj):
    print(f"File: {file_obj.filename} contains {file_obj.get_row_count()} data records.")
file1 = CSVFile("leads.csv")
file2 = JSONFile("config.json")
log_file_size(file1)
log_file_size(file2)
