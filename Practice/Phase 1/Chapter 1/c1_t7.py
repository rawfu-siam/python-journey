# t1
import math                 # Style 1
import pyjokes as pj        # Style 2
from random import randint  # Style 3

print(f"The value of pi is: {math.pi}")
print(f"Your jersey no is: {randint(1,50)}")
print(pj.get_joke())
# t2
from random import choice, randint
subject_list = ["Python", "Math", "Physics", "English", "Chemistry"]
subject = choice(subject_list)
duration = randint(25,90)
print(f"Today's focus: {subject}")
print(f"Study for: {duration} minutes")
print("Stay focused. No distractions.")
# t3
# already imported
score1 = randint(50,100)
score2 = randint(50,100)
score3 = randint(50,100)
score4 = randint(50,100)
score5 = randint(50,100)
average = math.floor((score1 + score2 + score3 + score4 + score5)/5)
# subject_list already done above

print(f"Math:        {score1}")
print(f"Physics:     {score2}")
print(f"Chemistry:   {score3}")
print(f"English:     {score4}")
print(f"Python:      {score5}")
print("───────────────")
print(f"Average:     {average}") 
