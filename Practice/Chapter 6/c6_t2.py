# t1
has_account = True
is_logged_in = False
if has_account == True:
    print("Account found.")
    if is_logged_in == True:
        print("Welcome dashboard!")        
    else:
        print("Please click login.")
else:
    print("Please create an account first!")
# t2
customer_spent = 150
has_coupon = True
if customer_spent > 100:
    print("Qualified for big savings evaluation.")
    if has_coupon == True:
        print("Total discount applied: 20%")
    else:
        print("Total discount applied: 10%")
else:
    print("Spend more than $100 to check for custom discounts.")
# t3
is_admin = True
secret_key = 9999
if is_admin == True:
    print("Admin level checked.")
    if secret_key == 9999:
        print("Full System Root Access Granted.")
    else:
        print("Security Breach! Wrong Code.")
else:
    print("Standard guest profile loaded successfully.")
    