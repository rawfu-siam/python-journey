'''
Chapter6, topic - async / await basics
'''
'''
Task 1 (Easy): Micro-Service Diagnostic Logger. Create a simple async coroutine task 
that logs system execution check thresholds. Setup: Import asyncio. Logic: Write an 
asynchronous function named run_diagnostic that prints "Initializing system 
diagnostics...", uses await asyncio.sleep(1) to simulate a check pause, and then 
prints "Diagnostic Status: 100% Clear". Verification Parameter: Call your coroutine 
function using asyncio.run(). Verify your terminal logs out your initialization 
text line, waits exactly 1 second, and prints out the final completion message 
safely.
'''
import asyncio
async def run_diagnostic():
    print("Initializing system diagnostics...")
    await asyncio.sleep(1)
    print("Diagnostic Status: 100% Clear")
asyncio.run(run_diagnostic())
'''
Task 2 (Medium): Parallel Webhook Dispatcher. Build a dual concurrent dispatch 
simulator routing script. Logic: Write two separate asynchronous functions: 
send_slack_alert and send_discord_alert. Each function must print a starting 
dispatch text log, pause for 1 non-blocking second using asyncio.sleep(1), and 
print a final success statement. Combine them into an orchestrator function 
named main that runs both tasks concurrently using asyncio.gather(). Verification 
Parameter: Fire off your setup using asyncio.run(main()). Verify that both task 
start logs hit your terminal console before either success statement prints out.
'''
import asyncio
async def send_slack_alert():
    print("Sending the slack message...")
    await asyncio.sleep(1)
    print("[SLACK GATEWAY] Alert broadcast completed.")

async def send_discord_alert():
    print("Sending the discord message...")
    await asyncio.sleep(1)
    print("[DISCORD GATEWAY] Alert broadcast completed.")
async def main():
    await asyncio.gather(send_slack_alert(), send_discord_alert())
asyncio.run(main())
'''
Task 3 (Above Average): Multi-Agent Scraping Core Simulator. Design a parameterized 
extraction system that manages complex worker times safely. Logic: Write an 
asynchronous function named scrape_website that accepts two parameters: url (str) 
and wait_time (int). Inside, print "Scraping node active for: " followed by the 
URL name. Use await asyncio.sleep(wait_time) to simulate page rendering loads. 
Finally, return a string text reading: "Data extracted from " + url. Execution: 
Inside your async main orchestrator, initialize two parallel tasks processing 
scrape_website("github.com", 2) and scrape_website("openai.com", 1) grouped 
together via asyncio.gather(). Capture the returned results list and print them.
Verification Parameter: Run your setup. Verify your script initiates both web 
scraping sites concurrently, finishes loading openai.com before github.com, and 
displays both extraction strings packed together inside a clean results array.
'''
import asyncio
async def scrape_website(url:str, wait_time: int):
    print(f"Scraping node active for: {url}")
    await asyncio.sleep(wait_time)
    return f"Data extracted from {url}"
async def main():
    results = await asyncio.gather(
        scrape_website("github.com", 2), 
        scrape_website("openai.com", 1))
    print(results)
asyncio.run(main())
