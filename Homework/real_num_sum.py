l = [1, 2, 3, 4 ,5]
def sum_num(li, target):
    lis = []
    for i in li:
        m = target - i
        if m in li:
            lis = []
            lis.append((i,m))
    return lis
print(sum_num(l, 6))
            
            