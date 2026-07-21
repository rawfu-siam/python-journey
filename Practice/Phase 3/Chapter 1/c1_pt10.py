'''
Chapter1, topic - semantic commit messages
'''
'''
Task 1: The Slack Alert IntegrationYou just added a brand-new Python 
function to your automated workflow. This function automatically pings 
the team's #alerts channel on Slack whenever a background worker runs 
successfully. Write the git commit command for this new feature.
'''
# git commit -m "feat(slack): add success notification for background worker"
'''
Task 2: The Broken Row LoopYour web scraper crashed because some row 
entries in a CSV file were completely empty. You added an if row is not 
None: validation check to prevent the scraper from crashing on empty data.
Write the git commit command to log this bug fix.
'''
# git commit -m "fix(scraper): add validation check for empty CSV rows"
'''
Task 3: Cleaning Up the MessYou noticed your main script file was looking 
messy with unorganized variables. You didn't add any features, and you 
didn't fix any bugs; you just spent 20 minutes rearranging the variables 
to make the file easier to read for your teammates. Write the 
git commit command for this structural cleanup.
'''
# git commit -m "refactor: reorganize variables in main script for readability"