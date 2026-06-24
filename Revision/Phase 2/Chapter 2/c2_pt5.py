'''
Chapter2, topic - abstraction (abc module)
'''
'''
Task 1 (Easy): Create an abstract base class called Database that 
inherits from ABC. Place an @abstractmethod sticker inside called 
connect(self). Build a concrete child class called SQLiteDatabase 
that fulfills the rule and prints "Connected to local sqlite3 
instance pipeline successfully.". Verification Parameter: Initialize 
an instance of SQLiteDatabase and call its .connect() method to 
verify the print execution.
'''
from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
class SQLiteDatabase(Database):
    def connect(self):
        print("Connected to local sqlite3 instance pipeline successfully.")
databaseA = SQLiteDatabase()
databaseA.connect()
'''
Task 2 (Medium): Create an abstract base class called SocialMediaBot(ABC).
Give it a normal pre-written shared method called log_action(self, action) 
that prints "[LOG ALERT]: Appended action: action". Give it a mandatory 
@abstractmethod called post_content(self, text).Build a child class called 
TwitterBot that fulfills the abstract rule by printing "🐦 Tweeting text 
payload onto public timeline feed!". Verification Parameter: Initialize 
TwitterBot(). Call .log_action("Post_01") followed immediately by 
.post_content("Learn Python in 2026") to verify both inherited and 
overridden behaviors run cleanly.
'''
from abc import ABC, abstractmethod
class SocialMediaBot(ABC):
    def log_action(self, action):
        print(f"[LOG ALERT]: Appended action: {action}")
    @abstractmethod
    def post_content(self, text):
        pass
class TwitterBot(SocialMediaBot):
    def post_content(self, text):
        print(f"🐦 Tweeting {text} payload onto public timeline feed!")
bot = TwitterBot()
bot.log_action("Post_01")
bot.post_content("Learn Python in 2026")
'''
Task 3 (Above Average): Let's build an automated agency billing gateway 
standardizer.Create an abstract base class called SaaSPricing(ABC) 
containing an __init__(self, plan_name, monthly_base_fee) constructor.
Add a mandatory @abstractmethod inside named calculate_yearly_bill(self).
Build a concrete child class called PremiumPlan that inherits from it. 
Its constructor should accept plan_name and monthly_base_fee, and pass 
them upward using super(). Its calculate_yearly_bill(self) method should 
take the inherited monthly_base_fee attribute, multiply it by 12, apply 
a flat $50 annual loyalty discount subtraction deduction, and return the 
final calculated number result. Verification Parameter: Initialize a 
PremiumPlan object instance using plan_name="Enterprise_AI", and 
monthly_base_fee=500. Call its .calculate_yearly_bill() method and verify 
the returned terminal calculation output shows exactly 5950.
'''
from abc import ABC, abstractmethod
class SaaSPricing(ABC):
    def __init__(self, plan_name, monthly_base_fee):
        self.plan_name = plan_name
        self.monthly_base_fee = monthly_base_fee
    @abstractmethod
    def calculate_yearly_bill(self):
        pass
class PremiumPlan(SaaSPricing):
    def __init__(self, plan_name, monthly_base_fee):
        super().__init__(plan_name, monthly_base_fee)
    def calculate_yearly_bill(self):
        return (self.monthly_base_fee * 12) - 50
planA = PremiumPlan("Enterprise_AI", 500)
print(planA.calculate_yearly_bill())
