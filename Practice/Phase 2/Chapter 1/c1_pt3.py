'''
Chapter1, topic - enumerate()
'''
'''
Task 1 (Easy) — The Automated Inventory AuditGoal: Create a script that lists 
warehouse stock items with a neat sequence tracker badge.Input list: 
inventory = ["Server Rack", "GPU Container", "UPS Backup"] Action: Use 
enumerate() with start=1 to print the items formatted exactly like:Item 1: 
Server Rack, Item 2: GPU Container, etc.
'''
inventory = ["Server Rack", "GPU Container", "UPS Backup"]
for index, item in enumerate(inventory, start=1):
    print(f"Item {index}: {item}")
'''
Task 2 (Medium) — The Even-Row Database ScannerGoal: An automation rule 
requires processing only records located on even-indexed rows (0, 2, 4) 
to balance task server processing loads.Input list: data_packets = 
["PKT-A", "PKT-B", "PKT-C", "PKT-D", "PKT-E"]Action: Use enumerate() to 
loop through the elements. Print the packet name only if its index 
position is an even number. (Hint: Use if index % 2 == 0:).
'''
data_packets = ["PKT-A", "PKT-B", "PKT-C", "PKT-D", "PKT-E"]
for number, packet in enumerate(data_packets):
    if number % 2 == 0:
        print(packet)
'''
Task 3 (Bit Harder) — The Fraudulent Transaction LocatorGoal: Build an 
automated transaction auditing scanner that identifies zero-value or 
negative entries and flags their exact row index locations for risk 
management teams.Input list: payments = [500, 1200, -50, 3100, 0, 4500]
Action: Loop through the payment data using enumerate(). If a payment 
value is less than or equal to 0, print a message stating: ALERT: Suspicious 
activity found at Index [X]! Value: [Value].
'''
payments = [500, 1200, -50, 3100, 0, 4500]
for index_no, payment in enumerate(payments):
    if payment <= 0:
        print(f"ALERT: Suspicious activity found at Index {index_no}! Value: {payment}")
