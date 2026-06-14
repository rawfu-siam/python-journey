'''
Chapter3, topic - iterators and generators
'''
'''
Task 1 (Easy) — The Dynamic Ticket Number Counter Goal: Create a 
generator function named ticket_stream. It must use a loop to 
yield numbers from 1 to a maximum target number passed into the 
function as a parameter.Action: Create a generator for 3 tickets. 
Use a for loop to iterate through it and print "Ticket Number: 
X" for each entry.
'''
def ticket_stream(total_tickets):
    count = 1
    while count <= total_tickets:
        yield count
        count += 1
ticket_pipeline = ticket_stream(3)
for ticket in ticket_pipeline:
    print(f"Ticket number: {ticket}")
'''
Task 2 (Medium) — The B2B Safe Financial Multiplier Loop Goal: 
Create a generator function named revenue_doubler. It must take 
a standard list of integer base revenue values (e.g. 
[1000, 5000, 12000]). Loop through the list, multiply each 
individual number by 2, and yield the new doubled value out.
Action: Pass [50, 100, 200] into your generator. Run next() 
twice on your generated stream to extract and print the first 
two calculated revenue boosts (should verify as 100 and 200).
'''
def revenue_doubler(base_revenue):
    for amount in base_revenue:
        yield amount * 2
raw_amounts = [50, 100, 200]
doubled_revenue_stream = revenue_doubler(raw_amounts)
print(next(doubled_revenue_stream))
print(next(doubled_revenue_stream))
'''
Task 3 (Bit Harder) — The Webhook Anomaly Data Filter Goal: Create 
a generator function named clean_log_stream. It must take a list 
of log dictionaries like [{"msg": "User login", "type": "INFO"}, 
{"msg": "Hack attempt", "type": "ERROR"}]. The generator must 
loop through the logs, but it must only yield the message string 
if the type matches "ERROR". If it says "INFO", it skips it 
completely!Action: Instantiate a batch of 3 logs (2 INFO items 
and 1 ERROR item). Use a for loop over your custom generator to 
ensure it filters out the noise and only prints the critical 
error text block summary.
'''
def clean_log_stream(log_dict):

    for log in log_dict:
        if log["type"] == "ERROR":
            yield log["msg"]
        elif log["type"] == "INFO":
            continue
webhook_logs = [{"msg": "User login", "type": "INFO"}, 
         {"msg": "Hack attempt", "type": "ERROR"},
         {"msg": "Admin login", "type": "INFO"}]
error_message_stream = clean_log_stream(webhook_logs)
for error_message in error_message_stream:
    print(error_message)
