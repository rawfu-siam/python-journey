'''
Chapter5, topic - Tuples — count(), index()
'''
'''
Task 1 (Medium): Create a clean script named c5_pt3.py 
inside your Chapter 5 directory. Create an immutable 
variable called fixed_targets holding a tuple of three 
items: "Math", "Theory", and "Coding". Print out the 
third item ("Coding") using standard index square brackets.
'''
fixed_targets = ("Math", "Theory", "Coding")
print(fixed_targets[2])
'''
Task 2 (Hard): Inside the same file, create a tuple variable 
named hourly_log containing these integer values: 10, 12, 10, 10, 8. 
Use the .count() method to find out exactly how many times the 
number 10 appears inside your frozen history. Print the answer 
using a clean f-string block.
'''
hourly_log = (10, 12, 10, 10, 8)
print(hourly_log.count(10))
'''
Task 3 (Professional Business Problem): Build an internal automated 
financial router. Create a frozen tuple tracking corporate target 
countries: destinations = ("UK", "US", "JP", "AU"). Use the correct 
method to find the exact index room number where the token string 
"JP" is locked away. Print out the final answer so it reads exactly 
like this: Target sector JP is located at station address: [Your Index Number].
'''
destinations = ("UK", "US", "JP", "AU")
index_jp = destinations.index("JP")
print(f"Target sector JP is located at station address: {index_jp}")
