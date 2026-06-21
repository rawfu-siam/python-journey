'''
Chapter4, topic - string index
'''
'''
Task 1 (Medium): Create a script named c4_pt1.py. 
Create a variable called target_country holding 
the string "Japan". Print out the third letter 
(the letter 'p') by passing its exact positive 
index number to the bracket tool.
'''
target_country = "Japan"
print(target_country[2])
'''
Task 2 (Hard): Inside the same file, create a 
variable called agency_token and ask the user 
to type an organization token using input(). 
Use negative indexing to extract the absolute 
last character of whatever they typed, 
and print it out.
'''
agency_token = input("Enter you token number: ")
print(agency_token[-1])
'''
Task 3 (Professional Business Problem): Write an 
internal system validation check. Create a 
variable tracking a product ID: product_id = "N-984". 
Use an index lookup to capture the very first 
character symbol ('N'). Print out a statement 
that looks like this: Validation check passed 
for sector: N.
'''
product_id = "N-984"
print(f"Validation check passed for sector: {product_id[0]}")
