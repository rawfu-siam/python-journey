# t1
tracking_counter = 5
while True:
    tracking_counter = tracking_counter - 1
    print(tracking_counter)
    if tracking_counter == 2:
        print("Safe landing!")
        break
# t2
payment_status = "PENDING"
attempt = 0
while True:
    print("Waiting for payment confirmation link...")
    attempt = attempt + 1
    if attempt == 4:
        payment_status = "SUCCESS"
    if payment_status == "SUCCESS":
        print("Transaction Complete! Dispensing invoice receipt now.")
        break
# t3
scraped_pages = 0
while True:
    scraped_pages = scraped_pages + 1
    print(f"[Scraper Bot]: Extracted data matrix from web page number: {scraped_pages}")
    if scraped_pages == 4:
        print("[Scraper Bot]: Data extraction pipeline batch run complete.")
        break
