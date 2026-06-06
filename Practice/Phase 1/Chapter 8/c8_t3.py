# t1
def multiply_by_five(num):
    return num * 5
final_product = multiply_by_five(6)
print(final_product)
# t2
def verify_investment_limit(amount):
    if amount > 10000:
        return "Alert: Upper threshold breached. Lock transfer."
    else:
        return "Transaction Verified Successfully."
result =verify_investment_limit(15000)
print(result)
# t3
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)
answer = recursive_sum(5)
print(answer)
