def consecutive_zeros(num):
    l = []
    for i in range(0, len(str(num))):
        l.append(num[i])
    return(l)
print(consecutive_zeros(5))