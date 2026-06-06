# t1
scores = [80, 55, 90]
for i in scores:
    if i >= 60:
        print(f"Congrats! you passed! you got: {i}")
    else:
        print(f"Sorry you failed! you got: {i}")
# t2
for x in range(1,4):
    print(f"Downloading part {x}")
else:
    print("All download parts joined together successfully!")
# t3
activity_log = ["read", "read", "unread", "read"]
for status in activity_log:
    if status == "unread":
        print("Notification Badge: Lit")
else:
    print("Database status check sequence complete.")
