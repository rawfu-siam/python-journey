'''
Chapter9, topic - File I/O — modes
'''
'''
Task 1 (Medium): The Workspace Config Generator Write a script 
using with open() in Write Mode to create a text file called config.txt. 
Inside, save two lines of configuration data: "api_host=https://openai.com\n" 
and "max_tokens=2000\n". Confirm it saves correctly by opening your 
folder path to inspect it.
'''
with open("config.txt", 'w') as api_host:
    api_host.write("api_host=https://openai.com\n")
    api_host.write("max_tokens=2000\n")
'''
Task 2 (Intermediate): The Client Activity Stream Write an automation 
script that adds usernames onto an existing list file named active_users.txt. 
Open the file in Append Mode so it doesn't wipe out past logs. Add three 
names sequentially: "siam_dev\n", "alice_ai\n", and "zayn_ops\n". Run the 
script two times in a row, then open the file to see how it cleanly 
multiplies your list lines!
'''
with open("active_users.txt", "a") as users:
    users.write("siam_dev\n")
    users.write("alice_ai\n")
    users.write("zayn_ops\n")
'''
Task 3 (Professional Challenge): Corporate Expense Statement Summary Auditor 
First, build a text document called expenses.txt containing these three ledger 
data rows:
Server_Cloud,450,Paid
OpenAI_API,1200,Paid
Database_Node,150,Pending
Write a professional-grade audit function called audit_agency_expenses(). 
Have it open expenses.txt in Read Mode, read the contents line by line, 
calculate the total sum cost of all items that are marked as "Paid", and 
completely print out the final total dollar invoice cost!
'''
with open("expenses.txt", 'w') as expenses:
    expenses.write("Server_Cloud,450,Paid\n")
    expenses.write("OpenAI_API,1200,Paid\n")
    expenses.write("Database_Node,150,Pending\n")
def audit_agency_expenses():
    total_cost = 0
    with open("expenses.txt", 'r') as file:
        for line in file:
            clean_line = line.strip()

            item, costs_str, status = clean_line.split(",")
            costs = int(costs_str)
            if status == "Paid":
                total_cost += costs
    print(f"📊 Final Total Paid Invoice Cost: ${total_cost}")

audit_agency_expenses()
