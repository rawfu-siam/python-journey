'''
Chapter4, topic - types definition
'''
'''
Task 1 (Easy):Declare a variable named project_count labeled explicitly as an 
integer data type with a starting value of 12. Below it, declare a variable named 
is_completed labeled explicitly as a boolean data type with a value of False. 
Verification Parameter: Print both variables sequentially and verify that your 
system successfully outputs 12 on the first line and False on the second line.
'''
project_count: int = 12
is_completed: bool = False
print(project_count)
print(is_completed)
'''
Task 2 (Medium):Write a function named get_profile_link that accepts a single 
argument named username (strictly hinted as a string). The function must combine 
that username with a URL and return a final string reading: "https://github.com" 
+ username. Ensure your function contains an explicit string return type hint 
contract. Verification Parameter: Initialize link: str = get_profile_link("flora"). 
Verify that running print(link) outputs exactly "https://github.comflora".
'''
def get_profile_link(username: str) -> str:
    return f"https://github.com{username}" 
link = get_profile_link("flora")
print(link)
'''
Task 3 (Above Average):Design an automated agency system script. Write a function 
named project_revenue that accepts two inputs: monthly_salary (hinted as a float) 
and months_worked (hinted as an integer). The function must multiply these two 
inputs and explicitly promise to return the calculated value as a float data 
shape. Verification Parameter: Initialize a test runner statement evaluating 
project_revenue(3500.0, 4). Run your script directly and verify it prints out 
the result exactly as 14000.0.
'''
def project_revenue(monthly_salary: float, months_worked: int) -> float:
    total_salary = monthly_salary * months_worked
    return total_salary
print(project_revenue(3500.0, 4))
