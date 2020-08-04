#Deposit
#getting cash
#check account
#change pin
#check account
choice = 0
balance = 0
print(' _________________________________________________')
print('|           /\     |`````````|    |``\    /``|    |')
print('|          /  \     ```|  |```    |   \  /   |    |')
print('|         /````\       |  |       |    ``    |    |')
print('|        /      \      |__|       |__/\__/\__|    |')
print('|       [1] Deposit Money   [2] Withdraw Cash     |')
print('|                                                 |')
print('|       [3] Check Balance   [4] Change Password   |')
print('|                                                 |')
print('|       [5] Check Account   [6] Exit               |')
print(' `````````````````````````````````````````````````')
# passcode = input('What do you want your passcode to be (6 digits): ')
while choice != 6:

    balance = balance
    choice = int(input('What do you want to do: '))
    if choice == 1:
        money = int(input('How much money do you want to deposit: '))
        balance += money
        print('Your balance is now $' + str(balance) + '.')
    elif choice == 2:
        withdraw = int(input(('How much money do you want to withdraw: ')))
        balance -= withdraw
        print('Your balance is now $' + str(balance) + '.')
if choice == 6:
    print('Okay, ATM is closing.')
    
    