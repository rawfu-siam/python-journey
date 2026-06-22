'''
Chapter1, topic - list comprehension
'''
'''
Task 1 (Easy): You have a list of raw numeric measurements: 
[3, 7, 12, 18]. Use a list comprehension to square every number 
(multiply it by itself). Print out the calculated output list.
'''
raw_measurements = [3, 7, 12, 18]
squared_values = [ x**2 for x in raw_measurements]
print(squared_values)
'''
Task 2 (Medium): An automated intake pipeline receives a registration 
list of client names: ["harry", "gorge", "zara", "fedrix"]. Use a list 
comprehension to transform every single name string format so it begins 
cleanly with an official capitalized first letter (use .capitalize()). 
Print the formatted results array.
'''
client_names = ["harry", "gorge", "zara", "fedrix"]
capitalized_names = [name.capitalize() for name in client_names]
print(capitalized_names)
'''
Task 3 (Above Average): A multi-agent network scaper returns a list of 
target platform monthly subscription costs: [15, 120, 45, 250, 8, 500]. 
Use a list comprehension containing a filtration guard gate to extract 
only the premium cost entries that are strictly greater than $50, and 
apply a 10% tax surcharge (multiply the value by 1.10) to those specific 
premium targets. Print the final tax-adjusted premium array list.
'''
subscription_costs = [15, 120, 45, 250, 8, 500]
premium_entries = [cost * 1.10 for cost in subscription_costs if cost > 50]
print(premium_entries)
