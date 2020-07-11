x = int(input('Insert number here: '))
flag = 1
def prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            flag = 0
        elif x % i != 0:
            flag = 1
    if flag == 0:
        print('This is not a prime number.')
    elif flag == 1:
        print('This is a prime number.')
prime_number(x)
    