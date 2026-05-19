# t1
class ClientProfile:
    def __init__(self, company_name, tier):
        self.name = company_name
        self.tier = tier
client1 = ClientProfile("Fintech Tokyo", "Enterprise")
print(f"Company name: {client1.name} and tier: {client1.tier}")
# t2
class StripePayment:
    def __init__(self, amount, currency):
        self.amount = float(amount)
        self.currency = currency
        self.tax_amount = self.amount * 0.15
paymentx = StripePayment(5000, "$")
print(f"Total tax: {paymentx.currency}{paymentx.tax_amount}")
# t3
class N8nServerNode:
    def __init__(self, server_id, max_load):
        self.server = int(server_id)
        self.max_load = int(max_load)
        self.current_load = 0
        self.active_jobs = []
    def add_job(self, job_name):
        if self.current_load + 25 <= self.max_load:
            self.job_name = job_name
            self.active_jobs.append(job_name)
            self.current_load += 25
        else:
            print("Load is max!")
server1 = N8nServerNode("234",50)
server1.add_job("developer")
print(server1.current_load)
print(server1.max_load)
print(server1.active_jobs)
# solve tasks 3