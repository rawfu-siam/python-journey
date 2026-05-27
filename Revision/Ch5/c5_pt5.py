'''
Chapter5, topic - items(), keys(), values(), update(), get()
'''
'''
Task 1 (Medium): Create a dictionary variable named war_dashboard 
holding three key-value slots tracking your progress 
("rank", "level", "hours"). Run two separate print statements: 
one that displays only the keys using the correct method button, 
and one that displays only the values.
'''
war_dashboard = {"rank" : "Captain", "level" : 40, "hours": 100}
print(war_dashboard.keys())
print(war_dashboard.values())
'''
Task 2 (Hard): Inside the same script file, create a dictionary 
called infrastructure_node set to hold {"ip": "192.168.1.1", "status": 
"Offline"}. On the line below it, write a single command line that 
uses .update() to cleanly switch its status value to "Online" 
and append a brand-new integer key-value block: "port_channel":
8080. Print the complete updated dictionary container.
'''
infrastructure_node = {"ip": "192.168.1.1", "status": "Offline"}
new_updates = {"status": "Online", "port_channel":8080}
infrastructure_node.update(new_updates)
print(infrastructure_node)
'''
Task 3 (Professional Business Problem): Build an internal automated 
database key validation router block. Create a dictionary: 
client_record = {"id": 9084, "tag": "Axaro"}. Use the safe .get() 
method to hunt for a completely missing key label named 
"billing_address". Print out the response inside an f-string so the 
console log displays exactly like this without crashing: Safe lookup 
validation response: None.
'''
client_record = {"id": 9084, "tag": "Axaro"}
print(f"Safe lookup validation response: {client_record.get("billing_address")}")
profile = {"tag": "Siam"}
print(profile.keys())