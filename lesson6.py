#I
number = input("What is your employee number?")
name = input("What is your name?")
location = input("Where did you go?")
start = input("When did you go?")
end = input("When did you return?")
days = input("How many days?")
car = input("Did you use your own car (O) or a rental car (R)")
km = 0
if car == "O":
    km = int(input("How many km did you drive?"))

#P
pd = 0
if days < "4":
    pd = 85 * days
else:
    pd = 100 * days
mileage = 0
if car == "O":
    mileage = 0.10 * km
else:
    mileage = 56 * days
claim = pd + days
hst = float(0.13) * pd
total = claim + hst

#O

print("Employee Name: {}".format(name))
print("Employee Number: {}".format(number))
print("Location: {}".format(location))
print("Trip Start: {}".format(start))
print("Trip End: {}".format(end))
print("Number of Days: {}".format(days))
if car == "O":
    print("Employee used own car")
else:
    print("Employee rented a vehicle")
if car == "O":
    print("Number of KM: {}".format(km))
print("Per Diem: {}".format(pd))
print("Mileage Driven: {}".format(mileage))
print("Claimed Amount: {}".format(claim))
print("HST: {}".format(hst))
print("Total Cost of Trip: {}".format(total))