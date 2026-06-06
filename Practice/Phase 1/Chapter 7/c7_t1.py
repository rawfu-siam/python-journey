# t1
for i in range(10,16):
    print(i)
# t2
system_logs = ["info", "warning", "error", "info", "error"]
for words in system_logs:
    print(words)
    if words == "error":
        print("Critical Alert: Fix issue immediately!")
    else:
        print("Log status: Clear")
# t3
user_input = "RUN"
cycles = 0
while user_input == "RUN":
    print(f"System processing cycle number: {cycles}")
    cycles = cycles + 1
    if cycles == 3:
        user_input = "STOP"
