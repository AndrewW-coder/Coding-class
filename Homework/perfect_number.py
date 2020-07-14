for num in range(1, 10000):
    l = []
    for i in range(1, num):
        if num % i == 0:
            l.append(i)
    s = 0
    for j in range(0, len(l)):
        s = s + l[j]
    if s == num:
        print(num)