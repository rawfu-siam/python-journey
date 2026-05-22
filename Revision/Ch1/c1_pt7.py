'''
Chapter1, topic - import
'''
'''
Task 1 (Medium): Create a clean script named c1_pt7.py. 
Import the built-in module named sys. Write a single comment 
line describing what it does, and then write a clean print() 
line displaying sys.platform using a clean sep=" : " arrow 
string to show your computer's operating system type.
'''
import sys
# sys is python's built-in configuration module
print("Operating system type of this computer", sys.platform, sep=" : ")
'''
Task 2 (Hard): Inside your script, use the from ... import ... 
technique to bring only the pow (power) tool out of the built-in 
math library box. Use it to calculate what 2 raised to the 
power of 5 is (written as pow(2, 5)). Print the final result 
to the screen.
'''
from math import pow
print("2 raised to the power of 5 equals to", pow(2,5), sep=" : ")
'''
Task 3 (Professional Business Problem): Write a script layout 
that imports the system os module but renames its shortcut 
identifier token to system_engine using an assignment keyword. 
Use a single-line comment to mark your workflow, then execute 
its .getcwd() function within a structured print() statement 
that ends using your favorite custom end=" [SECURED]\n" 
string tracker tag.
'''
import os as system_engine
# execute workflow to rewrite current directory
print(system_engine.getcwd(), end=" [SECURED]\n")
