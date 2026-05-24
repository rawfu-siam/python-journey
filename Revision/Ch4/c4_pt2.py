'''
Chapter4, topic - string slicing
'''
'''
Task 1 (Medium): Open your existing script file c4_pt1.py or 
make a new one. Create a variable tracking a system process 
line: process_tag = "Level-36_Complete". Use string slicing 
to cut out just the word "Level" and print it out.
'''
process_tag = "Level-36_complete"
print(process_tag[0:5])
'''
Task 2 (Hard): Create a variable named full_project_code and 
store the string "AAA_CSE_2027" inside it. Use blank shorthands 
and slicing boundaries to cut out everything after the 
first underscore, so your screen prints out just "CSE_2027".
'''
full_project_code = "AAA_CSE_2027"
print(full_project_code[4:])
'''
Task 3 (Professional Business Problem): Build an encryption 
string checker. Create a string variable representing an 
asset database item: asset_id = "X1Y2Z3_REVERSED". Use 
slicing with step hops to reverse the entire string 
backward, and print the output result inside a clean 
f-string label block.
'''
asset_id = "X1Y2Z3_REVERSED"
print(f"Reversed id: {asset_id[::-1]}")
