def thousands_seperator(num):
    word = str(num)
    l = []
    for i in range(0, len(word)):
        l.append(word[i])
    for i in range(len(word) - 3, 0, -3):
        l.insert(i, ',')
    s = ''.join(l)
    return(s)
print(thousands_seperator(1000))
