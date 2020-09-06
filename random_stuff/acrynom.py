import random



x = input('What word do you want to input: ')
l = []
for i in range(0, len(x)):
    l.append(x[i])
acrynom = ''
while len(l) > 0:
    n = random.randint(0, len(l)-1)
    acrynom = acrynom + l[n]
    l.remove(l[n])
print(acrynom)
