# t1
for row in range(1,3):
    for col in range(1,5):
        print("*", end="")
    print()
# t2
for row in range(1,4):
    for col in range(1,row +1):
        print(row, end="")
    print()
# t3
for row in range(1,4):
    for col in range(1,5 - row):
        print("*", end="")
    print()
