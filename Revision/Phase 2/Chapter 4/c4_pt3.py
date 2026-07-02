'''
Chapter4, topic - typing module
'''
'''
Task 1 (Easy): Flexible Metadata Container. Create a script that uses a 
dynamic type variable to hold flexible data shapes. Setup: Import Any from 
the typing module. Declare a variable named client_metadata with the 
type hint Any. Initialize it with the string value "Active Status" and 
print it. On the next line, re-assign it to the integer value 200 and 
print it again. Verification Parameter: Run your script directly and 
verify that your terminal outputs "Active Status" on the first line and 
200 on the second line without crashing.
'''
from typing import Any
client_metadata: Any = "Active Status"
print(client_metadata)
client_metadata = 200
print(client_metadata)
'''
Task 2 (Medium): Node Verification Alias BlueprintCreate a shortcut type 
alias to clean up collection tracking definitions. Setup: Import TypeAlias 
from the typing module. Define an alias named StringList that represents a 
list of strings (list[str]).Logic: Write a function named verify_nodes 
that takes a parameter named nodes (hinted as StringList) and returns an 
integer (-> int). Inside, return the total count of elements using len(nodes).
Verification Parameter: Initialize result: int = verify_nodes
(["node_alpha", "node_beta"]). Run your file and verify that printing 
result outputs exactly 2.
'''
from typing import TypeAlias
StringList: TypeAlias = list[str]
def verify_nodes(nodes: StringList) -> int:
    return len(nodes)
result: int = verify_nodes(["node_alpha", "node_beta"])
print(result)
'''
Task 3 (Above Average): Functional Automation Callback GateDesign an execution 
manager function that accepts another function as a callback tool. Setup: 
Import Callable from the typing module. Logic: Write a function named 
execute_task that takes two parameters: task_name (hinted as str) and 
worker_function (hinted as Callable[[str], bool]). The function must return 
a boolean (-> bool). Inside, run worker_function(task_name) and return its 
output.Verification Parameter: Define a helper function mock_bot(name: str) 
-> bool: return True. Call status: bool = execute_task("Sync_Task", mock_bot) 
and verify that printing status outputs exactly True.
'''
from typing import Callable
def execute_task(task_name: str, worker_function: Callable[[str], bool]) -> bool:
    return worker_function(task_name)
def mock_bot(name: str) -> bool:
    return True
status: bool = execute_task("Sync_Task", mock_bot)
print(status)
