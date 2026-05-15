# t1
import math
print(math.pi)          # shows the value of pi
print(math.sqrt(81))    # shows the square root of 81
print(math.floor(7.8))  # shows the largest integer less than or equal to 7.8
print(math.ceil(3.2))   # shows the smallest integer greater than or equal to 3.2
# t2
import random
participants = ["Messi", "Ronaldo", "Neymar", "Xavi", "Ramos"]
winner = random.choice(participants)
print(f"🎉 The winner is: {winner}!")
lucky_no = random.randint(100, 999)
print(f"And the lucky number - {lucky_no} is for {winner}.")
# t3
# math and random already imported
radius = random.randint(1, 50)
area = math.pi * math.pow(radius, 2)
puhhfekt_area = round(area, 2)
print("Radius:", radius)
print("Area of circle:", puhhfekt_area)
