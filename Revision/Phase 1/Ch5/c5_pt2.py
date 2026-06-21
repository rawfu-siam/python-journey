'''
Chapter5, topic - List - append(), sort(), reverse(), remove(), pop(), clear(), insert()
'''
'''
Task 1 (Medium): Open your Ch5 workspace directory, create a script 
named c5_pt2.py. Create a variable called skills = ["Logic", "Loops"]. 
Use the correct list method button to add the text string "Structures" 
straight onto the absolute end of your list. Print out the 
updated variable container.
'''
skills = ["Logic", "Loops"]
skills.append("Structures")
print(skills)
'''
Task 2 (Hard): Inside the same script, create a variable called 
scores = [35, 100, 45, 90]. Apply a list method that arranges those 
integers from smallest to largest automatically. On the line right 
below it, run a second list method that inserts the number 10 right 
into the absolute front of the list (index room 0). 
Print the final array.
'''
scores = [35, 100, 45, 90]
scores.sort()
scores.insert(0, 10)
print(scores)
'''
Task 3 (Professional Business Problem): Build an internal automated 
cloud server node manager. Create a variable: 
active_channels = ["CH_1", "BUG_NODE", "CH_2"]. 
Use a method command to delete "BUG_NODE" by its 
exact text name. On the next line, use .pop() with an empty bracket
to slice away the last channel remaining at the tail of your list. 
Print the final state of the list.
'''
active_channels = ["CH_1", "BUG_NODE", "CH_2"]
active_channels.remove("BUG_NODE")
active_channels.pop()
print(active_channels)
