'''this program prompts the user to input data that is customer name,
commodity name, commmodity price, cashiers name and the date of sale of the commodity
then it displays the sale details including the net sale price after deducting the vat of 18%
'''



'''

import datetime

# defining the Dynamic function to read what the user inputs
def get_input(insert):
    return input(insert)


# user inputs
customerName = get_input("ENTER THE NAME OF THE CUSTOMER: ")
commodityName = get_input("ENTER THE COMMODITY NAME: ")
commodityPrice = float(get_input("ENTER THE PRICE OF THE COMMODITY: "))
cashierName = get_input("ENTER THE NAME OF THE CASHIER: ")
date_ofSale = datetime.datetime.now()

# defining the Dynamic function to calculate the net sale after VAT
def compute(price):
    return price * 0.82

#NET SALE
netSale = compute(commodityPrice)

# displaying the details of the sale
print("\n")

print("DETAILS OF THE SALE:")

print(f"NAME OF THE COMMODITY: {commodityName}")
print(f"PRICE OF THE COMMODITY: {commodityPrice}")
print(f"NET SALE: {netSale}")
print(f"NAME OF CUSTOMER: {customerName}")
print(f"NAME OF THE CASSHIER: {cashierName}")
print(f"DATE OF SALE: {date_ofSale.strftime('%Y-%m-%d %H:%M:%S')}")

# printing the names of the developers

print("\nDetails of the developer:")
print("Developed by: ewach\nkiwanuka")
print("Copyright: © ewach\nkiwanuka")

'''

def get_input(insert):
    return insert

customer_name = get_input("Enter customer name: ")
commodity_name = get_input("Enter commodity name: ")
commodity_price = float(get_input("Enter commodity price: "))
date = get_input("Enter date: ")
cashier_name = get_input("Enter cashier name: ")

# Calculate net sale
def netSale(net_sale):
    return net_sale*0.82
# Print output
print("Name of customer: ", customer_name)
print("Name of cashier: ", cashier_name)
print("Date: ", date)
print("Commodity name: ", commodity_name)
print("Commodity price: ", commodity_price)
print("Net sale:", net_sale)