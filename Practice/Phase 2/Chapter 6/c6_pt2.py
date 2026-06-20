'''
Chapter6, topic - threading basics
'''
'''
Task 1 (Easy) — The Background Email Dispatcher Goal: Create a function 
named async_email_sender that takes a parameter string named recipient. 
It must print "📬 Outbox: Dispatching email packet to [recipient]...", 
sleep for 1 second using time.sleep(1), and print "📬 Outbox: Email 
safely sent to [recipient]!".Action: Create a thread worker targeting 
this function passing "tammy@dev.com". Start the thread, and make 
sure to print a message from the main thread saying "🚀 Master App: 
Continuing dashboard tasks..." immediately right after starting the 
worker to watch them run in parallel.
'''
import threading
import time
def async_email_sender(recipient):
    print(f"📬 Outbox: Dispatching email packet to {recipient}...")
    time.sleep(1)
    print(f"📬 Outbox: Email safely sent to {recipient}!")
extra_worker = threading.Thread(target=async_email_sender, args=("tammy@dev.com",))
extra_worker.start()
print(f"🚀 Master App: Continuing dashboard tasks...")
'''
Task 2 (Medium) — Locked Calculation Pipeline Goal: Create a function named 
calculate_compound_interest that takes an integer number parameter named 
account_id. It must print "📊 Thread: Scanning ledger rows for Account 
[account_id]...", pause for 2 seconds, and print "📊 Thread: Computation 
finished for Account #[account_id].".Inside a main execution block, spawn 
the worker thread for Account 9021. Start the worker, but right underneath 
it, apply the .join() safety block to force the main script to wait until 
the thread settles before printing a final completion log statement
"🚀 System: All ledger updates finalized. Main thread shutting down safely.".
Action: Verify that your output enforces the wait sequence precisely, 
blocking the final main log print until the calculation completes.
'''
import threading
import time
def calculate_compound_interest(account_id: int) -> None:
    print(f"📊 Thread: Scanning ledger rows for Account #{account_id}...")
    time.sleep(2)
    print(f"📊 Thread: Computation finished for Account #{account_id}.")
def main():
    extra_worker2 = threading.Thread(target=calculate_compound_interest, args=(9021,))
    extra_worker2.start()
    extra_worker2.join()
    print("🚀 System: All ledger updates finalized. Main thread shutting down safely.")
if __name__ == "__main__":
    main()
'''
Task 3 (Bit Harder) — The Parallel Server Node Audit Sweep Goal: Create a function 
named audit_hardware_node that takes a single integer parameter named node_number. 
The function must print "🔍 Scanner: Auditing security parameters for Node 
#[node_number]...", sleep for 1.5 seconds, and print "🔍 Scanner: Node #
[node_number] verified CLEAN.".Inside a main function, use a loop to spawn 
and start three separate threads to sweep Node 1, Node 2, and Node 3 concurrently.
Append all threads into a list array, and write a separate trailing loop to 
call .join() on each thread to ensure all sweeps clear safely before printing 
a final message: "🏆 Audit Complete: Entire data center infrastructure secured!".
Action: Run your parallel scanner blueprint. Confirm that all three node audits 
initiate at the exact same second, executing concurrently.
'''
import threading
import time
def audit_hardware_node(node_number: int) -> None:
    print(f"🔍 Scanner: Auditing security parameters for Node #{node_number}...")
    time.sleep(1.5)
    print(f"🔍 Scanner: Node #{node_number} verified CLEAN.")
thread_list = []
def mainB():
    for i in range(1,4):
        extra_worker3 = threading.Thread(target=audit_hardware_node, args=(i,))
        thread_list.append(extra_worker3)
        extra_worker3.start()
    for thread in thread_list:
        thread.join()
    print(f"🏆 Audit Complete: Entire data center infrastructure secured!")
if __name__ == "__main__":
    mainB()
  