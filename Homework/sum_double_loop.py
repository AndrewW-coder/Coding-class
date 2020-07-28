l = [1, 5, 2, 4, 3]
def target_sum(li, target):
    lis = []
    for i in range(0, len(li)):
        for j in range(0, len(li)):
            if li[i] + li[j] == target:
                s = []
                s.append(i)
                s.append(j)
                lis.append(s)
    # for i in range(0, len(lis) - 1):
    #     for j in range(0, len(lis) - 1):
    #         while i != j: 
    #             if lis[i].sort() == lis[j].sort():
    #                 lis.remove(lis[j])



    
    return lis
print(target_sum(l, 6))