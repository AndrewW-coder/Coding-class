x = str(input('Enter phrase here: '))
reversel = []
l = []
for i in range(0, len(x), 1):
    l.append(x[i])
for i in range(len(l) -1, -1, -1):
    reversel.append(l[i])
s = ''
for i in range(0, len(reversel)):
    s = s + reversel[i]
print(s)











