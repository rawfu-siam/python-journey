'''
Chapter4, topic - join() and format() methods
'''
'''
Task 1 (Medium): Create a clean script file named c4_pt7.py 
inside your Chapter 4 directory. Create a list grouping 
containing three text strings: "Python", "Basics", and 
"Revision". Use the .join() method to stitch them together 
cleanly separated by a space character string " ". 
Print the single combined string.
'''
text_strings = ["Python", "Basics", "Revision"]
print(" ".join(text_strings))
'''
Task 2 (Hard): Inside the same file, create a variable called 
status_flag set to "ACTIVE" and a whole integer variable 
port_channel = 8080. Write a text sentence string using the 
classic .format() template structure with index numbers 
({0} and {1}) to print a message that reads exactly like 
this: Channel 8080 status state is currently locked at ACTIVE.
'''
status_flag = "ACTIVE"
port_channel = 8080
together = "Channel {0} status state is currently locked at {1}."
print(together.format(port_channel, status_flag))
'''
Task 3 (Professional Business Problem): Build an internal 
automated deployment dashboard generator. Create a variable 
tracking an infrastructure directory path: folder_node = "root_nodes". 
Use an f-string or simple print statement containing a 
.join() method that squishes the text strings "SYS", "API", 
and "V1" together with an absolute arrow separator " -> " 
as the glue. Ensure the console prints the line clearly.
'''
folder_node = "root_nodes"
print(" -> ".join([folder_node,"SYS", "API", "V1"]))
