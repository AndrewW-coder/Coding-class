x = int(input('Insert number here: '))

def prime_num(num):
    l = []
    for i in range(2, x):
        if x % i == 0:
            l.append(i)
    if len(l) == 0:
        f = ('Im a prime number!')
    else:
        f = ("I'm not a prime number." + " My factors are " + str(l))
    return f
print(prime_num(x))
