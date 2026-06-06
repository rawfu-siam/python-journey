# t1
japan_plan = open("my_goal.txt", "w")
japan_plan.write("I want to go to Japan to pursue my bachelors in CSE in 2027\n")
japan_plan.close()
# t2
adding = open("my_goal.txt", "a")
adding.write("Weekly 80 hours work challenge protocol active.")
adding.close()
read = open("my_goal.txt", "r")
print(read.read())
read.close()
# t3
tools = ["n8n", "Make.com", "LangChain"]
stack = open("stack.txt", "w")
for tool in tools:
    stack.write(f"{tool}\n")
stack.close()
read_stack = open("stack.txt", "r")
print(read_stack.read())
read_stack.close()
