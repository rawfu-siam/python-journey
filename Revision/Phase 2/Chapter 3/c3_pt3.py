'''
Chapter3, topic - match case
'''
'''
Task 1 (Easy):Create a string variable named user_role and assign it a value like 
"admin". Write a match case structure checking if the role is "admin", "developer", 
or "guest", and print a corresponding greetings block. Include a wildcard case 
to handle unrecognized roles. Verification Parameter: Assign user_role = "developer". 
Verify that running your script displays your custom developer message in the terminal.
'''
user_role = "developer"
match user_role:
    case "admin":
        print("Hello admin!")
    case "developer":
        print("Hello developer!")
    case "guest":
        print("Hello guest!")
    case _:
        print("Role unrecognized!")
'''
Task 2 (Medium):Write a function named process_alert that accepts an integer argument 
level. Use match case with grouping operators | to check the severity level. If it's 1 
or 2, return "Low Alert". If it's 3 or 4, return "Medium Alert". If it's 5, return 
"Critical Alert". For anything else, return "Unknown Level". Verification Parameter: 
Initialize result = process_alert(4). Verify that running print(result) outputs 
exactly "Medium Alert".
'''
def process_alert(level):
    match level:
        case 1 | 2:
            return "Low Alert"
        case 3 | 4:
            return "Medium Alert"
        case 5:
            return "Critical Alert"
        case _:
            return "Unknown Level"
result = process_alert(4)
print(result)
'''
Task 3 (Above Average):Write a data routing pipeline system inside a loop that parses a 
command data tracking tuple list structure format. It should accept structured tuple 
blocks representing user authentication requests.Pattern match a list/tuple format 
reading ("login", username, password).Pattern match a list/tuple format reading 
("logout", username).Verification Parameter: Pass a tuple reading ("logout", "robert_dev") 
through your match case block and verify that your system successfully captures it 
and prints out a clean output tracking log statement reading: "User robert_dev 
disconnected safely."
'''
reading = ("logout", "robert_dev")
match reading:
    case ("login", username, password):
        print(f"User {username} logged in successfully!")
    case ("logout", username):
        print(f"User {username} disconnected safely.")
