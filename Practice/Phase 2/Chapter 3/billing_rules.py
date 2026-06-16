def apply_agency_discount(price):
    net_price = price * 0.90
    return net_price
if __name__ == "__main__":
    print(apply_agency_discount(100))