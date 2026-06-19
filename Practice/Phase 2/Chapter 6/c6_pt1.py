'''
Chapter6, topic - async/await basics
'''
'''
Task 1 (Easy) — The Smart SMS Dispatcher Goal: Create an asynchronous 
function named send_sms that takes a parameter named phone_number. The 
function must print "Outgoing SMS: Sending text alert to [phone_number]...". 
Then use await asyncio.sleep(1) to simulate cell network lag. Finally, 
print "Outgoing SMS: Message safely delivered to [phone_number]!". Action: 
Use asyncio.run() to launch your function passing the number "01799998888" 
and verify both print logs fire with the one-second pause gap in between.
'''
import asyncio
async def send_sms(phone_number):
    print(f"Outgoing SMS: Sending text alert to {phone_number}...")
    await asyncio.sleep(1)
    print(f"Outgoing SMS: Message safely delivered to {phone_number}!")
asyncio.run(send_sms("01799998888"))
'''
Task 2 (Medium) — Sequential vs Concurrent Report Generator Goal: Create an 
async function named generate_pdf_report. It should take a report_name 
string, print "Generating PDF data for [report_name]...", pause for 2 
seconds using the async sleep tool, and return "PDF_[report_name] Completed".
Inside a main async function, fire two separate report tasks concurrently 
using asyncio.gather() for "Sales_2026" and "Inventory_2026". Save the 
gathered output list and print it.Action: Run the file. Verify that both 
tasks start at the exact same moment, and the total execution completes 
in 2 seconds flat instead of 4!
'''
import asyncio
import time
async def generate_pdf_report(report_name):
    print(f"Generating PDF data for {report_name}...")
    await asyncio.sleep(2)
    return f"PDF_{report_name} Completed"
async def mainA():
    start_time = time.time()
    gathered_list = await asyncio.gather(generate_pdf_report("Sales_2026"), 
                                         generate_pdf_report("Inventory_2026"))
    print(gathered_list)
    end_time = time.time()
    print(f"Total runtime: {((end_time) - (start_time)):.2f}seconds")
asyncio.run(mainA())
'''
Task 3 (Bit Harder) — The Multi-Agent System Check Goal: Create an async 
function named ping_security_node that takes a string node_id and an integer 
delay_seconds. The function must print "Node [node_id]: Initiating ping 
sweep...", pause for delay_seconds using the async tool, and return "Node 
[node_id]: SECURE".Inside a main orchestrator function, construct a list 
of three separate task calls passing custom metrics: Node "A" with a 1-second 
delay, Node "B" with a 3-second delay, and Node "C" with a 2-second delay. 
Gather them concurrently and print the final aggregated statuses list.
Action: Run your master pipeline. Confirm that all nodes fire simultaneously, 
and verify that your print summary handles the responses cleanly as 
they resolve.
'''
import asyncio
async def ping_security_node(node_id: str, delay_seconds: int):
    print(f"Node {node_id}: Initiating ping sweep...")
    await asyncio.sleep(delay_seconds)
    return f"Node {node_id}: SECURE"
async def mainB():
    task_list = (ping_security_node("Node 'A'", 1),
                 ping_security_node("Node 'B'", 2),
                 ping_security_node("Node 'C'", 3))
    aggregated_status = await asyncio.gather(*task_list)
    print(aggregated_status)
asyncio.run(mainB())