x = int(input('Insert number here: '))

def prime_num(num):
    l = []
    for i in range(2, x):
        if x % i == 0:
            l.append(i)
    if len(l) == 0:
        f = ("I'm a prime number!")
    else:
        l.insert(0, 1)
        l.insert(x, x)
        f = ("I'm not a prime number, I'm a composite number." + " My factors are " + str(l))
    return f
print(prime_num(x))
