'''
Chapter2, topic - attribute and static method
'''
'''
Task 1 (Easy): Create a class called Course. Give it a Class Attribute named 
subject = "Python". Inside its constructor __init__, set up an instance attribute 
named student_name. Create one course instance object with a name, and 
print out both attributes cleanly.
'''
class Course:
    subject = "Python"
    def __init__(self, student_name):
        self.student_name = student_name
courseA = Course("Mozi")
print(courseA.subject)
print(courseA.student_name)
'''
Task 2 (Medium): Create an automation class called DataCleaner. Write a 
@staticmethod inside it called clean_text(raw_string). This method should take a 
messy text string input, strip out all external outer blank spaces, convert it 
entirely to lowercase, and return the cleaned text output. Test it without 
spinning up an instance object!
'''
class DataCleaner:
    @staticmethod
    def clean_text(raw_string):
        return raw_string.strip().lower()
print(DataCleaner.clean_text("  PYtHoN_iS_aWesOME    "))
'''
Task 3 (Above Average): Create a class called ServerNode. Add a Class Attribute 
tracking tracker called active_nodes = 0. Every time a new ServerNode instance 
is constructed, add 1 to the tracker variable. Create a special @staticmethod 
called check_capacity(node_count) that returns "OVERLOAD" if node_count is 
strictly greater than 2, else returns "SAFE". Build 3 node instances sequentially 
and verify the system counts them!
'''
class ServerNode:
    active_nodes = 0
    def __init__(self):
        ServerNode.active_nodes += 1
    @staticmethod
    def check_capacity(node_count):
            return "OVERLOAD" if node_count > 2 else "SAFE"

ServerNode()
ServerNode()
ServerNode()
status = ServerNode.check_capacity(ServerNode.active_nodes)
print(f"Active Nodes: {ServerNode.active_nodes} -> System Status: {status}")
