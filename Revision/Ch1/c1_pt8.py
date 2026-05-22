'''
Chapter1, topic - math, random and os modules
'''
'''
Task 1 (Medium): Create a clean script named c1_pt8.py. 
Import the math module. Write an execution line that 
rounds the number 84.12 up to the nearest whole integer 
using the correct tool. Print the output string using 
your clean sep=" -> " layout.
'''
import math
print("Rounding number 84.12", math.floor(84.12), sep=" -> ")
'''
Task 2 (Hard): Inside your script, use the from random import ... 
style to unpack only the randint tool. Generate a random integer 
between 1000 and 9999 (simulating an automated bank transaction 
ID code). Print it so it looks exactly like this on your screen: 
Transaction ID Code: [Your Random Number Number].
'''
from random import randint
id_code = randint(1000,9999)
print(f"Transaction ID Code: {id_code}")
'''
Task 3 (Professional Business Problem): Write an administrative 
status pipeline line. Import the os module. Write a single-line 
comment labeling your step. Then, write a single print() statement 
that displays your operating system's current working directory 
folder location (os.getcwd()) and make sure the printed line ends 
with an official secure tag using end=" [DIRECTORY_SECURED]\n".
'''
import os
# displaying my operating system's current working directory
print(os.getcwd(), end=" [DIRECTORY_SECURED]\n")
 