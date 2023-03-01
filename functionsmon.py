def customer(name, age, loc, sal):
    print("welcome:", name)
    print("your location is:", loc)
    print("your salary:")
    return sal
name = input("please enter your name")
age = int(input("please enter your age"))
loc = input("please enter your location")
sal = float(input("please enter your salary"))

def paye(rate):
    
    customerSalary = customer(name, age, loc, )
    customerRate = customerSalary*(rate/100)
    netSalary = customerSalary- customerRate
    print("your final paye:", netSalary)
rate = float(input("please enter your tax:"))   
paye(rate)
#function that invokes another funtion is called a calling function
    
