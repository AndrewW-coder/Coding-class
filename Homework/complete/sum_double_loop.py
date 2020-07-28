l = [1, 5, 2, 4, 3]
def target_sum(li, target):
    lis = []
    
    for i in range(0, len(li)):
        for j in range(0, len(li)):
            if i != j:
                if li[i] + li[j] == target:
                    s = []
                    s.append(i)
                    s.append(j)
                    lis.append(s)
    for i in range(0, len(lis) - 1):
        if lis[i][0] > lis[i][1]:
            lis.remove(lis[i])


    return lis
print(target_sum(l, 6))