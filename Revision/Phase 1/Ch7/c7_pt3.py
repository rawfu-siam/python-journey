'''
Chapter7, topic - break / continue / pass
'''
'''
Task 1 (Medium): The Shopping Cart Item Skipper 🛒Create a list 
called shopping_items containing strings: "Milk", "BANNED_ITEM", 
"Eggs", and "Bread". Write a for loop to print "Processing item: 
X". If the loop hits "BANNED_ITEM", use the continue keyword to 
skip it instantly so it never prints.
'''
shopping_items = ["Milk", "BANNED_ITEM", "Eggs", "Bread"]
for item in shopping_items:
    if item == "BANNED_ITEM":
        continue
    print(item)
'''
Task 2 (Intermediate): Database User Count Limit 🔢Write a for 
loop that iterates through the numbers 1 to 10 using range(). 
Print out "User account #X verified". However, if the count reaches 
exactly 6, use the break keyword to shut down the loop early, 
printing "🚨 Max registration limit reached!".
'''
for x in range(1,11):
    if x == 6:
        print("🚨 Max registration limit reached!")
        break
    print(f"User account #{x} verified")
'''
Task 3 (Professional Challenge): Autonomous Log Analytics Module 
📊Create a list of dictionaries called system_telemetry:
[{"node": "A1", "job": "render", "health": "good"}, 
{"node": "B2", "job": "crypto_mining", "health": "restricted"}, 
{"node": "C3", "job": "database_backup", "health": "good"}, 
{"node": "D4", "job": "ai_agent_run", "health": "critical"}]
Write a system optimization script to run through this telemetry 
data:If a node's health is "restricted", use pass because your 
team is still writing the code to handle it later. Let the script 
print "⚠️ Node restricted, skipping actions safely." underneath.
If a node's health status is "critical", trigger a clear warning 
log message and execute a hard break to protect the pipeline.For 
all other healthy nodes, print "🚀 Node [node_name] successfully
 processed job [job_type].".
'''
system_telemetry = [
    {"node": "A1", "job": "render",          "health": "good"       }, 
    {"node": "B2", "job": "crypto_mining",   "health": "restricted" }, 
    {"node": "C3", "job": "database_backup", "health": "good"       }, 
    {"node": "D4", "job": "ai_agent_run",    "health": "critical"   }]
for status in system_telemetry:
    if status["health"] == "restricted":
        print("⚠️ Node restricted, skipping actions safely.")
        pass
    if status["health"] == "critical":
        print(f"🚨Condition is critial for Node {status["node"]}!")
        break
    elif status["health"] == "good":
        print(f"🚀 Node {status["node"]} successfull yprocessed job {status["job"]}.")
