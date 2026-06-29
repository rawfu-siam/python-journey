'''
Chapter3, topic - __name__ and __main__
'''
'''
Task 1 (Easy):Write a script where you declare a function named greet_user 
that returns "Welcome Elite Builder". Below it, implement an if 
__name__ == "__main__": guard statement block. Inside that protected block, 
execute the function and print its return value. Verification Parameter: 
Run your script directly and verify that your terminal outputs exactly 
"Welcome Elite Builder".
'''
def greet_user():
    return "Welcome Elite Builder"
if __name__ == "__main__":
    print(greet_user())
'''
Task 2 (Medium):Create a file layout module with a function named 
calculate_tax that takes an integer revenue amount and returns 
revenue * 0.15. Add a main execution gate switch that sets up a local 
verification check using a test variable value of 1000. Verification 
Parameter: If the script is executed directly, verify it uses print 
statements to display exactly: "Diagnostic Tax Value: 150.0".
'''
def calculate_tax(revenue):
    return revenue * 0.15
if __name__ == "__main__":
    test = calculate_tax(1000)
    print(f"Diagnostic Tax Value: {test}")
'''
Task 3 (Above Average):Design an agency database connection simulation 
script. It must contain a function named connect_db that returns 
"Database Active". Implement an explicit main() workflow function that 
calls connect_db and prints the status line. Protect your script 
architecture by routing your application startup command exclusively 
through an if __name__ == "__main__": condition line that calls main(). 
Verification Parameter: Confirm that direct execution starts the 
network flow perfectly, but importing the module into another file 
keeps it entirely silent.
'''
def connect_db():
    return "Database Active"
def main():
    print(connect_db())
if __name__ == "__main__":
    main()
# Did the other testing by importing it 