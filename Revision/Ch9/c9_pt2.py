'''
Chapter9, topic - File I/O — with()
'''
'''
Task 1 (Medium): Secure Client Notes Generator 📝Write an automation script 
using a with statement in Write Mode to create a document named client_notes.txt.
Inside the indented safety zone, write a single corporate line: "Client Nexus 
requested an updated budget layout by tomorrow morning.\n".
'''
with open("client_notes.txt", "w") as note:
    note.write("Client Nexus requested an updated budget layout by tomorrow morning.\n")
'''
Task 2 (Intermediate): Secure Appending Profile Tracker Create a text file called 
blacklist.txt containing one initial string row: "192.168.1.1\n". Write a script wrapped 
inside a with statement in Append Mode that targets blacklist.txt and appends two new 
restricted IP address strings seamlessly on separate rows: "10.0.0.45\n" and "172.16.5.9\n".
'''
with open("blacklist.txt", "w") as a:
    a.write("192.168.1.1\n")

with open("blacklist.txt", "a") as b:
    b.write("10.0.0.45\n")
    b.write("172.16.5.9\n")
'''
Task 3 (Professional Challenge): Double-Vault Financial Migration System 📊First, 
create a source document text layout file called raw_revenue.txt containing these three rows:
Nexus_Corp,3500
Apex_Media,800
Zayn_Ops,5000
Write an optimization function called migrate_and_filter_revenue(). Use a single with 
statement line to open raw_revenue.txt in Read Mode and a new target file called 
high_value_vault.txt in Write Mode at the exact same time.
Loop stream through the source lines. If a company's revenue amount is greater than or 
equal to 2000, write a clean custom text summary string directly into your new 
high_value_vault.txt file!
'''
with open("raw_revenue.txt", "w") as r:
    r.write("Nexus_Corp,3500\n")
    r.write("Apex_Media,800\n")
    r.write("Zayn_Ops,5000\n")
def migrate_and_filter_revenue():
    with open("raw_revenue.txt", "r") as f1, open("high_value_vault.txt", "w") as f2:
        for lines in f1:
            clean_line = lines.strip()
            user_name, revenue_str = clean_line.split(",")
            revenue = int(revenue_str)
            if revenue >= 2000:
                f2.write(f"Revenue for {user_name} is ${revenue}\n")

migrate_and_filter_revenue()
