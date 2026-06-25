'''
Chapter2, topic - operator overloading
'''
'''
Task 1 (Easy): Create a class named DataPacket. Its constructor initializes 
an instance attribute named size_gb. Overload the __add__ operator so that 
adding two DataPacket objects together sums up their sizes and returns a 
brand new DataPacket object.Verification Parameter: Initialize packet_1 = 
DataPacket(15) and packet_2 = DataPacket(30). Add them together 
(combined = packet_1 + packet_2) and print out combined.size_gb to 
confirm the value equals exactly 45.
'''
class DataPacket:
    def __init__(self, size_gb):
        self.size_gb = size_gb
    def __add__(self, other):
        total = self.size_gb + other.size_gb
        return DataPacket(total)
packet_1 = DataPacket(15) 
packet_2 = DataPacket(30)
combined = packet_1 + packet_2
print(combined.size_gb)
'''
Task 2 (Medium): Create an agency service class named ServicePackage 
containing an __init__(self, name, price) constructor. Overload the 
__gt__ (Greater Than) operator so that it compares the packages based 
entirely on their internal price variable numbers. Verification Parameter: 
Initialize basic_plan = ServicePackage("Basic", 200) and 
premium_plan = ServicePackage("Premium", 800). Run an if 
premium_plan > basic_plan: logical check and print "Premium is higher" 
if it evaluates to true. Verify the alert fires correctly.
'''
class ServicePackage:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __gt__(self, other):
        return self.price > other.price
basic_plan = ServicePackage("Basic", 200)
premium_plan = ServicePackage("Premium", 800)
if premium_plan > basic_plan:
    print("Premium is higher")
'''
Task 3 (Above Average): Let's build an automated task duration aggregator 
tracker. Create a class named AutomationTask containing an 
__init__(self, task_name, duration_minutes) constructor. Overload the 
__sub__ (Minus) operator so that subtracting one task from another computes 
the time difference. Your method should take the left-hand duration, 
subtract the right-hand duration, wrap that absolute numeric calculation 
inside an actual integer, and return that raw number calculation directly 
(not wrapped in a class).Verification Parameter: Initialize 
task_long = AutomationTask("WebScrape", 120) and 
task_short = AutomationTask("CleanData", 45). Execute 
time_saved = task_long - task_short. Verify that printing out time_saved 
outputs exactly the integer number value of 75.
'''
class AutomationTask:
    def __init__(self, task_name, duration_minutes):
        self.task_name = task_name
        self.duration_minutes = duration_minutes
    def __sub__(self, other):
        difference = self.duration_minutes - other.duration_minutes
        return difference
task_long = AutomationTask("WebScrape", 120) 
task_short = AutomationTask("CleanData", 45)
time_saved = task_long - task_short
print(time_saved)
