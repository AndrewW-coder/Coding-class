l = [1, 3, 5, 4, 2]
m = l[0]
l2 = []
for x in range(1, len(l)):
    if m < l[x]:
        l2.append(m)
    elif m > l[x]:
        l2.append(l[x])
print(l2)
