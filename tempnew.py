# n = 0
# while True:
#   try:
#     n = int(input("Please input a number between 3 and 20 (inclusive)."))
#   except:
#     print("Invalid input! Can't convert input to a number. Please try again...")
#   else:
#     if (n >= 3) and (n <= 20):
#       break
#     else:
#       print("Invalid input! The input must be between 3 and 20, inclusive. Please try again...")
      
# print(n)
celsius = 0


while True:
    try:
        celsius = int(input('Please input a number from -100 to 100. '))
        f = (celsius * 9/5) +32
        k = celsius + 273.15
        print(f'{celsius} degrees Celsius converted to: \nFahrenheit: {f:.2f}F'f'\nKelvin: {k:.2f}K'
        if celsius == -90:
            print('Lowest Recorded Temperature')
        elif celsius == 0:
            print('Freezing Point of Water')
        elif celsius == 20:
            print('Average Room Temperature')
        elif celsius == 100:
            print('Boiling Point of Water')
    except:
        print('Invalid input! Please try again!')
)
