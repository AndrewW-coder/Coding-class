def flatten(l):
    l1 = []
    for i in range(0, len(l)):
        for j in range(0, len(l[i])):
            l1.append(l[i][j])
    return l1
l = [[1, 2, 3], [4, 5, 6]]
print(flatten(l))

        


