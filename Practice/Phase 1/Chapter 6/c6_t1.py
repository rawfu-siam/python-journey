# t1
temperature = 35
if temperature > 30:
    print("It is hot outside!")
else:
    print("It is nice outside!")
# t2
student_mark = int(input("Enter your marks: "))
if student_mark < 0:
    print("Invalid score")
elif student_mark >= 90:
    print("Congrats! You got a Grade A!")
elif student_mark >= 70:
    print("Well done! You got Grade B!")
elif student_mark >= 40:
    print("You managed to secure Grade C!")
else:
    print("Sorry! You failed! Try next time!")
# t3
packet_size = 1500
server_online = True
if packet_size <= 2000 and server_online == True:
    print("Packet Transmitted")
else:
    print("Transmission Failed")
