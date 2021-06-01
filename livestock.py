# Farmer George wants to modernize his farming practices. He
# wants a program to track how much produce he has in his
# inventory at any given time. Farmer George wants a program
# that takes in the following information: 

# A vegetable name,


# the amount of that vegetable that was grown (in pounds), 

# the amount of that vegetable that was sold (in pounds), 

# the amount of that vegetable that was fed to livestock (in pounds),


# and the price the vegetable was sold for (in dollars). 


# The program should write all of that information to a file, and then
# calculate and write the following information to the same file:
# The total amount of that vegetable that is left in inventory
# (calculate this by taking the amount that was grown and
# subtracting the amount that was sold and the amount that was
# fed to livestock),


# as well as the total revenue for the sales of
# the vegetable (calculated as the amount of the vegetable sold
# multiplied by the price the vegetable was sold for). Since
# Farmer George grows many types of veggies, the program
# should continue prompting the user for input in a loop and
# should ask the user after each entry if they want to stop. At the
# very end of the program, after the user has stopped entering
# input, we should write the total revenue across *all* of the
# vegetables to the file (calculated as the sum of the revenues of
# all of the individual vegetables). Note, that we should raise an
# exception if the total amount of vegetable that is left is
# negative, since obviously something has gone wrong. Use 
# raise ValueError(“YOUR MESSAGE HERE”)
# to accomplish this. You should also raise a ValueError if any of
# the numerical inputs are negative, such as the number of crops
# grown, or the number of crops sold.

f = open("output.txt", "a")
total_revenue = 0

while True:
    v_name = input("Enter name of vegetable: ")
    v_grown = float(input("Enter amount grown (in lbs): "))
    if v_grown < 0:
        raise("Amount cannot be less than zero.")
    v_sold = float(input("Enter amount sold: "))
    if v_sold < 0:
        raise("Amount cannot be less than zero.")
    v_live = float(input("Enter amount fed to livestock: "))
    if v_live < 0:
        raise("Amount cannot be less than zero.")
    v_price = float(input("Enter price: "))
    
    v_left = v_grown - v_sold - v_live
    if v_left < 0:
        raise("Amount cannot be less than zero.")
    revenue = v_sold * v_price
    total_revenue = total_revenue + revenue
    
    f.write(f"Veggie name: {v_name}\n")
    f.write(f"Amount grown: {v_grown:.2f}\n")
    f.write(f"Amount sold: {v_sold:.2f}\n")
    f.write(f"Amount fed to livestock: {v_live:.2f}\n")
    f.write(f"Price of vegetable per pound: {v_price:.2f}\n")
    f.write(f"Amount remaining: {v_left:.2f}\n")
    f.write(f"Revenue for {v_name}: {revenue:.2f}\n")
    
    end = input("Do you want to continue? Y or N?: ")
    if end.lower() != "y":
        break
    


f.write(f"Total Combined Revenue: {total_revenue:.2f}")