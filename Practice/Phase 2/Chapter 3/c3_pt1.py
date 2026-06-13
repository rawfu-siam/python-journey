'''
Chapter3, topic - custom decorator
'''
'''
Task 1 (Easy) — The VIP Welcomer Decorator 🎭Goal: Create a decorator 
named vip_stars. It must print three star emojis ⭐⭐⭐ right before 
the decorated function runs, and print three star emojis ⭐⭐⭐ right 
after it finishes. Action: Create a basic function def print_user(name): 
print(name). Decorate it with @vip_stars. Test it by passing the name 
"Mozi" to see stars printed around it.
'''
def vip_stars(original_function):
    def wrapper(*args, **kwargs):
        print("⭐⭐⭐")
        original_function(*args, **kwargs)
        print("⭐⭐⭐")
    return wrapper
@vip_stars
def print_user(name):
    print(name)
print_user("Mozi")
'''
Task 2 (Medium) — The Charge Double Up Multiplier ⚡Goal: Create a decorator 
named double_results. Inside the inner wrapper, capture the number returned 
by the original function, multiply that return number by 2, and return the 
final doubled calculation.Action: Decorate a function def 
calculate_bdt_bonus(amount): return amount. If you pass 15000 into 
the decorated function, verify the ultimate printed return value 
scales up to 30000.
'''
def double_results(original_function):
    def wrapper(*args, **kwargs):
        number = int(original_function(*args, **kwargs)) 
        doubled = number * 2
        return doubled
    return wrapper
@double_results
def calculate_bdt_bonus(amount):
    return amount
print(calculate_bdt_bonus(15000))
'''
Task 3 (Bit Harder) — The Capitalization Sanitation Filter Goal: Create 
a decorator named sanitize_username. Inside the inner wrapper, look at the 
username string argument passed into the function. Use python's 
.lower().strip() string tools to force the username to be completely 
lowercase and remove any empty trailing text spaces. Pass this clean, 
modified string parameter into the original function.Action: Slap the 
decorator onto def register_account(username): print(f"Registered 
user: {username}"). Test it by passing "  TaMmY_DeV   " into the 
function. Verify it prints the perfectly cleaned account string: 
"Registered user: tammy_dev".
'''
def sanitize_username(original_function):
    def wrapper(username):
        clean_name = username.lower().strip()
        return original_function(clean_name)
    return wrapper
@sanitize_username
def register_account(username):
    print(f"Registered user: {username}")
register_account("  TaMmY_DeV   ")
