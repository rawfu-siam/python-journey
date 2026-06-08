'''
Chapter2, topic - attribute and static method
'''
'''
Task 1 (Easy) — The Shared Corporate Domain TrackerGoal: Build a class named 
CRMConnector.Add a Class Attribute named target_domain set to "://agency.com".
Add an Instance Attribute inside __init__ named client_id.Test Action: Create 
two separate connectors with different client IDs, and print out their individual 
client IDs along with their shared target_domain.
'''
class CRMConnector:
    target_domain = "://agency.com"
    def __init__(self,client_id):
        self.client_id = client_id
client1 = CRMConnector(5888)
client2 = CRMConnector(5868)
print(f"client id: {client1.client_id} | targeted domain: {CRMConnector.target_domain}")
print(f"client id: {client2.client_id} | targeted domain: {CRMConnector.target_domain}")
'''
Task 2 (Medium) — The Automated Multi-Agent RegistryGoal: Create a class named 
AIAgent.Add a Class Attribute named spawned_agents_count initialized to 0.
Inside your __init__ constructor, increase that shared counter by 1 every time 
an agent is spawned.Test Action: Create 3 independent agent objects and print 
out the master class variable score value to prove it tracked all 3 allocations 
successfully.
'''
class AIAgent:
    spawned_agents_count = 0
    def __init__(self):
        AIAgent.spawned_agents_count +=1
agent1 = AIAgent()
agent2 = AIAgent()
agent3 = AIAgent()
print(AIAgent.spawned_agents_count)
'''
Task 3 (Bit Harder) — The Financial Arbitrage Ledger EngineGoal: Build a class 
named FinanceEngine.Add a Class Attribute named total_bdt_processed set to 0.
Add a Static Method named usd_to_bdt(usd_amount) that simply multiplies an 
input amount by 117 and returns the calculation result.Add a standard object 
method named process_payment(usd) that calls your static method tool to convert 
the incoming transaction, and adds that outcome value permanently to the main 
class variable total_bdt_processed.
'''
class FinanceEngine:
    total_bdt_processed = 0
    @staticmethod
    def usd_to_bdt(usd_amount):
        return usd_amount*117
    
    def process_payment(self,usd):
        bdt_converter = FinanceEngine.usd_to_bdt(usd)
        FinanceEngine.total_bdt_processed += bdt_converter

test1 = FinanceEngine()
test1.process_payment(500)
print(FinanceEngine.total_bdt_processed) 
