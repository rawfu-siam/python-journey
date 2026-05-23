'''
Chapter2, topic - the input() function
'''
'''
Task 1 (Medium): Create a new script file named c2_pt4.py. 
Write a line of code that asks the user to type their 
target country location (e.g., "Japan"). Save it into 
a variable named target_country, and then use an 
f-string to display the phrase: Migration destination 
path set to: [User's Country Input].
'''
target_country = input("Please enter your desired country name: ")
print(f"Migration destination path set to: [{target_country}]")
'''
Task 2 (Hard): Write a code segment that asks the user to 
type their current level as a whole number. Cast that 
input immediately into a real Integer. Add a mathematical 
calculation step that increases that number by exactly 
1 to represent a level up, and print out the 
final numeric result.
'''
current_level = int(input("Enter you current python level out of 100: "))
one_level_up = current_level + 1
print(f"After this topic, your level will be -> {one_level_up}")
'''
Task 3 (Professional Business Problem): Build an internal 
automated invoice tool. Ask a team developer to input an 
exact floating-point server hosting cost decimal 
(e.g., 299.40). Convert that input into a Float data 
type, round it completely down to the nearest whole 
number using the correct tool from your math module, 
and display the finalized bill balance.
'''
import math as m
exact_hosting_cost = float(input("Type the accurate server hosting cost: "))
rounded_cost = m.floor(exact_hosting_cost)
print(f"Final bill is: ${rounded_cost}")
