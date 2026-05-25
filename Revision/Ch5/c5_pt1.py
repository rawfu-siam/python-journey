'''
Chapter5, topic - List - index and slicing
'''
'''
Task 1 (Medium): Create a variable called study_plan 
holding a list of three items: "Logic", "Loops", and "Structures". 
Print out the second item ("Loops") using its exact index address bracket.
'''
study_plan = ["Logic", "Loops", "Structures"]
print(study_plan[1])
'''
Task 2 (Hard): Inside the same file, create a variable called 
revenue_logs containing a list of four separate decimal float 
numbers tracking income values. Use list slicing to cut out the 
last two numbers of your list using a blank end shorthand, and 
print out the resulting sub-list.
'''
revenue_logs = [55.00, 70.50, 199.00, 149.99, 99.99]
print(revenue_logs[3:])
'''
Task 3 (Professional Business Problem): Build an automated system 
configuration manager script block. Create a variable: 
database_nodes = ["Node_1", "Node_2", "OFFLINE_NODE"]. Use the 
correct single index assignment bracket operation to replace 
the "OFFLINE_NODE" element string with a clean new string "Node_3". 
Print the final complete list on screen.
'''
database_nodes = ["Node_1", "Node_2", "OFFLINE_NODE"]
database_nodes[2] = "Node_3"
print(database_nodes)
