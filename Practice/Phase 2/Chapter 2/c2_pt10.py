'''
Chapter2, topic - __str__ and __len__ (dunder methods)
'''
'''
Task 1 (Easy) — The Book Page Counter 📖Goal: Create a Book class where __init__ 
takes a title string and a total pages integer. Overload __str__ to return "Title: 
[Book Title]" and overload __len__ to return the total pages count number.Action: 
Instantiate a book titled "The Python Grind" with 350 pages. Print the book object 
and print its length to verify outputs.
'''
class Book:
    def __init__(self, title, total_page):
        self.title = title
        self.total_page = total_page
    def __str__(self):
        return f"Title: {self.title}"
    def __len__(self):
        return self.total_page
book1 = Book("The Python Grind", 350)
print(book1)
print(len(book1))
'''
Task 2 (Medium) — The Freelance Project Milestone Tracker Goal: Create a FreelanceProject 
class where __init__ maps a client name string and initializes an empty list inside 
self.milestones. Add a method named add_milestone(name). Overload __str__ to return 
a message containing the client name and how many milestones are completed. 
Overload __len__ to return the count of milestones.Action: Create a project for 
"Tokyo Tech Inc". Add two milestones: "Setup FastAPI" and "Configure Docker". 
Print the project object and print its length.
'''
class FreelanceProject:
    def __init__(self, client_name):
        self.client_name = client_name
        self.milestones = []
    def add_milestone(self, name):
        self.milestones.append(name)
    def __str__(self):
        return f"Client: {self.client_name} | total milestons completed: {len(self.milestones)}"
    def __len__(self):
        return len(self.milestones)
projectX = FreelanceProject("Tokyo Tech Inc")
projectX.add_milestone("Setup FastAPI")
projectX.add_milestone("Configure Docker")
print(projectX)
print(len(projectX))
'''
Task 3 (Bit Harder) — The Webhook Batch Safe Cleaner Goal: Create a WebhookBatch class 
where __init__ takes a list of dictionary lead payloads. Overload __len__ to return the 
total number of leads inside the list. Overload __str__ to run a loop or condition checking 
the data: if any lead payload dictionary inside the batch list is missing an "email" key, 
return "ALERT: Dirty Batch Detected!". If all leads have emails, return "Batch Clean: 
[Total Count] Leads Ready".Action: Create a batch with two entries: [{"name": "Siam", 
"email": "s@dev.com"}, {"name": "Anon"}] (the second one is missing an email!). Print 
the batch object to verify it catches the error. Then update the data to make it clean, 
and print again.
'''
class WebhookBatch:
    def __init__(self, lead_payloads):
        self.lead_payloads = lead_payloads
    def __len__(self):
        return len(self.lead_payloads)
    def __str__(self):
        for lead in self.lead_payloads:
            if "email" not in lead:
                return "ALERT: Dirty Batch Detected!"
        return f"Batch Clean: {len(self)} Leads Ready"
test_batch1 = [{"name": "Siam", "email": "s@dev.com"}, {"name": "Anon"}]
webhook1 = WebhookBatch(test_batch1)
print(webhook1)
test_batch2 = [{"name": "Siam", "email": "s@dev.com"}, {"name": "Anon", "email": "a@dev.com"}]
webhook2 = WebhookBatch(test_batch2)
print(webhook2)
