'''
Chapter2, topic - abstraction (abc module)
'''
'''
Task 1 (Easy) — The Social Media Enforcer FrameworkGoal: Create an 
abstract base class named SocialMediaBot that inherits from ABC. 
Add an abstract method named post_content().Build a child class 
named TwitterBot that overrides post_content() and returns 
"Twitter post uploaded successfully."Action: Instantiate a 
TwitterBot object and call the function.
'''
from abc import ABC, abstractmethod
class SocialMediaBot(ABC):
    @abstractmethod
    def post_content(self):
        pass
class TwitterBot(SocialMediaBot):
    def post_content(self):
        return "Twitter post uploaded successfully."
bot1 = TwitterBot()
print(bot1.post_content())
'''
Task 2 (Medium) — The Automated Agent Skill ContractGoal: Build a 
multi-rule abstraction template gate check: Abstract Base Class: 
BaseAgent → requires two abstract methods: .search_web() and 
.write_summary(). Child Class: ResearchSpecialist → successfully 
overrides both methods to return text strings of your choice.
Action: Instantiate ResearchSpecialist and verify that both 
methods call seamlessly without triggering a TypeError.
'''
class BaseAgent(ABC):
    @abstractmethod
    def search_web(self):
        pass
    @abstractmethod
    def write_summary(self):
        pass
class ResearchSpecialist(BaseAgent):
    def search_web(self):
        return "Completed web search!"
    def write_summary(self):
        return "Completed writing summary!"
specialist1 = ResearchSpecialist()
print(specialist1.search_web())
print(specialist1.write_summary())
'''
Task 3 (Bit Harder) — The Automated Multi-CRM Ledger InterfaceGoal: 
Construct an enterprise-grade customer tracking connector blueprint:
Abstract Base Class: AbstractCRM → has an __init__ setting crm_name. 
It requires one abstract method named export_lead(name, budget).
Child Class A: HubSpotCRM → overrides export_lead to return 
f"[{self.crm_name}] Exported {name} with budget ${budget}".
Child Class B: NotionCRM → overrides export_lead to calculate a 
converted BDT value (budget * 117) and return f"[{self.crm_name}] 
Logged row for {name} with value ৳{bdt_value}". Action: Place 
instances of both classes into a list, loop through them, execute 
.export_lead("Elon", 2000) on each, and print the outputs.
'''
class AbstractCRM(ABC):
    def __init__(self, crm_name):
        self.crm_name = crm_name
    @abstractmethod
    def export_lead(self, name, budget):
        pass
class HubSpotCRM(AbstractCRM):
    def export_lead(self, name, budget):
        return f"[{self.crm_name}] Exported {name} with budget ${budget}"
class NotionCRM(AbstractCRM):
    def export_lead(self, name, budget):
        bdt_value = budget * 117
        return f"[{self.crm_name}] Logged row for {name} with value ৳{bdt_value}"
all_crm = [HubSpotCRM("HubSpot"), NotionCRM("Notion")]
for crm in all_crm:
    print(crm.export_lead("Elon", 2000))
