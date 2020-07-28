l = [3, 3, -6, -5, -1, 6]
def element(l):
    lis = []
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            for h in range(0, len(l)):
                if j != i != h:
                    if h < i < j:
                        if l[i] + l[j] + l[h] == 0:
                            lis.append((l[i], l[h], l[j]))
    
    return lis
print(element(l))

    
                        

