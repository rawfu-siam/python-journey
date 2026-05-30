'''
Chapter8, topic - function
'''
'''
Task 1 (Medium): The Lead Greeting Engine Define a function called 
generate_welcome_msg that takes one parameter slot called client_name. 
Inside, have it combine the name with a business string to return: 
"Hello [client_name], welcome to our AI Agency workspace!". Call the 
function with your name and print the final result.
'''
def generate_welcome_msg(client_name):
    return f"Hello {client_name}, welcome to our AI Agency workspace!"
    
person = generate_welcome_msg("Alice")
print(person)
'''
Task 2 (Intermediate): The Crypto Investment Calculator 📈Define a function 
called calculate_profit that takes two parameters: buy_price and sell_price. 
Have it subtract the buy price from the sell price to calculate the net 
profit.If the profit is greater than 0, have it return the string: "🟢 
Profit made: $X".Otherwise, return: "🔴 Net loss or break even: $X".
Test it by saving the result to a variable and printing it.
'''
def calculate_profit(buy_price, sell_price):
    net_profit = sell_price - buy_price
    if net_profit > 0:
        return f"🟢 Profit made: ${net_profit}"
    else:
        return f"🔴 Net loss or break even: ${net_profit}"
sale1 = calculate_profit(100,250)
print(sale1)
'''
Task 3 (Professional Challenge): Global Automation Task Estimator 
Define a function called estimate_project_hours that takes a list of 
task strings (e.g., ["Scraping", "AI Prompting", "Webhook Setup"]).
Inside the function, loop through the list items. If a task contains 
the word "AI", add 5 hours to a total counter. If it doesn't, add 2 
hours to the counter. Have the function return the final total hour 
integer. Test it using a sample list of tasks.
'''
def estimate_project_hours(task_list):
    total_counter = 0
    for task in tasks:
        if "AI" in task:
            total_counter = total_counter +5
        else:
            total_counter = total_counter +2
    return total_counter
tasks = ["Scraping", "AI Prompting", "Webhook Setup"]
project1 = estimate_project_hours(tasks)
print(project1)
