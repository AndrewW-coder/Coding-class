word = ('HeLLo')
l = []
for x in range(0, len(word)):
    if word[x].isupper() == True:
        l.append(x)
print(l)
