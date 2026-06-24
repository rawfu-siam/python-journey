'''
Chapter2, topic - @property decorators(getters and setters)
'''
'''
Task 1 (Easy): Create an automation class named ServerSpeed. Initialize a hidden 
instance attribute named _mbps.Build a @property getter that returns the raw _mbps 
value.Build a .setter method that checks if an incoming value is strictly greater 
than 1000. If it is, print "❌ Speed exceeds pipeline limit!". Otherwise, save 
it cleanly. Verification Parameter: Initialize connection = ServerSpeed(500). 
Attempt to set connection.mbps = 1200 to verify the guard-rail alert string prints.
'''
class ServerSpeed:
    def __init__(self, mbps):
        self._mbps = mbps
    @property
    def mbps(self):
        return self._mbps
    @mbps.setter
    def mbps(self, value):
        if value > 1000:
            print("❌ Speed exceeds pipeline limit!")
        else:
            self._mbps = value
connection = ServerSpeed(500)
connection.mbps = 1200
'''
Task 2 (Medium): Create an agency lead manager class called CRMRecord.
Its constructor initializes a hidden attribute named _email.Build a @property 
getter that returns the email string completely in lowercase format.
Build a .setter method that checks if an incoming string contains an "@" symbol
using the in operator. If it does NOT, print "❌ Invalid email format dropped.". 
Otherwise, save it. Verification Parameter: Initialize an instance object, 
then execute record.email = "bad_data_text". Confirm the error printout fires 
and protects your database payload.
'''
class CRMRecord:
    def __init__(self, email):
        self._email = email
    @property
    def email(self):
        return (self._email).lower()
    @email.setter
    def email(self, new_email):
        if "@" not in new_email:
            print("❌ Invalid email format dropped.")
        else:
            self._email = new_email
record = CRMRecord("abd@gmail.com")
record.email = "bad_data_text"
'''
Task 3 (Above Average): Let's build a secure payment gateway tracker.Create a 
class named ClientWallet with an __init__(self, initial_balance: int) constructor 
that initializes a hidden attribute named _balance.Add a property getter that 
returns the raw integer.Add a property setter that checks if the incoming update 
is an integer number type. If it is NOT, print "❌ Transaction Rejected: 
Invalid balance type.". If it is a valid integer, it must next check if the 
balance would fall below zero. If it would, print "❌ Transaction Rejected: 
Insufficient client capital reserves.". Otherwise, apply the new balance.
Verification Parameter: Initialize a test object using wallet = ClientWallet(100).
Run a sequence: first try setting wallet.balance = "one_hundred". Next, try 
setting wallet.balance = -50. Verify that both security guard checks trigger 
their respective protection printouts cleanly.
'''
class ClientWallet:
    def __init__(self, initial_balance: int):
        self._balance = initial_balance
    @property
    def balance(self):
        return int(self._balance)
    @balance.setter
    def balance(self, value):
        if not isinstance (value, int):
            print("❌ Transaction Rejected: Invalid balance type.")
        else:
            if value < 0:
                print("❌ Transaction Rejected: Insufficient client capital reserves.")
            else:
                self._balance = value
wallet = ClientWallet(100)
wallet.balance = "one_hundred"
wallet.balance = -50
