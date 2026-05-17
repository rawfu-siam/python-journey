# t1
allowed_languages =["python", "javascript", "golang"]
if "python" in allowed_languages:
    print("Supported")
else:
    print("Not Supported")
# t2
user_bio = "I am an experienced AI automation builder and cloud engineering specialist."
found = "AI profile detected" if "AI" in user_bio else "AI profile not detected"
print(found)
# t4
active_nodes = {"node_1", "node_2", "node_3"}
target_node = "node_5"
if target_node not in active_nodes:
    print("Warning: Node offline. Initializing backup automated routing sequence!")
else:
    print("Target node online.")
    