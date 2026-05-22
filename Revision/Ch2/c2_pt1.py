'''
Chapter2, topic - variable
'''
'''
Task 1 (Medium): Create a clean script file named 
c2_pt1.py inside your Chapter 2 directory. Create 
a variable called target_hours. Assign it the 
total number of hours of your study war block (3000). 
Print it out so it displays nicely using your sep=" : " token.
'''
target_hours = 3000
print("Total targeted hours", target_hours, sep=" : ")
'''
Task 2 (Hard): Inside the same file, create a variable 
called current_status and store the word "Level 35" 
inside it. On the next line, update/re-assign that exact 
same variable name to hold a new string: "Level 36". 
Print the final variable out to the screen.
'''
current_status = "Level 35"
current_status = "Level 36"
print(f"Current level of basic python is {current_status}")
'''
Task 3 (Professional Business Problem): Write a mock financial 
ledger setup. Import the math module. Create a variable called 
raw_valuation and set it to 499.05. Create a second variable 
called secured_valuation and set it to hold the value of your 
first variable rounded down using the correct math tool. 
Print the final secured box name with an end marker code.
'''
import math
raw_valuation = 499.05
secured_valuation = math.floor(raw_valuation)
print("Rounded valuation is ", secured_valuation, sep="$", end="" )
