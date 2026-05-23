'''
Chapter2, topic - operators
'''
'''
Task 1 (Medium): Create a new script file named c3_pt1.py 
inside a new Chapter 3 directory. Ask the user to input 
any number using a clear prompt text. Convert it to an integer. 
Calculate that number raised to the power of 2 (squared) 
using the correct arithmetic operator token, and 
print the numerical answer.
'''
input_number = int(input("Enter any number: "))
print(input_number**2)
'''
Task 2 (Hard): Create a variable named completed_hours and 
initialize it to hold the integer 45. On the next line, 
update the variable using the correct shortcut assignment 
operator combo to add exactly 3 more hours to it. 
Print the updated variable box on the screen.
'''
completed_hours = 45
completed_hours += 3
print(completed_hours)
'''
Task 3 (Professional Business Problem): Build an internal 
automated audit gate script block. Create two boolean 
variables: has_passed_exam set to True, and has_paid_fees 
set to False. Create a third variable called is_eligible_for_japan 
that uses a Logical Operator to ensure a student can only 
be eligible if both values are True. Print the final 
eligibility status inside an f-string block.
'''
has_passed_exam = True
has_paid_fees = False
is_eligible_for_japan = has_passed_exam and has_paid_fees
print(f"Student is eligible for Japanese University: {is_eligible_for_japan}")
