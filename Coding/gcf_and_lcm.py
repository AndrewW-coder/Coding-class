a = 27 #make this the bigger number
b = 21 #make this the smaller number
l = []
#gcf
for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
        l.append(i)
m = l[0]
for j in range(0, len(l), 1):
    if m < l[j]:
        m = l[j]
print('The greatest common multiple is %s.' %m)

#lcm
for c in range(a, a * b + 1):
    if c % a == 0 and c % b == 0:
        break
print('The least common multiple is %s' %c)


    
    


    