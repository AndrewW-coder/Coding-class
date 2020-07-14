l = [3, 15, 7, 6, 3, 7, 8, 9]
m = l[0]
for i in range(1, len(l)-1):
    if m < l[i]:
        m = l[i]
print('The biggest number in the list is %s' %m)
n = l[0]
for i in range(1, len(l)-1):
    if n > l[i]:
        n = l[i]
print('The smallest number in the list is %s' %n)