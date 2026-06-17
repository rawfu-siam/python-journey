'''
Chapter4, topic - types definition
'''
'''
Task 1 (Easy) — The Secure Profile Welcome Sign Goal: Create a function 
named format_welcome_message that takes a parameter named username 
(hinted as a string) and a parameter named user_id (hinted as an integer). 
The function must return an f-string (hinted as a string) that says 
"Welcome back, [username]! Your ID is #[user_id]".Action: Run your 
function passing your name "Martin" and the ID number 101, then print 
the returned text to verify it works.
'''
def format_welcome_message(username: str, user_id: int) -> str:
    return f"Welcome back, {username}! Your ID is #{user_id}."
test1: str = format_welcome_message("Martin", 101)
print(test1)
'''
Task 2 (Medium) — The Agency Safe Tax Scaler Goal: Create a function named 
calculate_agency_tax that takes a parameter named revenue (hinted as a float) 
and a parameter named tax_rate (hinted as a float). It must use the arrow 
notation to show it returns a float value. Inside, multiply revenue * 
tax_rate and return the final value.Action: Test it by passing a revenue 
of 50000.00 and a tax rate of 0.15. Save the returned outcome into a 
typed float variable named total_tax, and print it.
'''
def calculate_agency_tax(revenue: float, tax_rate: float) -> float:
    final_value = revenue * tax_rate
    return final_value
total_tax: float = calculate_agency_tax(50000.00, 0.15)
print(total_tax)
'''
Task 3 (Bit Harder) — The Active Task Clearance Check 🤖Goal: Create a 
function named is_pipeline_clean that takes a parameter named active_tasks 
(hinted as a list). It must use arrow notation to show it returns a 
boolean value (bool). Inside, check if the length of the list is exactly 
equal to 0. If it is empty, return True. If it contains items, return 
False.Action: Test your pipeline function twice: first pass an empty 
list [], and second pass a list containing ["Scrape Leads", "Send Email"]. 
Print both outputs to verify it switches between True and False correctly.
'''
def is_pipeline_clean(active_tasks: list)-> bool:
        return len(active_tasks) == 0
empty_pipeline = []
active_pipeline = ["Scrape Leads", "Send Email"]
print(is_pipeline_clean(empty_pipeline))
print(is_pipeline_clean(active_pipeline))
