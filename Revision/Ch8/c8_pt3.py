'''
Chapter8, topic - recursion and return
'''
'''
Task 1 (Medium): Automated Message Repeater 📣Define a recursive function called 
repeat_alert that takes two parameters: message (String) and times (Integer).The 
Base Case should check if times == 0. If yes, use return to stop the function.
Otherwise, print the message string, and make the recursive call decreasing the 
times variable by 1 on every step. Test it with "🚨 Backup Sync Running" for 3 times.
'''
def repeat_alert(message, times):
    if times == 0:
        return "✅ All alerts successfully processed."
    
    print(message)
    return repeat_alert(message, times -1)

alert1 = repeat_alert("🚨 Backup Sync Running", 3)
print(alert1)
'''
Task 2 (Intermediate): The Math Factorial Multiplier 🔢In mathematics, a factorial 
(written as !) means multiplying a number by every whole number below it down to 1. 
For example, 4! = 4 * 3 * 2 * 1 = 24.Write a recursive function called calculate_factorial(n).
Base Case: If n == 1, return 1.Recursive Case: Return n * calculate_factorial(n - 1).
Test it by passing 4 and printing the final returned total.
'''
def calculate_factorial(n):
    if n == 1:
        return 1
        
    return n * calculate_factorial(n - 1)

result = calculate_factorial(4)
print(result)
'''
Task 3 (Professional Challenge): Crypto Wallet Reducer Matrix 📉Imagine a client has an 
initial crypto investment amount of $80. Every day they trade, their wallet amount gets 
cut in half due to market shifts. They want to stop trading the second their wallet 
balance falls below $15.Write a highly secure recursive function called audit_wallet_floor
(balance, days_count=0).Base Case: If balance < 15, return a string or dictionary stating 
the final balance and how many days it took to reach it.Recursive Case: Calculate the new 
balance by dividing the current balance by 2, increment days_count by 1, and return a 
recursive call passing these updated metrics down to the next gate layer.
'''
def audit_wallet_floor(balance, days_count=0):
    if balance < 15:
        return {
            "status": "Trading Halted",
            "final_balance_usd": round(balance, 2),
            "days_traded": days_count
        }
    new_balance = balance / 2
    return audit_wallet_floor(new_balance, days_count + 1)

audit_report = audit_wallet_floor(80)
print(audit_report)
