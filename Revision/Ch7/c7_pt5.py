'''
Chapter6, topic - star pattern
'''
'''
Task 1 (Medium): The Corporate Banner Blueprint 📊Write an engine that 
prints a horizontal banner made of stars that is 3 rows tall and 7 columns 
wide. Use nested loops and ensure your output creates a perfect, neat 
rectangle box.
'''
for x in range(3):
    for y in range(7):
        print("*", end="")
    print()
'''
Task 2 (Intermediate): The Digital Access Staircase 🪜Write a nested loop pattern 
that outputs an increasing star pattern ladder, but using numbers instead of 
stars! The shape should look exactly like this:text
1 
1 2 
1 2 3 
1 2 3 4
Use code with caution.Hint: Instead of printing *, print the dynamic 
loop variable value of your inner column counter (remembering to handle 
range offsets)!
'''
for a in range(1,5):
    for b in range(1,a + 1):
        print(b, end=" ")
    print()
'''
Task 3 (Professional Challenge): Custom AI Optimization Funnel 📉Write a 
loop script that prints an inverted right triangle pattern that starts with 
5 stars on the top row, down to 4, 3, 2, and ends with exactly 1 star on 
the very bottom line. Use a step parameter sequence inside your range() function.
'''
for p in range(5,0,-1):
    for q in range(p):
        print("*", end=" ")
    print()
