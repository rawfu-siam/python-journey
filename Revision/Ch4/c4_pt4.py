'''
Chapter4, topic - f-string
'''
'''
Task 1 (Medium): Open your Chapter 4 directory workspace, create 
a script named c4_pt4.py. Create two variables: study_hours = 45 
and topic_name = "f-strings". Use an f-string to output a message 
that looks exactly like this: Session log: 45 hours logged 
exploring f-strings.
'''
study_hours = 45
topic_name = "f-strings"
print(f"Session log: {study_hours} logged exploring {topic_name}.")
'''
Task 2 (Hard): Write a script snippet that captures a whole integer 
number entry from a team developer using input(). Cast it to an 
Integer. Use a single f-string to display the entered value alongside 
a live mathematical slot showing that value multiplied by 100.
'''
the_number = int(input("Enter a number: "))
print(f"100 times of the number is {the_number*100}")
'''
Task 3 (Professional Business Problem): Build a corporate database 
connection check line. Create a string variable host_ip = "192.168.1.1" 
and a boolean switch status variable is_connected = True. 
Construct a single formatted f-string print line that logs 
the IP address and the connection state cleanly divided by 
a horizontal escape tab code (\t).
'''
host_ip = "192.168.1.1"
is_connected = True
print(f"IP\t :\t{host_ip}\nConnected:\t{is_connected}")
