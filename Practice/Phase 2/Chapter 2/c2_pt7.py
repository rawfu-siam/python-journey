'''
Chapter2, topic - @property decorators
'''
'''
Task 1 (Easy) — The Pet Age Guard 🐶Goal: Create a Pet class 
where __init__ sets an initial age inside self._age. Logic: Add 
a @property getter for age. Add a @age.setter that blocks negative 
numbers with an error message, but allows positive numbers to 
update self._age.Action: Instantiate a pet at age 2. Update it 
to -5, then to 4, printing the outputs.
'''
class Pet:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            print("Error! age can not be negative!")
        else:
            self._age = value
my_pet = Pet(2)
print(my_pet.age)
my_pet.age = -5
print(my_pet.age)
my_pet.age = 4
print(my_pet.age)
'''
Task 2 (Medium) — The Currency Converter 💵Goal: Create a Wallet class 
where __init__ stores Bangladeshi Taka inside self._bdt.Logic: Add a 
@property getter for usd that returns Taka divided by 115. Add a 
@usd.setter that takes a USD value, multiplies it by 115, and saves 
the new amount back into self._bdt.Action: Instantiate with 11500 BDT. 
Print the USD value. Set wallet.usd = 200 and print wallet._bdt.
'''
class Wallet:
    def __init__(self, bdt_amount):
        self._bdt = bdt_amount
    @property
    def usd(self):
        return self._bdt / 115
    @usd.setter
    def usd(self, value):
        self._bdt = value * 115
money_bag = Wallet(11500)
print(money_bag.usd)
money_bag.usd = 200
print(money_bag._bdt)
'''
Task 3 (Bit Harder) — The Agency Client Onboarding Gate 🏢Goal: Create 
an AgencyClient class where __init__ saves an email to self._email.
Logic: Add a @property getter for email. Add a @email.setter that looks 
for an "@" symbol. If missing, print a critical error; if present, 
update self._email.Action: Instantiate with "contact@nexus.ai". Try 
updating to "bad_email_format", then update to "admin@nexus.ai".
'''
class AgencyClient:
    def __init__(self, email):
        self._email = email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if "@" not in value:
            print("Something went wrong! please recheck the email!")
        else:
            self._email = value
email1 = AgencyClient("contact@nexus.ai")
print(email1.email)
email1.email = "bad_email_format"
print(email1.email)
email1.email = "admin@nexus.ai"
print(email1.email)