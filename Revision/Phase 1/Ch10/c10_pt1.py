'''
Chapter9, topic - exception handling
'''
'''
Task 1 (Easy): Write a program that asks a user for their age using input(). 
Use a try/except block with ValueError to catch if they type their name instead of 
a number. If they make a mistake, print: "Please use digits only!"
'''
try:
    age = int(input("Please enter your age: "))
    print(f"Your current age is {age}.")
except ValueError:
    print("Please use digits only!")
'''
Task 2 (Medium): Create a list containing three items: items = ["Laptop", 
"Mouse", "Keyboard"]. Write a script that tries to print items[5]. Use except 
IndexError: to intercept the crash and print a clean message saying: "That 
item index does not exist in our inventory!"
'''
items = ["Laptop", "Mouse", "Keyboard"]
try:
    print(items[5])
except IndexError:
    print("That item index does not exist in our inventory!")
'''
Task 3 (Upper-Medium Business Logic): Write a mini bank-withdrawal script. 
Initialize a variable balance = 500. Ask the user how much money they want to 
withdraw. Use exception handling to catch if they input invalid text, but also 
use an else block to deduct the money from balance and print the new balance 
only if their input was a valid number!
'''
balance = 500
try:
    withdraw_amount = int(input("Please enter the amount: "))
    if withdraw_amount > balance:
        print("Transaction Denied: Insufficient funds!")
    elif withdraw_amount <= 0:
        print("Transaction Denied: Amount must be greater than zero.")
    else:
        balance -= withdraw_amount
        print(f"Success! Your remaining balance is ${balance}.")
except ValueError:
    print("Format Error: Please enter a valid numerical digit.")
