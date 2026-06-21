'''
Chapter2, topic - data types - string, integer, floating, boolean and none.
'''
'''
Task 1 (Medium): Create a clean script file named c2_pt2.py. 
Create two separate variable boxes. Store your current 
tracking rank description (e.g., "Python Basics") inside 
the first variable, and store your current level rank 
(e.g., 35) as a clean Integer inside the second variable. 
Print both items out onto one line with your custom 
sep=" | " parameter.
'''
current_rank = "Python Basics"
current_level = 35
print("Topic", current_rank, "Level", current_level, sep=" | ")
'''
Task 2 (Hard): Inside the same script file, create a variable 
called exact_progress_decimal and store the exact fraction 
float value 35.0 inside it. Below it, create a boolean 
variable called is_revision_complete and set it to False. 
Print out both values.
'''
exact_progress_decimal = 35.0
is_revision_complete = False
print(f"Revision complete : {is_revision_complete}")
print(f"Progress Update : {exact_progress_decimal}%")
'''
Task 3 (Professional Business Problem): Write a corporate 
workspace memory initialization script block. Create a 
placeholder variable box named client_signature_file and 
explicitly assign it the correct data type token that 
represents a completely empty value container. Use a 
single-line comment to describe your setup, and use a 
structured print command to show the initial state on 
screen with an end-anchor string tracker text.
'''
# initialize workspace variable with an explicit empty container 
client_signature_file = None
print(f"Initial stage: {client_signature_file}", end=" [TRACKER: INIT COMPLETE]")
