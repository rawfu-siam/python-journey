'''
Chapter5, topic - add(), remove(), discard(), pop(), union(), intersection(), difference()
'''
'''
Task 1 (Medium): Create a set variable called 
active_skills = {"Logic", "Loops"}. Use the correct method button to 
add "Structures" straight into the set. On the line right below it, 
use .discard() to safely delete a non-existent word "Bugs". Print 
the final set.
'''
active_skills = {"Logic", "Loops"} 
active_skills.add("Structures")
active_skills.discard("Bugs")
print(active_skills)
'''
Task 2 (Hard): Inside the same file, create two separate sets tracking 
project numbers: group_1 = {10, 20, 30} and group_2 = {20, 30, 40}.
Run two print statements: one that calculates and prints the union of 
both groups into a single unified set, and one that calculates and prints 
the intersection showing only matching numbers.
'''
group_1 = {10, 20, 30}
group_2 = {20, 30, 40}
all_together = group_1.union(group_2)
common_only = group_1.intersection(group_2)
print(all_together)
print(common_only)
'''
Task 3 (Professional Business Problem): Build an internal automated 
audit compliance filter block. Create a set variable tracking all 
system required packages: required_tech = {"Python", "Docker", "n8n", "SQL"}.
Create a second set variable tracking what a student has mastered: 
mastered_tech = {"Python", "n8n"}. Use the correct mathematical set 
method to calculate exactly which required items are still missing 
from the student's portfolio layout. Print the final sub-set inside 
a clean f-string label block.
'''
required_tech = {"Python", "Docker", "n8n", "SQL"}
mastered_tech = {"Python", "n8n"}
remaining_tech = required_tech.difference(mastered_tech)
print(f"Items missing: {remaining_tech}")
