'''
Chapter5, topic - Set
'''
'''
Task 1 (Medium): Create a set variable called project_sectors containing 
four items, but intentionally duplicate two of them (e.g., 
{"CSE", "AI", "CSE", "AI"}). Write a single print() line displaying 
the set on screen to observe how Python reacts.
'''
project_sectors = {"CSE", "AI", "CSE", "AI"}
print(project_sectors)
print(type(project_sectors))
'''
Task 2 (Hard): Inside the same file, create a variable called raw_ports 
and store a List containing five duplicate-filled integers: 8080, 8080, 
443, 8080, 443. On the next line, typecast that list into a real unique 
set, store the result in a clean new box variable named secured_ports, 
and print the sanitized outcome.
'''
raw_ports = [8080, 8080, 443, 8080, 443]
secured_ports = set(raw_ports)
print(secured_ports)
'''
Task 3 (Professional Business Problem): Build an internal automated 
database gate check line. Create a completely empty Set container box 
using the correct functional blueprint notation. Then, write a single print 
statement that prints the data type classification of your empty box 
variable using the type() tool function inside a clean f-string display block.
'''
empty_set = set()
print(f"The data type classification of the empty box is: {type(empty_set)}")
