'''
Chapter3, topic - match case
'''
'''
Task 1 (Easy) — The Smart Security Clearance Badge Router Goal: Create a 
function named verify_clearance_level(badge_role). Use a match case block 
to inspect the incoming role string.If it matches "CEO", print "Access 
Granted: Level 3 Server Vault Open".If it matches "Developer", print "Access 
Granted: Level 2 Lab Vault Open".For anything else, print "Access 
Denied: Intruders logged!".Action: Test it by passing "Developer" and 
then "Hacker" to verify your safety blocks trigger correctly.
'''
def verify_clearance_level(badge_role):
    match badge_role:
        case "CEO":
            print("Access Granted: Level 3 Server Vault Open")
        case "Developer":
            print("Access Granted: Level 2 Lab Vault Open")
        case _:
            print("Access Denied: Intruders logged!")
verify_clearance_level("Developer")
verify_clearance_level("Hacker")
'''
Task 2 (Medium) — The Multi-Server Status Code Hub Goal: Create a function 
named handle_server_status(status_code). Use match case to evaluate an 
integer status code.Combine codes 200 and 201 using a pipe operator to 
print "Server Response: Action Completed Safely".Combine codes 400 and 
404 to print "Server Response: Client Request Missing".Use the wildcard 
option to handle any other number as a generic "Server Response: Unknown 
Error Encountered".Action: Test your status hub by passing the values 
201, 404, and 503.
'''
def handle_server_status(status_code):
    match status_code:
        case 200 | 201:
            print("Server Response: Action Completed Safely")
        case 400 | 404:
            print("Server Response: Client Request Missing")
        case _:
            print("Server Response: Unknown Error Encountered")
handle_server_status(201)
handle_server_status(404)
handle_server_status(503)
'''
Task 3 (Bit Harder) — The Automated E-Commerce Fulfillment Parser Goal: 
Create a function named process_order_packet(order_tuple). The incoming 
tuple structure looks like (item_count, current_status). Overload the 
selection with match case.If it hits (count, "pending"), calculate a 
baseline value of count * 500 and print "Order pending. Expected revenue 
calculation: [Value] BDT". If it hits (count, "shipped"), print "Shipment 
active. Dispatched tracking loops for [count] items.".Add a conditional 
case guard to capture any items where count == 0 regardless of status, 
printing "Error: Empty batch container rejected.". Action: Run your 
function with three specific mock configurations: (5, "pending"), 
(12, "shipped"), and (0, "canceled").
'''
def process_order_packet(order_tuple):
    match order_tuple:
        case (count, current_status) if count == 0:
            print("Error: Empty batch container rejected.")
        case (count, "pending"):
            value = count * 500
            print(f"Order pending. Expected revenue calculation: {value} BDT")
        case (count, "shipped"):
            print(f"Shipment active. Dispatched tracking loops for {count} items.")
        case _:
            print("System Alert: Unhandled order packet signature.")
process_order_packet((5, "pending"))
process_order_packet((12, "shipped"))
process_order_packet((0, "canceled"))
