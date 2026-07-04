'''
Chapter6, topic - threading basics
'''
'''
Task 1 (Easy): Background Database Sync Node. Create a basic thread worker that 
simulates a localized system sync function. Setup: Import threading and time.
Logic: Write a function named sync_records that prints "Starting database 
backup...", pauses for 2 seconds using time.sleep(2), and prints "Backup 
complete!". Wire up a threading. Thread target pointing to this function, 
start it, and let it complete. Verification Parameter: Run your file directly. 
Verify that your script boots up the database worker string log cleanly in 
the background.
'''
import threading
import time
def sync_records():
    print("Starting database backup...")
    time.sleep(2)
    print("Backup complete!")
worker = threading.Thread(target= sync_records)
worker.start()
'''
Task 2 (Medium): Corporate Report Generation. GateBuild a reporting module that 
uses a join gate command sequence.Logic: Write a function named build_pdf_report 
that prints "Generating client document data rows...", waits for 2 seconds using 
time.sleep(2), and prints "PDF file built successfully.". In your main script 
flow, spin up a thread worker targeting this function, start it, and execute a 
.join() command immediately after to force the system to wait. Once unblocked, 
print out a final log statement reading "System status: Ready to email client."
Verification Parameter: Initialize your setup and verify that the console outputs 
the ready statement only after the PDF construction row statements have fully 
logged out.
'''
import threading
import time
def build_pdf_report():
    print("Generating client document data rows...")
    time.sleep(2)
    print("PDF file built successfully.")
workerA = threading.Thread(target= build_pdf_report)
workerA.start()
workerA.join()
print("System status: Ready to email client.")
'''
Task 3 (Above Average): Parameterized Multi-Server Ping Tool. Design a dynamic 
network worker system that accepts string configuration properties safely. Logic: 
Write a function named ping_server that accepts a single string argument named 
server_ip. Inside, print "Pinging address: " followed by the IP string. Pause for 
1 second using time.sleep(1). Finally, print "Ping response received from " + 
server_ip.Execution: Inside your main execution block, initialize two parallel 
threads processing ping_server with arguments "192.168.1.1" and "10.0.0.1" passed 
safely via the args tuple syntax block. Start both threads and execute .join() 
commands on both components.Verification Parameter: Execute your file. Verify 
that your script initiates both connection lines concurrently, matching your 
precise variable inputs, and concludes execution cleanly.
'''
import threading
import time
def ping_server(server_ip):
    print(f"Pinging address: {server_ip}")
    time.sleep(1)
    print(f"Ping response received from {server_ip}")
worker1 = threading.Thread(target= ping_server, args=("192.168.1.1",))
worker2 = threading.Thread(target= ping_server, args=("10.0.0.1",))
worker1.start()
worker2.start()
worker1.join()
worker2.join()
