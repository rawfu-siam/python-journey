'''
Chapter5, topic - Dictionary
'''
'''
Task 1 (Medium): Create a dictionary called target_plan. 
Inside it, map a key named "destination" to hold 
the value "Japan", and a key named "hours_target" to hold the 
integer 3000. Print out the target hours value onto your 
screen by using its exact custom key index bracket.
'''
target_plan = {
    "destination" : "Japan",
    "hours_target" : 3000
}
print(target_plan["hours_target"])
'''
Task 2 (Hard): Inside the same script file, create a dictionary 
variable named live_status tracking a single key-value block: 
"revision_phase": 1. On the line below it, update that phase 
value to 2 using its key pointer assignment. On the next line, 
insert a brand-new boolean switch pair into the dictionary: "is_ready": 
True. Print the final complete state of the dictionary.
'''
live_status = {"revision_phase": 1,}
live_status["revision_phase"] = 2
live_status["is_ready"] = True
print(live_status)
'''
Task 3 (Professional Business Problem): Build an internal automated 
invoice metadata file block. Create a dictionary named invoice_metadata. 
It must track three keys: "invoice_id" set to a whole number integer, 
"billing_decimal" set to any float price value, and "client_tag" set 
to a text string. Write a single print() statement that extracts and 
displays the client tag and billing float price cleanly divided by 
an arrow string separator (" -> ").
'''
invoice_metadata = {"invoice_id" : 222, "billing_decimal" : 99.00, "client_tag" : "Axaro" }
print(f"{invoice_metadata['client_tag']} -> {invoice_metadata['billing_decimal']}")
