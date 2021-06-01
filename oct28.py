"""
Write a program that will process invoices for a customer. Only process one product or service per invoice. 
Allow user to enter invoices until a termination value is entered.

For each invoice, user will enter:
Customer name:  cust_name = input("enter cust name:" )
phone number: 
service provided:
number of hours required to complete job:
cost of service:

All fields must be entered, the number of hours must be between 1 - 10, and the cost must be greater than 0 and 500.

Calculate labor cost:
num hours * labor rate
Cost is doubled on saturday and Sunday
Bonus: if service is after 6:
labour rate 1.5 for overtime.

Subtotal:
service cost + labour cost
HST = subtotal * hst
total = subtotal + hst

Print a receipt for customer. Include the following:
all costs with appropriate headings and formatted dollar values, and the invoice totals at the end.At top.
HST Reg # of 123-53-34553-345 and a message at the end of the invoice thanking the customer for the opportunity to serve them.
"""

import datetime

f = open("/home/ubuntu/environment/Practice/defaults.txt", "r")

invoice = int(f.readline())
hst = float(f.readline())
labour_rate = float(f.readline())
discount = float(f.readline())

f.close()

print("Invoice #", invoice)
print("HST Rate", hst)
print("Labour Rate", labour_rate)
print("Discount Rate on orders over $500", discount)



weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

currdate = datetime.datetime.now()
currday = currdate.weekday()
currdateAsstring = weekDays[currday]
# Input for invoice:
while True:
    cust_name = input("\n\nEnter customer name: ")
    
    phone_number = int(input(f"Enter {cust_name}'s phone number: "))
    
    service_provided = input("Enter service provided: ")
    
    num_hours = int(input(f"Enter number of hours required for {service_provided} install: "))
    if num_hours < 1 or num_hours > 10:
        print("You must enter a value from 1 to 10")
        num_hours = int(input(f"Enter number of hours required for {service_provided}: "))
    
    service_cost = int(input(f"Enter cost of {service_provided}: $"))
    if service_cost == 0:
        print("You must enter a number higher than 0")
        service_cost = int(input(f"Enter cost of {service_provided}: $"))
    
    if currdateAsstring == "Saturday" or currdateAsstring == "Sunday":
        service_cost = service_cost * 2
        print("double rate for Saturday and Sunday")
    
    
    labour_cost = num_hours * labour_rate #(Needs to use variable rate from defaults.txt
    
    subtotal = service_cost + labour_cost
    if subtotal >= 500:
        subtotal = subtotal - (subtotal * discount)
        print(f"Your subtotal {subtotal} with a {discount} discount")
        
    hst = subtotal * hst #(needs to use variable rate from file defaults.txt )
    total = subtotal + hst
    
    
    print(f"Labor cost = ${labour_cost:.2f}")
    print(f"Subtotal = ${subtotal:.2f}")
    print(f"HST = {hst:.2f}")
    print(f"Total = ${total:.2f}")
      
    end = input("Would you like to enter another invoice? Y or N: ")
    if end.lower() != "y":
        break

f = open("receipt.txt", "w")
f.write(f"labour cost: {labour_cost:.2f}\n")
f.write(f"subtotal: {subtotal:.2f}\n")
f.write(f"hst: {hst:.2f}\n")
f.write(f"total: {total:.2f}\n")
    
f.close()
#Input for labour cost:
# Calculate labor cost:
# num hours * labor rate
# Cost is doubled on saturday and Sunday
# Bonus: if service is after 6:
# labour rate 1.5 for overtime.

    # labour_cost = num_hours * labour_rate #(Needs to use variable rate from defaults.txt
    
#Create a loop for doubled rate on saturday and sunday, and overtime after 6

# Subtotal:
# service cost + labour cost
# HST = subtotal * hst
# total = subtotal + hst

    