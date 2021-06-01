
l = list()

while True:
    number = float(input("Please enter a number. Enter 0 to stop. "))
    if number == 0:
        break
    l.append(number)
    
    
subtotal = sum(l)
hst = subtotal * 0.13
total = hst + subtotal

s_l = sorted()

print(f"Numbers entered: {l}")
print(f"Numbers Sorted: {s_l}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"HST: ${hst:.2f}")
print(f"Total: ${total:.2f}")
 