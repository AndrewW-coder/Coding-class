x = int(input('Insert number here: '))
flag = 1
def prime_number(x):
    flag = 1
    for i in range(2, x):
        if x % i == 0:
            flag = 0
            break
        
    if flag == 1:
        print('This is a prime number.')
    elif flag == 0:
        print('This is not a prime number.')
prime_number(x)
    