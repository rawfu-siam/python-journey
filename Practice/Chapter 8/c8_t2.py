# t1
def calculate_rectangle_area(length, width):
    area = length * width
    print(f"The area of the rectangle is {area}")
calculate_rectangle_area(10,5)
# t2
def dispatch_delivery_bot(client_destination,bot_type = "Standard_Drone"):
    print(f"Dispatching a {bot_type} directly to location: {client_destination}.")
dispatch_delivery_bot("Dhaka_Sector_1")
dispatch_delivery_bot("Chittagong_Port","Heavy_Truck")
# t3
def trigger_system_alert(alert_message, admin_rank,send_sms_flag = False):
    if admin_rank == "Senior" and send_sms_flag == True:
        print(f"[CRITICAL SYSTEM SMS INITIATED]: {alert_message}")
    elif admin_rank == "Senior" and send_sms_flag == False:
        print(f"[Standard Console Log Registered]: {alert_message}")
    else:
        print("[Access Denied]: Low ranking profile cannot view alert matrix data.")
trigger_system_alert("Rush to the base", "Senior", True)
