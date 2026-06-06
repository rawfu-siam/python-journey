# t1
for i in range(1,6):
    if i == 4:
        break
    print(i)
# t2
cart = ["milk", "egg_carton_broken", "bread"]
for item in cart:
    if item == "egg_carton_broken":
        print("Skipping item...")
        continue
    print("Item added safely to grocery bag:")
# t3
data_packets = ["good", "good", "placeholder_node", "good", "corrupted_file", "good"]
for packet in data_packets:
    if packet == "placeholder_node":
        pass
    if packet == "corrupted_file":
        print("Warning! Corrupted file detected!")
        break
    print("Data packet processed successfully.")
