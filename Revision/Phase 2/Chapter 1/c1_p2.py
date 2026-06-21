'''
Chapter1, topic - map, filter, reduce
'''
'''
Task 1 (Easy): You have a list of product item prices: [10, 20, 30, 40]. 
Use the map function with a lambda to add a flat $3 shipping fee to 
every single item. Print the new final list.
'''
product_prices = [10, 20, 30, 40]
final_prices = list(map(lambda a: a + 3, product_prices))
print(final_prices)
'''
Task 2 (Medium): An AI scraper returns a list of lead scores: [45, 88, 
30, 91, 75, 60]. Use the filter function with a lambda to keep only the 
elite leads whose scores are 70 or higher. Print the filtered list.
'''
leads = [45, 88, 30, 91, 75, 60]
elite_leads = list(filter(lambda lead: lead >= 70, leads))
print(elite_leads)
'''
Task 3 (Above Average): A multi-agent AI system outputs a batch sentence 
fragments list: ["AI ", "Automation ", "is ", "the ", "Future!"]. Use 
the reduce function with a custom lambda to concatenate (glue) all 
these individual text fragments into one single seamless title string!
'''
from functools import reduce 
words = ["AI ", "Automation ", "is ", "the ", "Future!"]
final_string = reduce(lambda x, y: x+y, words)
print(final_string)
