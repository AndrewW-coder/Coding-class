def consecutive_zeros(num):
    word = str(num)
    if len(word) > 1:
        l = []
        t = 0
        for i in range(0, len(word) - 1):
            while int(word[i]) == 0:
                t += 1
                i += 1
                if int(word[i]) == 1:
                    l.append(t)
                    t = 0
    else:
        l = []
        if int(word[0]) == 0:
            l.append(1)
        else:
            l.append(0)
    return max(l)
print(consecutive_zeros(0))