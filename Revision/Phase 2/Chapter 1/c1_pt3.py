'''
Chapter1, topic - enumerate function
'''
'''
Task 1 (Easy): You have a list of programming tasks to finish today: 
["Fix Login Bug", "Test OpenAI API Hook", "Deploy FastAPI Container"]. 
Use enumerate() with a loop to print them out as a clean, numbered 
checklist starting at 1.
'''
tasks = ["Fix Login Bug", "Test OpenAI API Hook", "Deploy FastAPI Container"]
for count, task in enumerate(tasks, start=1):
    print(f"Task no {count} is: {task}")
'''
Task 2 (Medium): A user fills out a text box on a web application with 
4 distinct sentences: ["Hello", "I need automation help", "My budget is 
small", "Thanks"]. Use enumerate() to iterate through the text entries. 
If the phrase "budget" is found inside a sentence string, print a 
warning string showing the exact index position number where 
it occurred!
'''
text_box = ["Hello", "I need automation help", "My budget is small", "Thanks"]
for count, chunk in enumerate(text_box):
    if "budget" in chunk:
        print(f"Warning! index no {count} contains the words 'budget'.")
'''
Task 3 (Above Average): You have two matching lists compiled from a client 
website: names = ["Alice", "Bob", "Charlie"] and roles = ["CEO", "Manager", 
"Intern"]. Use enumerate() to iterate through the first names list, track 
the item's position index, look up their corresponding title from the roles 
list, and print out a formatted company hierarchy log like: "Staff Member 1: 
Alice holds the position of CEO".
'''
names = ["Alice", "Bob", "Charlie"]
roles = ["CEO", "Manager", "Intern"]
for rank, name in enumerate(names):
    specified_roles = roles[rank]
    print(f"Staff Member {rank+1}: {name} holds the position of {specified_roles}")
