'''
Museum Price Challenge 

The problem statement is as follows. Let's assume that we have a museum that has the following 
policy for the admission price based on a full price ticket of $12.50. 
The museum is closed on Mondays. Everyone gets half price discount on Tuesday and Thursdays. 
If you are age between 13 and 20 (including min-max), you will get the discount on Wednesdays. 
If you are younger than 6, or older than 65, your admission if free. 
If you are age between 6 and 12 (including min-max), your admission is half price on the 
Weekend (Saturday and Sunday). Build the program that gives the user to input the day of the week 
and his/her age, then gives the user information about the pricing for him/her. Your program should 
only have three patterns of output 1.) "We are closed on Monday," 2.) "You get half price discount of 
$99.99!", 3.) "You pay full price pf $99.99." Test your program with multiple days and multiple ages – 
before you run the program, determine what the answer should be to check for accuracy. 

BONUS: rather than input the day of the week, use date functions to try and determine what the day of the 
week is based on the current system date. 
'''

import datetime

weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

currdate = datetime.datetime.now()
currday = currdate.weekday()
currdateAsstring = weekDays[currday]

admission = float(12.50)


while True:
    age = int(input("Please enter your age: "))
    if currdateAsstring == "Monday":
        print("The Museum is closed on Mondays.")
    elif age < 6 or age > 65:
        print("Your admission is free!")
    elif currdateAsstring == "Tuesday" or currdateAsstring == " Thursday":
        halfprice = admission/2
        print(f"Admission is half price today! {halfprice:.2f}")
    elif currdateAsstring == "Wednesday" and age >= 13 and age <= 20:
        halfprice = admission/2
        print(f"Admission is half price today! {halfprice:.2f}")
    elif currdateAsstring == "Saturday" or currdateAsstring == "Sunday" and age >= 6 and age <= 12:
        halfprice = admission/2
        print(f"Admission is half price today! {halfprice:.2f}")
    else:
        print(f"{admission}")
    end = input("Do you want to add another ticket? Y or N: ")  #End the loop here by inputting n.
    if end.lower() != "y":
        break

print("Welcome to the Museum!")