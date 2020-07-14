l = [1, 7, 5, 9, 3]
m = l[0]
#Max
for i in range(1, len(l)):
    if m < l[i]:
        m = l[i]
print('The biggest number in the list is %s' %m)
n = l[0]
#Min
for i in range(1, len(l)):
    if n > l[i]:
        n = l[i]
print('The smallest number in the list is %s' %n)
#Average
s = 0
for x in range(0, len(l)):
    s = s + l[x]
a = s / len(l)
print('The average of the list is %s' %a)
#range
sl = sorted(l)
r = sl[len(l)-1] - sl[0]
print('The range of the list is %s' %r)
