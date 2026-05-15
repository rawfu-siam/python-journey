# t1
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 140)
engine.setProperty('volume',1.0)
engine.say("My name is Siam")
engine.say("I am going to Japan for pursuing my bachelors degree")
engine.say("Winners never quit")

# t2
import random
player_list = ["Messi", "Ronaldo", "Neymar", "Mbappe", "Salah", "Lewandowski", "Kane","Xavi" ]
random.shuffle(player_list)
teamA = random.sample(player_list, 5)
print(f"TeamA: {teamA}")
# how to find remaining players in player_list after selecting teamA without advance for concept?
# t3
# I dont think that task1 can be done completely without further concept
import os
current = os.getcwd()
print(f"Current working directory: {current}")
files = os.listdir()
total_files = len(files)
engine.say(f"Total files in current directory: {total_files}")
engine.runAndWait()
engine.stop()
# I made lots of mistakes correct me!!