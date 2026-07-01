'''
Chapter4, topic - advanced type hints
'''
'''
Task 1 (Easy):Declare a variable named server_ips explicitly hinted as a 
list containing only string elements (list[str]), initialized with two mock 
IP strings. Below it, declare a variable named task_tracker explicitly 
hinted as a dictionary mapping string keys directly to boolean values 
(dict[str, bool]). Verification Parameter: Add a print statement tracking 
both variables and verify your console prints out your assigned collection 
states clearly.
'''
server_ips: list[str] = ['101', '102']
task_tracker: dict[str, bool] = {'logged in': True, 'logged out': False}
print(server_ips)
print(task_tracker)
'''
Task 2 (Medium):Write a function named process_payment that accepts a single 
argument named amount explicitly hinted to allow either an integer or a 
float value (int | float). The function must return a string reading: 
"Payment logged: " followed by the amount converted to a string. Ensure 
your function signature includes its structural string return hint. 
Verification Parameter: Initialize test_run: str = process_payment(450.50). 
Run your file and verify it prints out exactly "Payment logged: 450.50".
'''
def process_payment(amount: int | float) -> str:
    return f"Payment logged: {(amount):.2f}"
test_run: str = process_payment(450.50)
print(test_run)
'''
Task 3 (Above Average):Design an elite agency user lookup system module. 
Write a function named find_email that takes an integer system identifier 
argument named user_id. The function must look up data and explicitly 
promise to return either a string containing an email address OR None if 
the identification key is invalid. Verification Parameter: Pass an 
invalid user ID argument through your function, capture the returned 
result into an annotated variable, and use print statements to verify 
that it outputs None safely without causing execution breaks.
'''
def find_email(user_id: int) -> str | None:
    agency_db: dict[int, str] = {
        1: "architect@agency.com", 2: "developer@agency.com" }
    return agency_db.get(user_id, None)
lookup_result: str | None = find_email(999)
print(lookup_result) 
