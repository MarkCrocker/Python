balance = input('Enter your balance: ')
transaction = input('Type of transaction: (D or W) ')

if transaction.upper() == 'W':
    withdrawal = input('Please enter withdrawal amount: ')
    withdrawal_total = int(balance) - int(withdrawal)
    print(withdrawal_total)
elif transaction.upper() == 'D':
    deposit = input('Please enter deposit amount: ')
    balance_total = int(balance) + int(deposit)
    print(balance_total)
else:
    print('Invalid transaction type entered')
    print(balance)
    
