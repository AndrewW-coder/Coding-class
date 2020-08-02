def consecutive_zeros(num):
    l = []
    l1 = []
    word = str(num)
    for i in range(0, len(word)):
        if int(word[i]) == 0:
            l.append(i)
    for i in range(0, len(l)):
        if l[i] + 1 == l[i + 1]:
            l1 = []
            

    
    return l
print(consecutive_zeros(100))