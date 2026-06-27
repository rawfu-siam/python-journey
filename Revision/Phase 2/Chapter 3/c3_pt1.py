'''
Chapter3, topic - custom decorators
'''
'''
Task 1 (Easy): Create a custom decorator function named stars_decorator. This 
decorator should print a decorative line of stars "**********" right before the 
wrapped function runs, and another line of stars right after it finishes executing.
Verification Parameter: Wrap it around a simple function def print_msg(): 
print("Python Progressing"). Call print_msg() and verify the terminal displays 
the messages cleanly sandboxed inside two rows of star banners.
'''
def stars_decorator(original_function):
    def wrapper():
        print("**********")
        original_function()
        print("**********")
    return wrapper
@stars_decorator
def print_msg():
    print("Python Progressing")
print_msg()
'''
Task 2 (Medium): Create an optimization decorator named convert_uppercase. This 
decorator should intercept whatever string output value is returned by the 
original function, convert that string completely to capitalized uppercase format 
using .upper(), and return that modified string text payload instead! Verification 
Parameter: Wrap it around a function def fetch_codename(): return "sk_live_agent". 
Call fetch_codename() and verify that printing the final execution output returns 
exactly the uppercase string text: "SK_LIVE_AGENT".
'''
def convert_uppercase(original_function):
    def wrapper(*args, **kwargs):
        raw_result = original_function(*args, **kwargs)
        return raw_result.upper()
    return wrapper
@convert_uppercase
def fetch_codename():
    return "sk_live_agent"
print(fetch_codename())
'''
Task 3 (Above Average): Let's build an automated currency formatting layer for an 
agency invoice billing system. Create a custom decorator named dollar_sign_injector.
This decorator should capture the numeric integer output returned by an underlying 
calculation function, convert that number format into a string, slap an official 
currency symbol variable prefix text string "$" right in front of it, and return 
that final styled text message payload. Verification Parameter: Wrap it around a 
calculation function def calculate_billing(hours, rate): return hours * rate. 
Test it by executing calculate_billing(10, 50). Verify that printing out the 
returned value outputs exactly the formatted string text: "$500".
'''
def dollar_sign_injector(original_function):
    def wrapper(*args, **kwargs):
        raw_number = original_function(*args, **kwargs)
        return f"${raw_number}"
    return wrapper
@dollar_sign_injector
def calculate_billing(hours, rate):
    return hours * rate
print(calculate_billing(10, 50))
