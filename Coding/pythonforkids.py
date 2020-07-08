l = [1, 3, 7, 5]
m = l[0]
for x in range(1, len(l)):
    if m < l[x]:
        m = l[x]
    elif m > l[x]:
        print(m)











