'''
Chapter9, topic - try / except / else / finally
'''
'''
Task 1 (Easy): Write a full 4-block layout (try/except/else/finally). In your try block, 
calculate result = 5 + 5. Catch a TypeError. In your else block, print the result. In your 
finally block, print "Execution Complete". Run it to see how a perfect run behaves!
'''
try:
    calculate_result = 5 + 5
except TypeError:
    print("There is a type error!")
else:
    print(calculate_result)
finally:
    print("Execution Complete")
'''
Task 2 (Medium): Build a data-loading script structure. Create a variable filename = 
"client_list.txt". Try to open it in read mode. Catch the FileNotFoundError and print 
"Warning: Using temporary list instead". Use the else block to print "File read 
successfully". Use the finally block to print "System check complete".
'''
filename = None 
try:
    filename = open("client_list.txt", "r")
except FileNotFoundError:
    print("Warning: Using temporary list instead")
else:
    print("File read successfully")
finally:
    if filename:
        filename.close()
    print("System check complete")

'''
Task 3 (Upper-Medium Business Logic): Create an automated system check for a user profile. 
Ask the user to input their desired username. Inside the try block, convert their input to 
a string (which always works). Inside the else block, use an if/else statement to check if 
the username length is less than 4 characters. If it is too short, print a warning. No 
matter what, make sure your finally block runs and prints "Profile database sync finished".
'''
try:
    user_name = str(input("Please enter your username here: "))
except TypeError:
    print("Invalid user name.")
else:
    if len(user_name) < 4:
        print("The user name is too short. Please type a new one!")
    else:
        print(f"User name saved as {user_name}.")
finally:
    print("Profile database sync finished")
