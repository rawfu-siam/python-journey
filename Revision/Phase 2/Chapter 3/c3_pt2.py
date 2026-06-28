'''
Chapter3, topic - iterators and generators
'''
'''
Task 1 (Easy): Create a list of 3 items: ["Laptop", "Mouse", "Keyboard"]. 
Convert it into an iterator using iter(), and use next() twice to print out 
the first two tools.
'''
items = ["Laptop", "Mouse", "Keyboard"]
item_iterator = iter(items)
print(next(item_iterator))
print(next(item_iterator))
'''
Task 2 (Medium): Write a generator function called countdown(n) that takes a 
number and counts down to 1 using yield. (e.g., countdown(3) should give 3, 
then 2, then 1).
'''
def countdown(n):
    for remaining_value in range(n, 0, -1):
        yield remaining_value
stream = countdown(3)
print(next(stream))
print(next(stream))
print(next(stream))
'''
Task 3 (Above Average):Write a generator function named revenue_simulator 
that takes two arguments: base_revenue (float) and growth_multiplier 
(float). Use a loop that runs exactly 3 times to calculate and yield 
the projected monthly agency revenue, where Month 1 returns the 
base_revenue, and each following month multiplies the previous 
month's revenue by the growth_multiplier. Verification 
Parameter: Initialize sim = revenue_simulator(3000.0, 1.2). Run 
print(next(sim)) and verify it prints exactly 3000.0, then run 
print(next(sim)) again to verify it prints exactly 3600.0.
'''
def revenue_simulator(base_revenue, growth_multiplier):
    current_revenue = base_revenue
    for _ in range(3):
        yield current_revenue
        current_revenue *= growth_multiplier
sim = revenue_simulator(3000.0, 1.2)
print(next(sim))
print(next(sim))
print(next(sim))
