'''
Chapter1, topic - lambda function
'''
'''
Task 1 (Easy): Write a lambda function that takes a user's name as an 
input string and returns a personalized greeting like "Hello, [Name]!". 
Test it with a name!
'''
greetings = lambda name: f"Hello, {name}!"
print(greetings("John"))
'''
Task 2 (Medium): An online store wants to apply a flat $5 discount 
coupon to an item, but only if the item costs more than $20. Write a 
single lambda function that uses a conditional expression (if-else) 
to check the price and return the final discounted value.
'''
discounted_price = lambda price: price - 5 if price > 20 else price
print(discounted_price(50))
'''
Task 3 (Above Average): You have a list of strings representing messy 
usernames scraped from a web page: [" user_alpha ", "beta_user ", "  
gamma   "]. Use Python's built-in sorted() function combined with a 
custom key lambda function to sort this list by the length of the 
strings after stripping out all the empty outer spaces!
'''
usernames = [" user_alpha ", "beta_user ", "  gamma   "]
usernames.sort(key= lambda name: len(name.strip()))
print(usernames)
