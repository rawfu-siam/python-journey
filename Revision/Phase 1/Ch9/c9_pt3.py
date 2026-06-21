'''
Chapter9, topic - readlines()
'''
'''
Task 1 (Easy): Create a text file called friends.txt and write 3 
names in it (one per line). Use readlines() to read them and print 
the total number of friends in your list using Python's len() function.
'''
with open("friends.txt", "w") as friend:
    friend.write("Alice\n")
    friend.write("Jack\n")
    friend.write("Mike\n")
with open("friends.txt", "r") as f:
    friend_name = f.readlines()
print(friend_name)
print(len(friend_name))
'''
Task 2 (Medium): Write a script that reads your friends.txt file and 
prints each name out one by one with an exciting greeting like: "Hello,
[Name]! Welcome to the team!" (Make sure there are no weird empty 
lines caused by \n!)
'''
with open("friends.txt", "r") as file:
    name_list = (file.readlines())
    for name in name_list:
        unique_name = name.strip()
        print(f"Hello, {unique_name}! Welcome to the team!")
'''
📝 Task 3 (Upper-Medium Business Logic): Create a file called prices.txt 
with numbers on separate lines: 10, 20, 30. Read them using readlines(), 
convert them from strings to integers using int(), calculate their total 
sum, and print it out.
'''
with open("prices.txt", "w") as p:
    p.write("10\n")
    p.write("20\n")
    p.write("30\n")

total_sum = 0
with open("prices.txt", "r") as price:
    price_str = price.readlines()
    for cost in price_str:
        price_int = int(cost.strip())
        total_sum = total_sum + price_int
print(total_sum)
