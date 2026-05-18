# t1
with open("daily_hours.txt", "w") as file1:
    file1.write("Target milestone locked: Committing 3000 hours of deep work.\n")
# t2
with open("daily_hours.txt", "+a") as file2:
    file2.write("Discipline tracking stabilizer active.")
with open("daily_hours.txt", "r") as file3:
    read_it = file3.read()
    print(read_it)
# t3
agencies = ["Scale_AI", "OpenAI_Remote", "Tokyo_Tech_Labs"]
i = 0
with open("target_employers.txt", "w") as target_employer:
    for agency in agencies:
        i = i + 1
        target_employer.write(f"Company Node {i}: {agency}\n")
