x = int(input('Insert number here: '))
for i in range(2, x):
    if x % i == 0:
        print('This number is not prime number.')
        break
    else:
        print('This is a prime number')
        break