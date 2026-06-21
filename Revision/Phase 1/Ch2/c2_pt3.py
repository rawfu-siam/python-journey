'''
Chapter2, topic - type() and typecasting
'''
'''
Task 1 (Medium): Create a new script file named c2_pt3.py. 
Create a variable containing a decimal number 75.85. 
Use type() to print out its data class. Below it, 
use typecasting to turn that decimal number into a 
clean, whole Integer, save it to a new box, and 
print that out.
'''
decimal_number = 75.85
print(type(decimal_number))
clean_number = int(decimal_number)
print(clean_number)
'''
Task 2 (Hard): Create a variable named raw_string_count 
and set it to hold the text string "3000". Convert that 
string variable into a real number, add a value of 50 
to it mathematically, and display the final result.
'''
raw_string_count = "3000"
actual_count = int(raw_string_count) + 50
print(actual_count)
'''
Task 3 (Professional Business Problem): Imagine you are 
receiving server status logs. Create a boolean variable 
called backup_status and set it to True. Convert this 
boolean variable directly into a String using the correct 
spell function. Print it out inside an f-string to look 
like an official system log line.
'''
backup_status = True
backup_status_string = str(backup_status)
print(f"Backup Status: {backup_status_string}")
