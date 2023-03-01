#print(f"EWACH")
#print(f"KIWANUKA")
def get_input(insert):
    return input(insert)

customer_name = get_input("Enter customer name: ")
commodity_name = get_input("Enter commodity name: ")
commodity_price = float(get_input("Enter commodity price: "))
date = get_input("Enter date: ")
cashier_name = get_input("Enter cashier name: ")

# Calculate net sale
vat = 0.18
net_sale = commodity_price * (1 - vat)

# Print output
print("\n")
print("Name of customer: ", customer_name)
print("Name of cashier: ", cashier_name)
print("Date: ", date)
print("Commodity name: ", commodity_name)
print("Commodity price: ", commodity_price)
print("Net sale: ", net_sale)
print("\nDetails of the developer:")
print("Developed by: ewach\ nkiwanuka")