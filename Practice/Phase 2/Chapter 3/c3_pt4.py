'''
Chapter3, topic - __name__ and __main__
'''
'''
Task 1 (Easy) — The Secret Identity Agent Tag Goal: Create a script named 
agent_badge.py. Inside it, write a print statement that outputs the raw 
value stored inside the internal __name__ variable. Underneath that, add 
an if __name__ == "__main__": gate that prints "Agent badge checked: 
Standing by on primary console.". Action: Execute the file directly in 
your terminal/IDE and confirm both text blocks print successfully.
'''
# DONE 
'''
Task 2 (Medium) — The Isolated Client Discounter Goal: Create a helper 
script named billing_rules.py. Inside it, define a function 
apply_agency_discount(price) that returns the price multiplied by 0.90 
(a 10% discount). At the bottom of the file, add an if __name__ == 
"__main__": guard box. Inside that box, test your function by running 
print(apply_agency_discount(100)) to make sure it outputs 90.Action: 
Execute billing_rules.py directly to make sure your playground test 
value prints out perfectly.
'''
# DONE 
'''
Task 3 (Bit Harder) — The Silent Webhook Trigger Goal: Create two files 
in your environment folder: webhook_sender.py and app_dashboard.py.In 
webhook_sender.py, write a function fire_webhook() that prints "🚀 
Webhook payload launched safely!". Underneath it, add an unprotected 
print statement outside of any block that says "⚠️ System Warning: 
Testing active server signals!". Now, wrap only the execution of 
fire_webhook() inside an if __name__ == "__main__": block.In 
app_dashboard.py, simply type import webhook_sender.Action: Run 
app_dashboard.py. Verify that the security warning prints out 
(because it was left unprotected), but the active webhook launch 
message is completely blocked and silenced from executing.
'''
# DONE 
