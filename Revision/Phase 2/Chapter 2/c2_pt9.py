'''
Chapter2, topic - __str__ and __len__ (dunder methods)
'''
'''
Task 1 (Easy): Create a class named ServerLog. Its constructor initializes an 
instance attribute named status_code (an integer like 200 or 500). Implement 
the __str__ method so that it returns a clean text alert message layout string: 
"Server Node Log Alert: status_code". Verification Parameter: Initialize 
log = ServerLog(500). Run print(log) and verify that the printed string reads 
exactly "Server Node Log Alert: 500".
'''
class ServerLog:
    def __init__(self, status_code):
        self.status_code = status_code
    def __str__(self):
        return f"Server Node Log Alert: {self.status_code}"
log = ServerLog(500)
print(log)
'''
Task 2 (Medium): Create an automated database container class named LeadSheet. 
Its constructor initializes an empty internal storage array list named 
self.leads_list. Overload the __len__ method so that it returns the exact item 
count inside self.leads_list. Verification Parameter: Initialize 
sheet = LeadSheet(). Append two dictionary lead entities to its inner tracker 
array: sheet.leads_list.append({"name": "Alice"}) and 
sheet.leads_list.append({"name": "Bob"}). Execute print(len(sheet)) and 
verify the output returns exactly the integer number value of 2.
'''
class LeadSheet:
    def __init__(self):
        self.leads_list = []
    def __len__(self):
        return len(self.leads_list)
sheet = LeadSheet()
sheet.leads_list.append({"name": "Alice"})
sheet.leads_list.append({"name": "Bob"})
print(len(sheet))
'''
Task 3 (Above Average): Let's build a unified corporate repository tracker. 
Create a class named ProjectRepo containing an __init__(self, repo_name, files_list) 
constructor. Overload the __str__ method to return: "Repository: [repo_name]". 
Overload the __len__ method to return the count of files inside the files_list 
array. Verification Parameter: Initialize a test run using 
repo = ProjectRepo("AI_Automation_Agency", ["main.py", "utils.py", 
"requirements.txt", "DockerFile"]). Execute print(repo) followed directly by 
print(len(repo)). Verify the screen logs the repository name and outputs 
exactly the integer count of 4.
'''
class ProjectRepo:
    def __init__(self, repo_name, files_list):
        self.repo_name = repo_name
        self.files_list = files_list
    def __str__(self):
        return f"Repository: {self.repo_name}"
    def __len__(self):
        return len(self.files_list)
repo = ProjectRepo(
    "AI_Automation_Agency", 
    ["main.py", "utils.py", "requirements.txt", "DockerFile"]
)
print(repo)
print(len(repo))
