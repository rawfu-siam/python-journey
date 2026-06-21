'''
Chapter1, topic - keywords in python
'''
'''
Task 1 (Medium): Write a script that imports the keyword module.
Use its built-in list capability to print out the total number
of keywords Python currently has locked down using your
favorite string styling layout from our earlier lessons.
'''
import keyword
print("Total forbidden keywords", (len(keyword.kwlist)), sep=" -> ")
'''
Task 2 (Hard): Write a snippet that uses the keyword helper method
.iskeyword() to check two different words: "client" and "for". Print
out the True/False results on your screen to see which one is a forbidden word.
'''
print(keyword.iskeyword("client"))
print(keyword.iskeyword("for"))
'''
Task 3 (Professional Business Problem): Build a small mock configuration setup.
Create a variable called user_count and set it to 150. Write a functional logic
block using the if and else keywords to print "Upgrade Cloud Infrastructure Server!"
if the user count goes over 100.
'''
user_count = 150
if user_count >100:
    print("Upgrade Cloud Infrastructure Server")
else:
    print("User counter under range!")
