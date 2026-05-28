'''
Chapter6, topic - if/elif/else
'''
'''
Task 1 (Medium): The Crypto Trader Alert System 📈Create a variable 
called bitcoin_price. Write an if/elif/else system. If the price goes 
above $90,000, print "🚨 SELL NOW!". If it drops below $60,000, print 
"📉 BUY THE DIP!". Otherwise, print "😴 Do nothing. Market is stable."
'''
bitcoin_price = 40000
if bitcoin_price > 90000:
    print("SELL NOW!")
elif bitcoin_price > 60000:
    print("BUY THE DIP!")
else:
    print("Do nothing. Market is stable.")
'''
Task 2 (Intermediate): User Access Control 🔐Create two variables: 
user_age (an integer) and has_parental_permission (a boolean True/False). 
Write a system that prints "🔓 Access Granted" if the user is 18 or older, 
or if they are younger than 18 but have parental permission. Otherwise, 
print "🔒 Access Denied."
'''
user_age = 19
has_parental_permission = False
if user_age > 18 or has_parental_permission:
    print("Access Granted!")
else:
    print("Access Denied.")
'''
Task 3 (Professional Challenge): AI API Rate Limiter 📡Create two 
variables: api_calls_made and account_tier (which can be "Free", "Gold", 
or "Platinum").Free users are blocked if api_calls_made is greater 
than 100.Gold users are blocked if it's greater than 1000.Platinum 
users are never blocked.Write an optimized script that prints either "
🔴 Rate Limit Exceeded: Upgrading required" or "🟢 Request Approved".
'''
api_calls_made = 550
account_tier = "Gold"
if account_tier == "Free":
    if api_calls_made < 100:
        print("Request Approved")
    else:
        print("Rate Limit Exceeded: Upgrading required")
elif account_tier == "Gold":
    if api_calls_made < 1000:
            print("Request Approved")
    else:
        print("Rate Limit Exceeded: Upgrading required")
elif account_tier == "Platinum":
    print("Request Approved")
else:
    print("Sorry Something went wrong!")