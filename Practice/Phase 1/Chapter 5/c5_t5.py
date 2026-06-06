# t1
device = {"type": "PC", "ram_gb": 16}
only_keys = device.keys()
only_values = device.values()
print(only_keys)
print(only_values)
# t2
stock_sheet = {"Laptop" : 1200, "Mouse" : 25}
searched_item = (input("Search item: ")).title()
result = stock_sheet.get(searched_item, "Item not found in inventory")
print(result)
# t3
master_record = {"user": "Siam", "clearance": "L1"}
fresh_logs = {"clearance": "L3", "joined_date": "2026"}
master_record.update(fresh_logs)
print(f"Updated clearance value: {master_record['clearance']} and joined date: {master_record.get("joined_date", "not found")}")
