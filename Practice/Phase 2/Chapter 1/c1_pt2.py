'''
Chapter1, topic - map, filter, reduce
'''
'''
Task 1 (Easy) — The Smart Price Tag Inflator (map)Goal: A retail client wants to 
increase all their product prices by $5 due to shipping costs.Input list: prices 
= [10, 25, 50, 100]Action: Use map() and a lambda function to add 5 to every price.
'''
prices = [10, 25, 50, 100]
updated_prices = list(map(lambda price : price + 5, prices))
print(updated_prices)
'''
Task 2 (Medium) — VIP Client Identifier (filter)Goal: Extract high-value customers 
from a database list based on their transaction tier score.Input list: scores = 
[85, 42, 91, 60, 95, 30] Action: Use filter() to create a new list containing only 
scores that are greater than or equal to 80.
'''
scores = [85, 42, 91, 60, 95, 30]
top_scores = list(filter(lambda score : score>=80, scores))
print(top_scores)
'''
Task 3 (Bit Harder) — The Corporate Expense Counter (reduce)Goal: Calculate the exact 
total financial burn rate of your agency server bills.Input list: bills = [120, 80, 250, 
150]Action: Import reduce and calculate the combined sum total of all the numbers in 
the list.
'''
from functools import reduce
bills = [120, 80, 250, 150]
total_sum = reduce(lambda x,y : x + y, bills)
print(total_sum)
