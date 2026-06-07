'''
Chapter1, topic - *args and **kwargs
'''
'''
Task 1 (Easy) — The Unlimited Inventory Counter (*args)Goal: Build a function 
named count_total_stock(*args) that accepts any number of inventory item count 
integers and returns their collective sum. Test Call: Calling count_total_stock
(15, 25, 10) should output 50.
'''
def count_total_stock(*args):
    return sum(args)
result = count_total_stock(15, 25, 10)
print(result)
'''
Task 2 (Medium) — The Dynamic Server Registry (**kwargs)Goal: Construct a function 
named register_server(**kwargs) that accepts variable key-value infrastructure 
definitions. The function should loop through the data and print each config 
parameter as: Config: [Key] -> Value: [Value].Test Call: Run it with parameters 
like ip="192.168.1.1", status="Online", ram="16GB".
'''
def register_server(**kwargs):
    for key,value in kwargs.items():
        print(f"Config: {key.upper()} -> Value: {value}")
register_server(ip="192.168.1.1", status="Online", ram="16GB")
'''
Task 3 (Bit Harder) — The Modular Agency Contract Gatekeeper (Mixed Parameters)
Goal: Write a system function named generate_contract(client_name, *services, 
**adjustments).It must print the client's name.It must loop through and print 
all active text strings bundled inside the services parameters.It must check 
if a keyword key named discount exists inside the adjustments parameters 
dictionary. If it does, print: Discount Factor Applied: [Discount Value].
'''
def generate_contract(client_name, *services, **adjustments):
    print(client_name)

    for service in services:
        print(f"- {service}")
    if "discount" in adjustments:
        print(f"Discount Factor Applied: {adjustments['discount']}")
generate_contract("Acme Corp", "SEO", "Web Dev", discount="20%", rush=True)
