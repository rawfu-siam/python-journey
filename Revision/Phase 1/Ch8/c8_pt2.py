'''
Chapter8, topic - function with arguments
'''
'''
Task 1 (Medium): Dynamic Invoice Billing Generator 🧾Define a function called 
generate_invoice that takes three parameter slots: client_name, amount, and 
currency. Give the currency parameter a default fallback value of "USD". Have 
the function return a clean string sentence matching this setup. Test it twice: 
once without supplying a currency, and once by passing "BDT".
'''
def generate_invoice(client_name, amount,currency="USD"):
    return f"Client {client_name} wants to pay the bill of ${amount} in {currency}."
client1 = generate_invoice("Alice", 3500)
client2 = generate_invoice("John", 2000, "Pound")
print(client1)
print(client2)
'''
Task 2 (Intermediate): User Profile Dashboard Map 👤Define a function called 
build_user_profile that takes three parameters: username, account_role, and status. 
Give status a default fallback value of "Active". Inside, return a dictionary 
containing those three properties as key-value pairs. Call this function using Keyword 
Arguments in a scrambled order to prove that labeling overrides positional limits.
'''
def build_user_profile(username, account_role, status="Active"):
    return {"client_name"   :       username,
            "role"          :       account_role,
            "current_statues":      status}
role1 = build_user_profile(account_role="Developer", username="Roger")
role2 = build_user_profile("Bunny", "Intern", "Inactive")
print(role1)
print(role2)
'''
Task 3 (Professional Challenge): AI API Token Throttle Node 🤖Define an optimization function 
called configure_api_node that takes four parameters: api_name, tokens_requested, tier 
(default value "Free"), and allow_overflow (default value False).If the user's tier is "Free" and 
their tokens requested are greater than 5000, check allow_overflow. If allow_overflow is False, 
return "❌ Request Blocked: Limit exceeded for Free Tier."For all other combinations, return 
"🟢 Configuration Validated. Connection Approved."Test this function by explicitly passing arguments 
to override the default parameter safety triggers.
'''
def configure_api_node(api_name, tokens_requested, tier="Free", allow_overflow=False):
    if tier == "Free" and tokens_requested > 5000:
        if allow_overflow == False:
            return "❌ Request Blocked: Limit exceeded for Free Tier."
    return "🟢 Configuration Validated. Connection Approved."
test1 = configure_api_node("Bbc25", 6000)
print(test1)
test2 = configure_api_node("Bbc75", 7000, "Gold", True)
print(test2)
