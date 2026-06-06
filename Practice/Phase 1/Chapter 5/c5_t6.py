# t1
base_info = {"name": "Siam", "age": 18}
contact_info = {"city": "Dhaka", "country": "Bangladesh"}
full_profile = base_info | contact_info
print(full_profile)
# t2
standard_menu = {"Burger": 4.50, "Drinks": 1.50}
holiday_pricing = {"Drinks": 2.50, "Fries": 3.00}
standard_menu |= holiday_pricing
print(standard_menu)
# t3
hardware = {"device": "Laptop"}
memory_specs = {"ram": "16GB", "storage": "512GB"}
upgrades = {"ram": "32GB"}
final_spec_sheet = hardware | memory_specs | upgrades
print(final_spec_sheet)
