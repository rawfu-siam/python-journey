# t1
number = 50
try:
    division = 100/number
    print(f"The division result is {division}")
except ZeroDivisionError:
    print("We can't divide a number by zero.")
else:
    print("Success: Math completed beautifully!")
finally:
    print("Cleanup: Sequence finished safely.")
# t2
def safeguard_database_write(file):
    try:
        with open(file,"w") as f:
            f.write("Last transaction recorded!")
    except FileNotFoundError:
        print("There is no such file in the directory!")
    else:
        print("[System Notification]: Asset data written with zero errors!")
    finally:
        print("[System Notification]: Asset data written with zero errors!")
safeguard_database_write("file.txt")
# t3
request_tokens = [20, "corrupted", 0, 10]
for token in request_tokens:
    try:
        data_packet = 200 / token
    except TypeError:
        print("[Alert]: Token data type is corrupted. Skipped row.")
    except ZeroDivisionError:
        print("[Alert]: Token value is zero empty. Skipped row.")
    else:
        print(f"[Success]: Data packet transmission total calculated: {data_packet}")
    finally:
        print("[Pipeline Log]: Step checkpoint verified.")
