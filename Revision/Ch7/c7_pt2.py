'''
Chapter6, topic - for loop with if and else
'''
'''
Task 1 (Medium): Food Allergy Scanner 🛑Create a list called 
dish_ingredients filled with strings: "Tomato", "Garlic", "Peanuts", 
and "Olive Oil". Write a loop that checks each ingredient. If it finds 
"Peanuts", print "🚨 ALLERGY WARNING: Contains peanuts! Do not serve." 
and exit the loop immediately using a break.
'''
dish_ingredients = ["Tomato", "Garlic", "Peanuts", "Olive Oil"]
for items in dish_ingredients:
    if items == "Peanuts":
        print("🚨 ALLERGY WARNING: Contains peanuts! Do not serve.")
        break
'''
Task 2 (Intermediate): VIP Coupon Voucher Lookup 🎟️Create a list called 
active_coupons containing "SAVE10", "WELCOME20", and "FREESHIP". Create a 
variable called user_coupon = "DISCOUNT50". Write a for...else loop system 
to check if user_coupon exists inside active_coupons. If it matches, 
print "🎟️ Coupon Applied!" and break. If the loop completes and the 
coupon isn't found, use the loop else block to print "❌ Invalid Coupon Code."
'''
active_coupons = ["SAVE10", "WELCOME20", "FREESHIP"]
user_coupon = "DISCOUNT50"
for coupons in active_coupons:
    if coupons == user_coupon:
        print("🎟️ Coupon Applied!")
        break
else:
    print("❌ Invalid Coupon Code.")
'''
Task 3 (Professional Challenge): Security Webhook Log Audit 🔐Create a list of 
dictionaries called server_logs containing system status events:
[{"event": "login", "status": "success"}, {"event": "api_call", "status": "success"}, 
{"event": "database_sync", "status": "failed"}]Write a professional-grade audit 
script that sweeps through the logs.If any event has a status of "failed", print 
"🚨 SECURITY ALERT: Critical system failure detected at [event_name]!" and break 
out instantly.If the entire log matrix is swept and no failures are found, use 
the loop else block to print "🟢 SYSTEM HEALTHY: All telemetry points operating 
within nominal parameters."
'''
server_logs = [ {"event": "login",           "status": "success"},
                {"event": "api_call",        "status": "success"}, 
                {"event": "database_sync",   "status": "failed" }]
for log in server_logs:
    if log["status"] == "failed":
        print(f"🚨 SECURITY ALERT: Critical system failure detected at {log["event"]}!")
        break
else:
    print("🟢 SYSTEM HEALTHY: All telemetry points operating within nominal parameters.")
