'''
Chapter1, topic - print(), sep=(), end=()
'''
'''
Task 1 (Medium): Write a code that prints your
three favorite foods, but uses a plus sign + as
the separator between them.
'''
print("Atomic Habits", "The Millionaire Fastlane", "Rich Dad Poor Dad", sep=" + ")
'''
Task 2 (Hard): Use three completely separate print()
 commands to output Loading, then Your, then Profile. 
 Make sure they all print out on one single line separated 
 by single hyphens like this: Loading-Your-Profile.
'''
print("Loading", end="-")
print("Your", end="-")
print("Profile")
'''
Task 3 (Professional Business Problem): Imagine you are 
building an AI invoice tracker. Print out a billing reference
 line containing a client name, their order ID number, 
 and total price. Separate them using a vertical bar line
| and end the line with an official checkmark string text like  [VALIDATED].
'''
print("client name", "order ID number", "total price", sep=" | ", end="[VALIDATED]")
