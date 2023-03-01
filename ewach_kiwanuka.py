# Define a dynamic function to calculate the net sale price
def calculate_net_sale_price(commodity_price):
    vat = 0.18
    net_sale_price = commodity_price - (commodity_price * vat)
    return net_sale_price


# Read input from keyboard
customer_name = input("Enter the name of the customer: ")
commodity_name = input("Enter the name of the commodity: ")
commodity_price = float(input("Enter the price of the commodity: "))
cashier_name = input("Enter the name of the cashier: ")
date = input("Enter the date (dd/mm/yyyy): ")

# Calculate the net sale price using the dynamic function
net_sale_price = calculate_net_sale_price(commodity_price)

print('------------------------')

# Print the output
print("\n")
print("Sale Details:")
print("--------------")
print("Customer Name: ", customer_name)
print("Commodity Name: ", commodity_name)
print("Commodity Price: ", commodity_price)
print("Net Sale Price: ", net_sale_price)
print("Cashier Name: ", cashier_name)
print("Date: ", date)

print('---------------------------')

# printing the names of the developers

print("\nDetails of the developer:")
print("Developed by: ewach\ nkiwanuka")
print("Copyright: © ewach\  nkiwanuka")