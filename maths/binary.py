def binary(num):
    for i in range(num + 1, -1, -1):
        if 2 ** i <= num:
            m = i
            num = num - 2 ** m
            break
    l = []
    
    for i in range(0, m + 1):
        l.append('0')
    l[0] = '1'
    for i in range(0, m + 1):
        if 2 ** m > num:
            num = num
            m -= 1
        if 2 ** m <= num:
            l[m - 1] = '1'
            m -= 1
    s = ''.join(l)


    return s
x = int(input('Insert number here: '))
print(binary(x))












    

    
        



