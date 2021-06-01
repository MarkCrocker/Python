name = input('enter name: ')
address = input('enter addres: ')
last_month = int(input('last month meter reading: '))
current_month = int(input('current meter reading: '))


print(f'Your total is: ${total_charge:.2f}')


total_kwh = (last_month) + (current_month)
print(f'Total usage for two months: {total_kwh:.2f}')


kwh = 0
if total_kwh < 100:
    kwh = total_kwh * 0.073
    print(f'Total cost of kwh used: ${kwh:.2f}')
elif total_kwh >= 100:
    kwh = total_kwh * 0.069
    print(f'Total cost of kwh used: ${kwh:.2f}')

    
discount_total = 0
discount = 0
if kwh >= 500:
    discount = (kwh * 0.10)
    discount_total = kwh - discount
    print('Discount offered!')
    print(f'Total cost of early payment: ${discount_total:.2f}')
    
    

HST = kwh * 0.13
print(f'HST: ${HST:.2f}')
total_charge = kwh + HST