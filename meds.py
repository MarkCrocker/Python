import datetime

f = open("meds.txt", "a")

while True:
    meds = input("What medicine did you take? :")
    
    time_taken = int(input("enter how many minutes ago you took this: "))
    when_to_take = int(input("How many minutes until you take again?: "))

    current_time = datetime.datetime.now()
    meds_taken = current_time - datetime.timedelta(minutes = time_taken)
    take_again = meds_taken + datetime.timedelta(minutes = when_to_take)
    
    f.write(f"The current time is {current_time}\n")
    f.write(f"{meds}\n")
    f.write(f"{meds} was taken at {meds_taken}\n")
    f.write(f"{meds} needs to be taken again at {take_again}\n")
    
    
    
    end = input("Would you like to continue? Y or N: ")
    if end.lower() != "y":
        break
        
total = []
with open("meds.txt") as file:
    for line in file:
        line = line.replace("\n","")
        total.append(line)
f.write("We hope you get well soon!")
f.close()