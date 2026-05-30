'''
Chapter7, topic - loop - for/range/while
'''
'''
Task 1 (Medium): The Instagram Follower Count Loop 📈Create a list called 
follower_milestones containing the integers 1000, 5000, 10000, and 25000. 
Write a for loop that iterates through the list and prints "🎉 Milestone 
Reached: X followers!" for each value.
'''
follower_milestones = [1000, 5000, 10000, 25000]
for x in follower_milestones:
    print(f"🎉 Milestone Reached: {x} followers!")
'''
Task 2 (Intermediate): Odd Number Invoice Batcher 🧾Write a for loop using 
the range() function to find all odd numbers between 1 and 15 (inclusive, 
meaning 15 should be included!). Print each number out to simulate sorting 
alternating rows. Hint: Use the step parameter inside range()!
'''
for o in range(1,16,2):
    print(o)
'''
Task 3 (Professional Challenge): Safe Cloud Database Downloader 💾Create a 
variable called downloaded_megabytes = 0. Write a while loop that simulates 
downloading a large data package. The loop should run as long as 
downloaded_megabytes is less than 100. Every time the loop spins, increase 
downloaded_megabytes by 25, and print out "📥 Download progress: X MB received". 
Once the loop ends, print "✅ Download complete!".
'''
downloaded_megabytes = 0
while downloaded_megabytes < 100:
    downloaded_megabytes += 25
    print(f"📥 Download progress: {downloaded_megabytes} MB received")
print("✅ Download complete!")
