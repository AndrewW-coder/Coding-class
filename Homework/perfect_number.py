for num in range(1, 10000):
    sum = 0
    for i in range(1, int(num/2+1)):
        if num % i == 0:
            sum += i
    if num == sum:
        print(num)
    