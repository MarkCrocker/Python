rental_days = int(input('Number of days rented: '))
km_beginning = int(input('Number of km on vehicle before leaving: '))
km_end = int(input('Number of km on vehicle upon return: '))

total_km = (km_end) - (km_beginning)
daily_cost = rental_days * 35.00
km_cost = total_km * 0.10
rental = (daily_cost) + (km_cost)
insurance = rental_days * 7.90
subtotal = (daily_cost) + (km_cost) + (insurance)
HST = subtotal * 0.13
total_rental_cost = (subtotal) + (HST)

print(total_km)
print(f'Total for {rental_days} days is: ${daily_cost:.2f}')
print(f'Total cost of km usage is: ${km_cost:.2f}')
print(f'Total cost of rental is: ${rental:.2f}')
print(f'Total insurance cost is: ${insurance:.2f}')
print(f'Subtotal: ${subtotal:.2f}')
print(f'HST: ${HST:.2f}')
print(f'total cost of your rental is: ${total_rental_cost}')