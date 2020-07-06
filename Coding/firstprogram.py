x = str(input('Please insert number here: '))
l = []
for i in range(0, len(x), 1):
    l.append(x[i])
reversel = []
for i in range(len(l)-1, -1, -1):
    reversel.append(l[i]) 
    
print(reversel)

if l == reversel:
    print("I'm a palindrone")
else:
    print("I'm not a palindrone")