l = [1, 2, 2, 3, 3, 3, 5, 5, 4]
l2 = []
for x in range(0, len(l)):
    if l[x] not in l2:
        l2.append(l[x])
print(l2)