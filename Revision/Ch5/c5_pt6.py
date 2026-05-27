'''
Chapter5, topic - Dictionary merge & update operators
'''
'''
Task 1 (Medium): Create a dictionary named study_war = 
{"hours": 45}. Create a second dictionary named booster = 
{"topic": "Merge_Operators"}. Use the | operator to merge them 
together into a new container called final_war_map, and print it.
'''
study_war = {"hours": 45}
booster = {"topic": "Merge_Operators"}
final_war_map = study_war | booster
print(final_war_map)
'''
Task 2 (Hard): Inside the same file, create a dictionary variable 
named cloud_node set to hold {"ip": "10.0.0.1", "status": "Maintenance"}. 
On the line below it, write a single command line that uses the |= operator 
shortcut to cleanly swap its status value to "Operational" and attach 
a brand-new integer key-value slot: "active_users": 150. Print the 
updated cloud_node box.
'''
cloud_node = {"ip": "10.0.0.1", "status": "Maintenance"}
cloud_node |= {"status": "Operational", "active_users": 150}
print(cloud_node)
'''
Task 3 (Professional Business Problem): Build an internal automated 
invoice tracker. Create a base dictionary tracking corporate client 
metrics: invoice_data = {"id": 1042, "cost": 299.99}. Use a single-line 
comment to describe your task. Then, use a single print statement 
that uses the | operator to merge invoice_data with an anonymous 
on-the-fly dictionary checking block {"client_tag": "Axaro"} straight 
inside an f-string display block.
'''
invoice_data = {"id": 1042, "cost": 299.99}
# Task: Build an internal automated invoice tracker by merging corporate client metrics with tags.
print(f"Merged invoice data: {invoice_data | {"client_tag": "Axaro"}}")
