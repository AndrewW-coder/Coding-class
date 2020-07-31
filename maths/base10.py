def base10(num):
    m = int(input('What base is the number?: '))
    word = str(num)
    s = 0
    for i in range(0, len(word)):
        n = num % 10
        s += n * m ** i
        num //= 10
    return s
x = int(input('Insert number here: '))
print(base10(x))
