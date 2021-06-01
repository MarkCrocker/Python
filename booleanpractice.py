"""The problem statement is as follows. Let's assume that we have a museum that has the following policy for 
the admission price based on a full price ticket of $12.50. 

 

The museum is closed on Mondays. 
if day.lower == monday
Everyone gets half price discount on Tuesday and Thursdays. 
if day.lower == tuesday or day.lower == thursday

If you are age between 13 and 20 (including min-max), you will get the discount on Wednesdays. 
if age >= 13 and <= 20
discount on wednesday
If you are younger than 6, or older than 65, your admission if free. 
If you are age between 6 and 12 (including min-max), your admission is half price on the Weekend 
(Saturday and Sunday). 
Build the program that gives the user to input the day of the week and his/her age, then gives the user 
information about the pricing for him/her. Your program should only have three patterns of output 1.) 
"We are closed on Monday," 2.) "You get half price discount of $!", 3.) "You pay full price pf 12.50." 
"""



    


ticket = 0
admission = float(12.50)
while True:
    day = input("Please enter the day: ")
    if day.lower() == "monday":
        print("Closed on Mondays")
    else:
        if day.lower() == "tuesday" or day.lower() == "thursday":
            ticket = admission - (admission * 0.50)
            print("half price discount!")
        elif day.lower() != "tuesday" or day.lower() != "thursday":
            print("No discount")
    
    age = int(input("Please enter your age: "))
    if (age < 6 or age > 65):
        print("Your admission cost is $0.00")
    elif (age >= 6 or age <= 12) and (day.lower() == "saturday" or day.lower() == "sunday"):
        ticket = admission - (admission * 0.50)
    elif (age >= 13 or age <= 20) and day.lower() == "wednesday":
        ticket = admission - (admission * 0.50)
    print(f"Your ticket is {ticket:.2f}")
    cont = input("would you like to continue? Y or N: ")
    if cont.lower() != "y":
        break