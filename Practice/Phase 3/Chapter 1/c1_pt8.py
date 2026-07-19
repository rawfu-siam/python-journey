'''
Chapter1, topic - open source contribution workflow
'''
'''
Task 1: The Safe Launch pad (Easy), Your Mission: Imagine you just forked 
an open-source project named awesome-automation-toolkit. Write down the 
exact terminal commands required to download your fork onto your computer 
and instantly switch to a safe feature branch named feat/add-slack-logger.
'''
# git clone https://github.com
# cd awesome-automation-toolkit

# git checkout -b feat/add-slack-logger
'''
Task 2: The Semantic Save Point (Medium), Your Mission: You just modified a 
Python file named utils.py to fix a sneaky security bug where someone's 
password was being printed to the logs. Write down the commands to stage 
this specific file and save it with a perfect, clean semantic commit message.
'''
# git add utils.py
# git commit -m "fix(security): stop masking and leaking user passwords in logs"
'''
Task 3: The Full Delivery Sequence (Bit Harder), Your Mission: Write out the 
complete sequence of commands from scratch for this real-world scenario:
Clone your fork at https://github.com and Create a branch called 
fix/missing-csv-header (Pretend you modified the file scraper.py here)
Stage and commit the change using an appropriate semantic message prefix.
Push your branch safely up to your online account (origin).
'''
# git clone https://github.com
# cd awesome-automation-toolkit

# git checkout -b fix/missing-csv-header

# git add scraper.py
# git commit -m "fix(scraper): append missing header row to exported CSV files"

# git push -u origin fix/missing-csv-header
