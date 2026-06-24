'''
Chapter2, topic - @classmethod
'''
'''
Task 1 (Easy): Create a class called Project. Inside its standard constructor 
__init__, save an instance attribute named title. Create a class method 
called from_short_code(cls, code). This method should take a code string, 
slap "Project Alpha: " right in front of it, and return a newly constructed 
Project object. Verification Parameter: Test it by calling 
Project.from_short_code("LeadScraper"). Print out the newly generated 
object's .title attribute to confirm it reads exactly "Project Alpha: 
LeadScraper".
'''
class Project:
    def __init__(self, title):
        self.title = title
    @classmethod
    def from_short_code(cls, code):
        titlaA = f"Project Alpha: {code}"
        return cls(titlaA)
proA = Project.from_short_code("LeadScraper")
print(proA.title)
'''
Task 2 (Medium): Create an automation class called EmailLead. Its standard 
constructor accepts username and domain. Create a specialized factory class 
method called from_raw_email(cls, email_address). This method should accept 
a full email string (like "john@agency.com"), chop it into two pieces at 
the "@" symbol using .split("@"), and return a perfect initialized EmailLead 
object instance. Verification Parameter: Test it by executing 
lead = EmailLead.from_raw_email("sivana@techcorp.io"). Print out 
lead.username and lead.domain separately to verify the parsing 
split worked cleanly.
'''
class EmailLead:
    def __init__(self, username, domain):
        self.username = username
        self.domain = domain
    @classmethod  
    def from_raw_email(cls, email_address):
        real_username, real_domain = email_address.split("@")
        return cls(real_username, real_domain)
lead = EmailLead.from_raw_email("sivana@techcorp.io")
print(lead.username)
print(lead.domain)
'''
Task 3 (Above Average): Create an invoicing standardizer class named InvoiceNode 
containing an __init__(self, description, price_integer) constructor. Add a 
specialized alternative factory class method inside named 
from_messy_list(cls, data_array). This method should parse a list array layout 
containing three items: [description_string, price_string, status_string]. Your 
factory must extract the description, use int() to typecast the price string 
into a proper integer number, apply a flat $10 processing surcharge fee addition 
to that integer, and return a completed initialized InvoiceNode object instance.
Verification Parameter: Initialize a test using scraped_payload = 
["n8n_Cloud_Hosting", "45", "PAID"]. Pass this list directly through your 
alternative constructor factory: invoice = 
InvoiceNode.from_messy_list(scraped_payload). Verify that printing out 
invoice.price_integer outputs exactly the calculated integer value of 55.
'''
class InvoiceNode:
    def __init__(self, description, price_integer):
        self.description = description
        self.price_integer = price_integer
    @classmethod
    def from_messy_list(cls, data_array):
        description_string = data_array[0]
        price_string = int(data_array[1]) + 10
        return cls(description_string, price_string)
scraped_payload = ["n8n_Cloud_Hosting", "45", "PAID"]
invoice = InvoiceNode.from_messy_list(scraped_payload)
print(invoice.price_integer)
