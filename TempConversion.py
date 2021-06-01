# write a temperature conversion program that will process celsius temperatures from -100 degree to 100 degrees.
# for each temp, the program will calculate the temp in Fahrenheit using the formula:
# F = (9/5C) + 32
#  print(f'{k:.2f} K')
# print(f'{f:.2f} F')
celsius = 0

while True:
    try:
        celsius = int(input('Enter the temperature you wish to convert: '))
        if (celsius < -100) or (celsius > 100):
            print("Please input a value from -100 to 100")
        if celsius == -90:
            print('Lowest Recorded Temperature')
        elif celsius == 0:
            print('Freezing Point of Water')
        elif celsius == 20:
            print('Average Room Temperature')
        elif celsius == 100:
            print('Boiling Point of Water')
        f = (celsius * 9/5) +32
        k = celsius + 273.15
        print(f'{celsius} degrees Celsius converted to: \nFahrenheit: {f:.2f}F'f'\nKelvin: {k:.2f}K')
        cont = input("Do you want to continue? Y or N?")
        if cont.upper() != "Y":
            break
        

# f = (celsius * 9/5) +32
# k = celsius + 273.15
# while True:
#     print('Enter your age:')
#     age = input()
#     try:
#         age = int(age)
#     except:
#         print('Please use numeric digits.')
#         continue
#     if age < 1:
#         print('Please enter a positive number.')
#         continue
#     break
# while True:
#     print('Enter your temperature to convert: ')
#     temperature = input()
#     try:
#         temperature = input(f)
                      