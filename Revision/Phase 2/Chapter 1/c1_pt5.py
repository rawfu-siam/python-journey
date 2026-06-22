'''
Chapter1, topic - *args and **kwargs
'''
'''
Task 1 (Easy): Write an automated logging function called 
show_team(*args). It should accept any number of employee name 
strings and print each one out sequentially as "Team Member: [Name]". 
Test it with three names.
'''
def show_team(*args):
    for name in args:
        print(f"Team Member: {name}")
show_team("Newton", "Einstein", "Tesla")
'''
Task 2 (Medium): Create an agency billing calculator function called 
invoice_summary(base_fee, *extras, **taxes). It should sum all the 
numeric costs inside extras and add them to the base_fee. Then, check 
if a labeled tax rate parameter named vat exists inside taxes. If it 
does, multiply the subtotal by that rate and print the absolute final 
grand total!
'''
def invoice_summary(base_fee, *extras, **taxes):
    subtotal = base_fee + sum(extras)
    vat_rate = taxes.get("vat", 1.0)
    grand_total = subtotal * vat_rate
    print(f"The grand total of your purchase is ${grand_total:.2f}")
invoice_summary(500, 34, 44, 67, vat=1.10)   
'''
Task 3 (Above Average): Build a flexible multi-channel messaging router 
function called dispatch_alert(alert_text, **channels). The function 
reads the keys inside **channels. If slack=True is provided, print 
"[SLACK ROUTE]: alert_text". If whatsapp=True is passed, print 
"[WHATSAPP ROUTE]: alert_text". Test it with ("Server Database RAM 
threshold reached 90%!", slack=True, whatsapp=True)

'''
def dispatch_alert(alert_text, **channels):
        if channels.get("slack") is True:
            print(f"[SLACK ROUTE]: {alert_text}")
        if channels.get("whatsapp") is True:
            print(f"[WHATSAPP ROUTE]: {alert_text}")
dispatch_alert("Server Database RAM threshold reached 90%!", slack=True, whatsapp=True)
