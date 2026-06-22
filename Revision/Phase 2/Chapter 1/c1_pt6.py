'''
Chapter1, topic - global keyword
'''
'''
Task 1 (Easy): Create a global variable called client_name and set it to 
"Unknown". Write a function called set_client_name() that uses the global 
keyword to update that main variable to your actual name. Run the function 
and print the global variable outside to verify it changed.
'''
client_name = "Unknown"
def set_client_name():
    global client_name
    client_name = "Danny"
print(client_name)
set_client_name()
print(client_name)
'''
Task 2 (Medium): An online e-commerce checkout script has a global variable 
called total_cart_value = 150. Write a function called apply_discount_coupon() 
that updates the global value by subtracting $20 from it, but only if the 
current cart value is strictly greater than $100! Print the final updated
cart value outside.
'''
total_cart_value = 150
def apply_discount_coupon():
    global total_cart_value
    if total_cart_value > 100:
        total_cart_value -= 20
apply_discount_coupon()
print(total_cart_value)
'''
Task 3 (Above Average): Create a global variable called active_connections = 0. 
Write two separate functions: user_login() which adds 1 to the global counter, 
and user_logout() which subtracts 1 from the counter. Simulate a sequence: two 
users log in, one user logs out, and print the active connections tally value 
at each step!
'''
active_connections = 0
def user_login():
    global active_connections
    active_connections += 1
def user_logout():
    global active_connections
    active_connections -= 1
user_login()
print(f"[METRIC] Active Connections: {active_connections}")
user_login()
print(f"[METRIC] Active Connections: {active_connections}")
user_logout()
print(f"[METRIC] Active Connections: {active_connections}")
