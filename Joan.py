# Write a program that adds up the measured numbers for joan.
# Since bacterial cultures sometimes die off, or new ones get added to the mix, it is unknown how many numbers
# will need to be input on any given day. 
# Write a program that takes in any number of numbers with decimal places, adds them all up, and then outputs the total

s = 0
l = []

while True:
    num = float(input("Enter Number [Type 0 to end]\n"))
    if num == 0:
        break
    
    s = s + num
    l.append(num)

print(f"The total sum is: {s}")

f = open("Joan.data", "w")
c = 1
for num in l:
    f.write(f"Culture # {num}\n")
    c = c + 1
f.write(f"Total: {s}\n")
f.close()
    