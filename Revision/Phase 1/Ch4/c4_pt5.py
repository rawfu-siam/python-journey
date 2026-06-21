'''
Chapter4, topic - lower(), len(), title() and capitalize()
'''
'''
Task 1 (Medium): Create a clean script named c4_pt5.py 
inside your Chapter 4 directory. Create a variable named 
user_message and set it to hold the string text 
"learning code is view as ibadah". Run a single 
print statement that uses .capitalize() to turn 
it into a correctly structured sentence.
'''
user_message = "learning code is view as ibadah"
print(user_message.capitalize())
'''
Task 2 (Hard): Create a variable named messy_client_name 
and ask a team member to enter their full name using 
input(). Take that input variable, transform it into a 
perfectly polished corporate layout using .title(), 
calculate the exact number of character spaces it 
consumes using len(), and print both details back 
out inside a single clean f-string line.
'''
messy_client_name = input("Please enter you full name: ")
clean_name = messy_client_name.title()
print(f"Total no of characters in '{clean_name}' is {len(clean_name)}")
'''
Task 3 (Professional Business Problem): Build an internal 
network tag tracker line. Create a string tracking 
code: tag = "Cse-2027_ApRiL". Use your method tools 
to force the entire tracking code string down into 
completely lowercase letters (.lower()). Print the 
final results out so that the console display line 
looks exactly like this: Normalized server 
tag: cse-2027_april.
'''
tag = "Cse-2027_ApRiL"
tag = tag.lower()
print(f"Normalized server tag: {tag}.")
