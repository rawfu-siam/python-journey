'''
Chapter1, topic - lambda function
'''
'''
Task 1 (Easy) — The Celsius to Fahrenheit ConverterGoal: Write a lambda 
function that converts a temperature from Celsius to Fahrenheit.Formula: 
Fahrenheit = (Celsius * 9/5) + 32. Test Case: Input 0 should give you 32.0. 
Input 100 should give you 212.0.
'''
fahrenheit_converter = lambda celsius : (celsius * 9/5 + 32)
print(fahrenheit_converter(0)) 
print(fahrenheit_converter(100))
'''
Task 2 (Medium) — The Currency Arbitrage CalculatorGoal: Create a lambda 
function that takes an amount in USD ($) and converts it to Bangladeshi 
Taka (BDT). Assume an exchange rate of 1 USD = 117 BDT. Test Case: 
Inputting 100 USD should return 11700 BDT.
''' 
usd_to_bdt = lambda usd : usd * 117
print(usd_to_bdt(100))
print(usd_to_bdt(650))
'''
Task 3 (Bit Harder) — The Automated GatekeeperGoal: Write a lambda 
function that checks if an incoming lead's budget is enough for your 
agency. The function should take an integer input. If the input is 
1500 or higher, return the string "Approved". If it is less than 1500, 
return "Rejected".Hint: Use the inline if-else pattern !
'''
lead_budget = lambda price : "Approved" if price>=1500 else "Rejected"
print(lead_budget(2000))
print(lead_budget(1000))
