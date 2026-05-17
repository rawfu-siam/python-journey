# t1
def display_agency_banner():
    print("====================")
    print("AI AUTOMATION")
    print("====================")
display_agency_banner()
# t2
def check_admission_score(score):
    if score >= 80:
        print("Status: Admission Confirmed!")
    else:
        print("Status: Retry Option Active.")
check_admission_score(85)
check_admission_score(72)
# t3
def convert_usd_to_bdt(usd_amount):
    bdt_total = usd_amount * 117
    print(f"${usd_amount} USD is equal to {bdt_total} BDT")
convert_usd_to_bdt(50)
